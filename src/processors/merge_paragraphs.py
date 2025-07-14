import re

def merge_paragraphs(input_file, output_file, min_length=100):
    """合并短段落，减少段落数量"""
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 按双换行分割段落
    paragraphs = content.split('\n\n')
    
    merged_paragraphs = []
    current_paragraph = ""
    
    for paragraph in paragraphs:
        paragraph = paragraph.strip()
        if not paragraph:  # 跳过空段落
            continue
            
        # 如果当前段落太短，尝试合并
        if len(current_paragraph) < min_length and current_paragraph:
            # 合并段落，用空格分隔
            current_paragraph += " " + paragraph
        else:
            # 保存当前段落，开始新段落
            if current_paragraph:
                merged_paragraphs.append(current_paragraph)
            current_paragraph = paragraph
    
    # 添加最后一个段落
    if current_paragraph:
        merged_paragraphs.append(current_paragraph)
    
    # 重新组合内容
    merged_content = '\n\n'.join(merged_paragraphs)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(merged_content)
    
    print(f"段落合并完成！")
    print(f"原文件: {input_file}")
    print(f"合并后文件: {output_file}")
    print(f"原段落数: {len(paragraphs)}")
    print(f"合并后段落数: {len(merged_paragraphs)}")
    print(f"减少段落数: {len(paragraphs) - len(merged_paragraphs)}")
    print(f"平均段落长度: {len(merged_content) // len(merged_paragraphs)} 字符")

if __name__ == "__main__":
    # 可以调整min_length参数来控制合并的阈值
    merge_paragraphs("book_clean.md", "book_merged.md", min_length=150)


def main():
    """Command line entry point."""
    import sys
    if len(sys.argv) != 3:
        print("Usage: python merge_paragraphs.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    merge_paragraphs(input_file, output_file) 