import requests
from ebooklib import epub
import markdown
import sys
import os

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

def paragraphs_translate(paragraphs, api_key, source_lang):
    translated = []
    total = len(paragraphs)
    for i, p in enumerate(paragraphs, 1):
        print(f"翻译进度: {i}/{total}")
        translated.append(translate(p, api_key, source_lang))
    return translated

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
    
    print(f"开始处理文件: {input_md}")
    print(f"输出文件: {output_epub}")
    print(f"源语言: {source_lang}")
    
    md_content = read_markdown(input_md)
    print(f"文件大小: {len(md_content)} 字符")
    
    paragraphs = split_paragraphs(md_content)
    print(f"段落数量: {len(paragraphs)}")
    
    translated_paragraphs = paragraphs_translate(paragraphs, api_key, source_lang)
    translated_md = '\n\n'.join(translated_paragraphs)
    
    md_to_epub(translated_md, output_epub)
    print(f"转换完成，输出文件: {output_epub}")

if __name__ == "__main__":
    main() 