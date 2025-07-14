import requests
from ebooklib import epub
import markdown
import sys
import os
import json
import signal

# 全局变量用于保存进度
progress_file = None
current_progress = {}

def signal_handler(signum, frame):
    """处理中断信号，保存进度后退出"""
    print("\n收到中断信号，正在保存翻译进度...")
    save_progress()
    print("进度已保存，程序退出")
    sys.exit(0)

def save_progress():
    """保存翻译进度到文件"""
    if progress_file and current_progress:
        with open(progress_file, 'w', encoding='utf-8') as f:
            json.dump(current_progress, f, ensure_ascii=False, indent=2)
        print(f"翻译进度已保存到: {progress_file}")

def load_progress(progress_file):
    """从文件加载翻译进度"""
    if os.path.exists(progress_file):
        try:
            with open(progress_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"加载进度文件失败: {e}")
    return {"translated_paragraphs": [], "total_paragraphs": 0, "source_lang": "", "api_key": ""}

def read_markdown(file_path):
    if not os.path.exists(file_path):
        print(f"错误：文件 {file_path} 不存在")
        sys.exit(1)
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def split_paragraphs(md_content):
    # 按双换行分段
    return [p.strip() for p in md_content.split('\n\n') if p.strip()]

def translate(text, api_key, source_lang):
    # 使用DeepSeek Chat API进行翻译
    url = "https://api.deepseek.com/v1/chat/completions"
    
    # 构建翻译提示
    lang_map = {"en": "英语", "fr": "法语"}
    source_lang_name = lang_map.get(source_lang, source_lang)
    
    prompt = f"""请将以下{source_lang_name}文本翻译成中文，保持原文的格式和结构：

{text}

请只返回翻译结果，不要添加任何解释。"""
    
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.3,
        "max_tokens": 4000
    }
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content'].strip()
        else:
            print(f"翻译失败: {response.status_code} - {response.text}")
            return text
    except Exception as e:
        print(f"翻译请求异常: {e}")
        return text

def paragraphs_translate(paragraphs, api_key, source_lang, progress_file):
    """翻译段落，支持进度保存和恢复"""
    global current_progress
    
    # 加载已有进度
    progress = load_progress(progress_file)
    translated_paragraphs = progress.get("translated_paragraphs", [])
    
    # 检查是否可以继续之前的进度
    if (len(translated_paragraphs) > 0 and 
        progress.get("total_paragraphs") == len(paragraphs) and
        progress.get("source_lang") == source_lang):
        
        print(f"发现已有翻译进度，已翻译 {len(translated_paragraphs)}/{len(paragraphs)} 段落")
        choice = input("是否继续之前的翻译进度？(y/n): ").lower().strip()
        if choice != 'y':
            translated_paragraphs = []
            progress = {"translated_paragraphs": [], "total_paragraphs": len(paragraphs), 
                       "source_lang": source_lang, "api_key": api_key}
    else:
        # 开始新的翻译
        translated_paragraphs = []
        progress = {"translated_paragraphs": [], "total_paragraphs": len(paragraphs), 
                   "source_lang": source_lang, "api_key": api_key}
    
    current_progress = progress
    
    # 设置中断信号处理
    signal.signal(signal.SIGINT, signal_handler)
    
    total = len(paragraphs)
    start_index = len(translated_paragraphs)
    
    print(f"开始翻译，从第 {start_index + 1} 段开始...")
    
    for i in range(start_index, total):
        print(f"翻译进度: {i + 1}/{total} ({(i + 1) * 100 // total}%)")
        
        translated_text = translate(paragraphs[i], api_key, source_lang)
        translated_paragraphs.append(translated_text)
        
        # 更新进度
        current_progress["translated_paragraphs"] = translated_paragraphs
        
        # 每翻译10段保存一次进度
        if (i + 1) % 10 == 0:
            save_progress()
            print(f"已保存进度到第 {i + 1} 段")
    
    # 翻译完成，保存最终进度
    save_progress()
    print("翻译完成！")
    
    return translated_paragraphs

def md_to_epub(translated_md, output_path, title="翻译电子书"):
    html_content = markdown.markdown(translated_md)
    book = epub.EpubBook()
    book.set_title(title)
    chapter = epub.EpubHtml(title='章节1', file_name='chap_01.xhtml', content=html_content)
    book.add_item(chapter)
    book.spine = ['nav', chapter]
    epub.write_epub(output_path, book, {})

def main():
    if len(sys.argv) < 5:
        print("用法: python translate_md_to_epub.py <input.md> <output.epub> <api_key> <source_lang: en|fr>")
        print("或者设置环境变量 DEEPSEEK_API_KEY")
        sys.exit(1)
    
    input_md = sys.argv[1]
    output_epub = sys.argv[2]
    api_key = sys.argv[3]
    source_lang = sys.argv[4]
    
    # 如果API密钥以<开头，尝试从环境变量获取
    if api_key.startswith('<') and api_key.endswith('>'):
        api_key = os.getenv('DEEPSEEK_API_KEY')
        if not api_key:
            print("错误：请在命令行中直接提供API密钥，或设置环境变量 DEEPSEEK_API_KEY")
            sys.exit(1)
    
    if source_lang not in ["en", "fr"]:
        print("source_lang 只支持 'en' 或 'fr'")
        sys.exit(1)
    
    # 设置进度文件路径
    global progress_file
    progress_file = f"{os.path.splitext(input_md)[0]}_progress.json"
    
    print(f"开始处理文件: {input_md}")
    print(f"输出文件: {output_epub}")
    print(f"进度文件: {progress_file}")
    print(f"源语言: {source_lang}")
    
    md_content = read_markdown(input_md)
    print(f"文件大小: {len(md_content)} 字符")
    
    paragraphs = split_paragraphs(md_content)
    print(f"段落数量: {len(paragraphs)}")
    
    try:
        translated_paragraphs = paragraphs_translate(paragraphs, api_key, source_lang, progress_file)
        translated_md = '\n\n'.join(translated_paragraphs)
        
        md_to_epub(translated_md, output_epub)
        print(f"转换完成，输出文件: {output_epub}")
        
        # 翻译完成后删除进度文件
        if os.path.exists(progress_file):
            os.remove(progress_file)
            print(f"已删除进度文件: {progress_file}")
            
    except KeyboardInterrupt:
        print("\n用户中断程序")
        save_progress()
        print("进度已保存，可以稍后继续翻译")
    except Exception as e:
        print(f"程序异常: {e}")
        save_progress()
        print("进度已保存")

if __name__ == "__main__":
    main() 