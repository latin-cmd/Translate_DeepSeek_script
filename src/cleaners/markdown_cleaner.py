import re

def clean_markdown(input_file, output_file):
    """清理Markdown文件中的多余空行和特殊字符"""
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. 移除连续的空行，只保留一个空行
    cleaned_content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
    
    # 2. 移除行首行尾的空白字符（空格、制表符等）
    cleaned_content = re.sub(r'^[ \t]+|[ \t]+$', '', cleaned_content, flags=re.MULTILINE)
    
    # 3. 移除除了文字、数字、标点符号和基本空格之外的特殊字符
    # 保留：字母、数字、中文、基本标点符号、空格、换行符
    # 移除：制表符、特殊空白字符、控制字符等
    cleaned_content = re.sub(r'[^\w\s\u4e00-\u9fff\u3000-\u303f\uff00-\uffef\n\r.,!?;:()\[\]{}""''\-\u2013\u2014\u2026]', '', cleaned_content)
    
    # 4. 规范化空格：将多个连续空格替换为单个空格
    cleaned_content = re.sub(r' +', ' ', cleaned_content)
    
    # 5. 移除空行中的空格
    cleaned_content = re.sub(r'^\s+$', '', cleaned_content, flags=re.MULTILINE)
    
    # 6. 移除文件开头和结尾的多余空行
    cleaned_content = cleaned_content.strip()
    
    # 7. 确保段落之间只有一个空行
    cleaned_content = re.sub(r'\n\s*\n\s*\n+', '\n\n', cleaned_content)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)
    
    print(f"清理完成！原文件: {input_file}")
    print(f"清理后文件: {output_file}")
    print(f"清理前字符数: {len(content)}")
    print(f"清理后字符数: {len(cleaned_content)}")

if __name__ == "__main__":
    clean_markdown("book.md", "book_clean.md")


def main():
    """Command line entry point."""
    import sys
    if len(sys.argv) != 3:
        print("Usage: python markdown_cleaner.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    clean_markdown(input_file, output_file) 