#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
段落缩减脚本
将markdown文件中的段落缩减到指定数量
"""

import re
import sys
from typing import List, Tuple

def read_markdown_file(filename: str) -> str:
    """读取markdown文件"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"错误：找不到文件 {filename}")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"错误：无法解码文件 {filename}，请检查文件编码")
        sys.exit(1)

def split_into_paragraphs(content: str) -> List[str]:
    """将内容分割成段落"""
    # 使用双换行符分割段落
    paragraphs = re.split(r'\n\s*\n', content.strip())
    # 过滤空段落
    return [p.strip() for p in paragraphs if p.strip()]

def merge_paragraphs(paragraphs: List[str], target_count: int) -> List[str]:
    """将段落合并到目标数量"""
    if len(paragraphs) <= target_count:
        return paragraphs
    
    # 计算需要合并的段落数量
    total_paragraphs = len(paragraphs)
    merge_count = total_paragraphs - target_count
    
    # 计算每个合并组应该包含的段落数量
    paragraphs_per_group = total_paragraphs // target_count
    remainder = total_paragraphs % target_count
    
    merged_paragraphs = []
    current_index = 0
    
    for i in range(target_count):
        # 计算当前组应该包含的段落数量
        if i < remainder:
            group_size = paragraphs_per_group + 1
        else:
            group_size = paragraphs_per_group
        
        # 提取当前组的段落
        group_paragraphs = paragraphs[current_index:current_index + group_size]
        
        # 合并段落
        merged_text = '\n\n'.join(group_paragraphs)
        merged_paragraphs.append(merged_text)
        
        current_index += group_size
    
    return merged_paragraphs

def preserve_structure(paragraphs: List[str], target_count: int) -> List[str]:
    """保持文档结构，智能合并段落"""
    if len(paragraphs) <= target_count:
        return paragraphs
    
    # 识别标题和特殊段落
    title_pattern = re.compile(r'^#+\s+', re.MULTILINE)
    list_pattern = re.compile(r'^[\-\*\+]\s+', re.MULTILINE)
    
    # 分类段落
    titles = []
    lists = []
    regular_paragraphs = []
    
    for i, para in enumerate(paragraphs):
        if title_pattern.match(para):
            titles.append((i, para))
        elif list_pattern.match(para):
            lists.append((i, para))
        else:
            regular_paragraphs.append((i, para))
    
    # 计算需要保留的常规段落数量
    available_slots = target_count - len(titles) - len(lists)
    
    if available_slots <= 0:
        # 如果标题和列表太多，需要合并一些
        return merge_paragraphs(paragraphs, target_count)
    
    # 合并常规段落
    if len(regular_paragraphs) > available_slots:
        regular_texts = [p[1] for p in regular_paragraphs]
        merged_regular = merge_paragraphs(regular_texts, available_slots)
        
        # 重新构建段落列表
        result = []
        title_idx = 0
        list_idx = 0
        regular_idx = 0
        
        for i in range(len(paragraphs)):
            if title_idx < len(titles) and titles[title_idx][0] == i:
                result.append(titles[title_idx][1])
                title_idx += 1
            elif list_idx < len(lists) and lists[list_idx][0] == i:
                result.append(lists[list_idx][1])
                list_idx += 1
            elif regular_idx < len(merged_regular):
                result.append(merged_regular[regular_idx])
                regular_idx += 1
                # 跳过原始段落中对应的常规段落
                while (regular_idx < len(regular_paragraphs) and 
                       regular_paragraphs[regular_idx][0] < len(paragraphs) and
                       regular_paragraphs[regular_idx][0] <= i + 1):
                    regular_idx += 1
        
        return result
    else:
        return paragraphs

def write_markdown_file(filename: str, content: str):
    """写入markdown文件"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"已成功写入文件：{filename}")
    except Exception as e:
        print(f"写入文件时出错：{e}")
        sys.exit(1)

def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("用法：python reduce_paragraphs.py <输入文件> [目标段落数] [输出文件]")
        print("示例：python reduce_paragraphs.py book_merged.md 10 book_reduced.md")
        sys.exit(1)
    
    input_file = sys.argv[1]
    target_count = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    output_file = sys.argv[3] if len(sys.argv) > 3 else f"{input_file.rsplit('.', 1)[0]}_reduced.md"
    
    print(f"正在处理文件：{input_file}")
    print(f"目标段落数：{target_count}")
    print(f"输出文件：{output_file}")
    
    # 读取文件
    content = read_markdown_file(input_file)
    
    # 分割段落
    paragraphs = split_into_paragraphs(content)
    print(f"原始段落数：{len(paragraphs)}")
    
    # 缩减段落
    reduced_paragraphs = preserve_structure(paragraphs, target_count)
    print(f"缩减后段落数：{len(reduced_paragraphs)}")
    
    # 合并段落
    final_content = '\n\n'.join(reduced_paragraphs)
    
    # 写入文件
    write_markdown_file(output_file, final_content)
    
    print("段落缩减完成！")

if __name__ == "__main__":
    main() 