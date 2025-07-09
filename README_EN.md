# Translation Toolkit (Translate Direct)

A Python toolkit for processing Markdown document translation, supporting document cleaning, paragraph processing, translation, and progress management.

## Features

- **Document Cleaning**: Clean up extra blank lines and special characters in Markdown files
- **Paragraph Processing**: Merge short paragraphs or reduce paragraph count
- **Smart Translation**: Use DeepSeek API for Chinese-English translation
- **Progress Management**: Support translation progress saving and recovery
- **Format Conversion**: Convert translated content to EPUB e-book format
- **Progress Decoding**: Extract translated content from progress files

## Installation

```bash
pip install -r requirements.txt
```

## Tool Descriptions

### 1. Document Cleaning (clean_md.py)

Clean formatting issues in Markdown files:

```bash
python clean_md.py
```

Features:
- Remove consecutive blank lines
- Clean leading and trailing whitespace
- Remove special control characters
- Normalize spaces
- Ensure single blank line between paragraphs

### 2. Paragraph Merging (merge_paragraphs.py)

Merge short paragraphs to reduce paragraph count:

```bash
python merge_paragraphs.py
```

Parameters:
- `min_length`: Minimum paragraph length threshold (default 150 characters)

### 3. Paragraph Reduction (reduce_paragraphs.py)

Intelligently reduce paragraph count while maintaining document structure:

```bash
python reduce_paragraphs.py <input_file> [target_count] [output_file]
```

Example:
```bash
python reduce_paragraphs.py book_merged.md 10 book_reduced.md
```

Features:
- Preserve title and list structure
- Intelligently merge regular paragraphs
- Support custom target paragraph count

### 4. Translation Tool (translate_md_to_epub.py)

Translate Markdown files using DeepSeek API and convert to EPUB:

```bash
python translate_md_to_epub.py <input.md> <output.epub> <api_key> <source_lang>
```

Parameters:
- `input.md`: Input Markdown file
- `output.epub`: Output EPUB file
- `api_key`: DeepSeek API key
- `source_lang`: Source language (en/fr)

Example:
```bash
python translate_md_to_epub.py book.md book_translated.epub your_api_key en
```

Features:
- Support progress saving and recovery
- Resume translation after interruption
- Auto-generate progress files
- Support English and French translation

### 5. Progress Decoding (decode_progress.py)

Extract translated content from translation progress files:

```bash
python decode_progress.py <progress_file> [output_format]
```

Example:
```bash
python decode_progress.py book_progress.json md
python decode_progress.py book_progress.json txt
```

Features:
- Display translation progress statistics
- Extract translated content
- Support Markdown and TXT format output
- List all progress files

## Workflow

1. **Document Preprocessing**:
   ```bash
   python clean_md.py          # Clean original document
   python merge_paragraphs.py  # Merge short paragraphs
   python reduce_paragraphs.py # Reduce paragraph count (optional)
   ```

2. **Translation Processing**:
   ```bash
   python translate_md_to_epub.py book_merged.md book_translated.epub your_api_key en
   ```

3. **Progress Viewing**:
   ```bash
   python decode_progress.py book_merged_progress.json
   ```

## File Descriptions

- `clean_md.py`: Document cleaning tool
- `merge_paragraphs.py`: Paragraph merging tool
- `reduce_paragraphs.py`: Paragraph reduction tool
- `translate_md_to_epub.py`: Translation and EPUB conversion tool
- `decode_progress.py`: Progress decoding tool
- `requirements.txt`: Python dependencies

## Important Notes

1. **API Key**: Requires valid DeepSeek API key
2. **File Encoding**: All files use UTF-8 encoding
3. **Progress Files**: Translation process automatically generates `*_progress.json` files
4. **Interrupt Recovery**: Press Ctrl+C during translation to save progress and exit
5. **File Size**: Recommend reducing paragraph count before processing to improve translation efficiency

## Environment Variables

You can set environment variables to avoid exposing API keys in command line:

```bash
export DEEPSEEK_API_KEY="your_api_key_here"
```

Then use placeholder in command line:
```bash
python translate_md_to_epub.py book.md output.epub <API_KEY> en
```

## License

This project is for learning and personal use only.

---

## Multilingual Versions

- [中文版本](README.md)
- [Version Française](README_FR.md) 