# 翻译工具集 (Translate Direct)

这是一个用于处理Markdown文档翻译的Python工具集，支持文档清理、段落处理、翻译和进度管理。

## 功能特性

- **文档清理**: 清理Markdown文件中的多余空行和特殊字符
- **段落处理**: 合并短段落或缩减段落数量
- **智能翻译**: 使用DeepSeek API进行中英文翻译
- **进度管理**: 支持翻译进度保存和恢复
- **格式转换**: 将翻译后的内容转换为EPUB电子书格式
- **进度解码**: 从进度文件中提取已翻译的内容

## 安装依赖

```bash
pip install -r requirements.txt
```

## 工具说明

### 1. 文档清理 (clean_md.py)

清理Markdown文件中的格式问题：

```bash
python clean_md.py
```

功能：
- 移除连续空行
- 清理行首行尾空白字符
- 移除特殊控制字符
- 规范化空格
- 确保段落间只有一个空行

### 2. 段落合并 (merge_paragraphs.py)

合并短段落以减少段落数量：

```bash
python merge_paragraphs.py
```

参数：
- `min_length`: 最小段落长度阈值（默认150字符）

### 3. 段落缩减 (reduce_paragraphs.py)

智能缩减段落数量，保持文档结构：

```bash
python reduce_paragraphs.py <输入文件> [目标段落数] [输出文件]
```

示例：
```bash
python reduce_paragraphs.py book_merged.md 10 book_reduced.md
```

特性：
- 保持标题和列表结构
- 智能合并常规段落
- 支持自定义目标段落数

### 4. 翻译工具 (translate_md_to_epub.py)

使用DeepSeek API翻译Markdown文件并转换为EPUB：

```bash
python translate_md_to_epub.py <input.md> <output.epub> <api_key> <source_lang>
```

参数：
- `input.md`: 输入的Markdown文件
- `output.epub`: 输出的EPUB文件
- `api_key`: DeepSeek API密钥
- `source_lang`: 源语言 (en/fr)

示例：
```bash
python translate_md_to_epub.py book.md book_translated.epub your_api_key en
```

特性：
- 支持进度保存和恢复
- 中断后可继续翻译
- 自动生成进度文件
- 支持英语和法语翻译

### 5. 进度解码 (decode_progress.py)

从翻译进度文件中提取已翻译的内容：

```bash
python decode_progress.py <进度文件> [输出格式]
```

示例：
```bash
python decode_progress.py book_progress.json md
python decode_progress.py book_progress.json txt
```

功能：
- 显示翻译进度统计
- 提取已翻译内容
- 支持Markdown和TXT格式输出
- 列出所有进度文件

## 工作流程

1. **文档预处理**:
   ```bash
   python clean_md.py          # 清理原始文档
   python merge_paragraphs.py  # 合并短段落
   python reduce_paragraphs.py # 缩减段落数量（可选）
   ```

2. **翻译处理**:
   ```bash
   python translate_md_to_epub.py book_merged.md book_translated.epub your_api_key en
   ```

3. **进度查看**:
   ```bash
   python decode_progress.py book_merged_progress.json
   ```

## 文件说明

- `clean_md.py`: 文档清理工具
- `merge_paragraphs.py`: 段落合并工具
- `reduce_paragraphs.py`: 段落缩减工具
- `translate_md_to_epub.py`: 翻译和EPUB转换工具
- `decode_progress.py`: 进度解码工具
- `requirements.txt`: Python依赖包

## 注意事项

1. **API密钥**: 需要有效的DeepSeek API密钥
2. **文件编码**: 所有文件使用UTF-8编码
3. **进度文件**: 翻译过程中会自动生成`*_progress.json`文件
4. **中断恢复**: 翻译过程中按Ctrl+C可保存进度并退出
5. **文件大小**: 建议处理前先缩减段落数量以提高翻译效率

## 环境变量

可以设置环境变量来避免在命令行中暴露API密钥：

```bash
export DEEPSEEK_API_KEY="your_api_key_here"
```

然后在命令行中使用占位符：
```bash
python translate_md_to_epub.py book.md output.epub <API_KEY> en
```

## 许可证

本项目仅供学习和个人使用。

---

## 多语言版本

- [English Version](README.md)
- [Version Française](README_FR.md) 