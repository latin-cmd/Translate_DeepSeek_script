import json
import os
import sys

def decode_progress(progress_file, output_format="md"):
    """解码翻译进度文件，提取已翻译的段落"""
    
    if not os.path.exists(progress_file):
        print(f"错误：进度文件 {progress_file} 不存在")
        return
    
    try:
        with open(progress_file, 'r', encoding='utf-8') as f:
            progress_data = json.load(f)
    except Exception as e:
        print(f"读取进度文件失败: {e}")
        return
    
    # 提取翻译进度信息
    translated_paragraphs = progress_data.get("translated_paragraphs", [])
    total_paragraphs = progress_data.get("total_paragraphs", 0)
    source_lang = progress_data.get("source_lang", "unknown")
    
    if not translated_paragraphs:
        print("进度文件中没有已翻译的段落")
        return
    
    print(f"找到翻译进度:")
    print(f"- 已翻译段落数: {len(translated_paragraphs)}")
    print(f"- 总段落数: {total_paragraphs}")
    print(f"- 源语言: {source_lang}")
    print(f"- 翻译进度: {len(translated_paragraphs)/total_paragraphs*100:.1f}%")
    
    # 生成输出文件名
    base_name = os.path.splitext(progress_file)[0].replace("_progress", "")
    if output_format.lower() == "md":
        output_file = f"{base_name}_translated.md"
    else:
        output_file = f"{base_name}_translated.txt"
    
    # 提取翻译内容
    translated_content = []
    for i, item in enumerate(translated_paragraphs, 1):
        if isinstance(item, dict):
            # 如果是字典格式，提取翻译后的文本
            translated_text = item.get("translated", item.get("text", str(item)))
        else:
            # 如果是字符串格式，直接使用
            translated_text = str(item)
        
        if output_format.lower() == "md":
            # Markdown格式：添加段落分隔
            translated_content.append(translated_text)
        else:
            # TXT格式：添加段落编号
            translated_content.append(f"段落 {i}: {translated_text}")
    
    # 写入文件
    content = "\n\n".join(translated_content)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"翻译内容已保存到: {output_file}")
    print(f"文件大小: {len(content)} 字符")

def list_progress_files():
    """列出当前目录下的所有进度文件"""
    progress_files = [f for f in os.listdir('.') if f.endswith('_progress.json')]
    
    if not progress_files:
        print("当前目录下没有找到进度文件")
        return
    
    print("找到以下进度文件:")
    for i, file in enumerate(progress_files, 1):
        try:
            with open(file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                translated_count = len(data.get("translated_paragraphs", []))
                total_count = data.get("total_paragraphs", 0)
                progress = f"{translated_count}/{total_count}" if total_count > 0 else f"{translated_count}"
                print(f"{i}. {file} - 进度: {progress}")
        except:
            print(f"{i}. {file} - 读取失败")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使用方法:")
        print("python decode_progress.py <进度文件> [输出格式]")
        print("python decode_progress.py --list")
        print("\n输出格式: md (Markdown) 或 txt (纯文本)")
        sys.exit(1)
    
    if sys.argv[1] == "--list":
        list_progress_files()
    else:
        progress_file = sys.argv[1]
        output_format = sys.argv[2] if len(sys.argv) > 2 else "md"
        decode_progress(progress_file, output_format) 