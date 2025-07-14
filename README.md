# Translation Toolkit (Translate Direct)

A Python toolkit for processing Markdown document translation, supporting document cleaning, paragraph processing, translation, and progress management.

## Features

- **Document Cleaning**: Clean up extra blank lines and special characters in Markdown files
- **Paragraph Processing**: Merge short paragraphs or reduce paragraph count
- **Smart Translation**: Use DeepSeek API for Chinese-English translation
- **Progress Management**: Support translation progress saving and recovery
- **Format Conversion**: Convert translated content to EPUB e-book format
- **Progress Decoding**: Extract translated content from progress files

## Project Structure

```
translation-toolkit/
├── src/
│   ├── text_processing/
│   │   ├── __init__.py
│   │   ├── clean_md.py           # Document cleaning tool
│   │   ├── merge_paragraphs.py   # Paragraph merging tool
│   │   └── reduce_paragraphs.py  # Paragraph reduction tool
│   ├── translation/
│   │   ├── __init__.py
│   │   ├── translate_md_to_epub.py  # Translation and EPUB conversion
│   │   └── decode_progress.py       # Progress decoding tool
│   └── __init__.py
├── docs/
│   ├── README_CN.md             # Chinese documentation
│   └── README_FR.md             # French documentation
├── main.py                      # Unified CLI entry point
├── setup.py                     # Package setup
├── requirements.txt             # Dependencies
└── README.md                    # This file
```

## Installation

### Method 1: Direct Installation
```bash
pip install -r requirements.txt
```

### Method 2: Development Installation
```bash
pip install -e .
```

## Usage

The toolkit provides both a unified command-line interface and individual script usage.

### Unified CLI (Recommended)

```bash
# Clean markdown files
python main.py clean input.md output.md

# Merge short paragraphs
python main.py merge input.md output.md --min-length 150

# Reduce paragraph count
python main.py reduce input.md 10 output.md

# Translate markdown to EPUB
python main.py translate input.md output.epub your_api_key en

# Decode translation progress
python main.py decode progress_file.json --format md
python main.py decode --list
```

### Individual Script Usage

#### 1. Document Cleaning
```bash
cd src/text_processing
python clean_md.py
```

#### 2. Paragraph Merging
```bash
cd src/text_processing
python merge_paragraphs.py
```

#### 3. Paragraph Reduction
```bash
cd src/text_processing
python reduce_paragraphs.py <input_file> [target_count] [output_file]
```

#### 4. Translation Tool
```bash
cd src/translation
python translate_md_to_epub.py <input.md> <output.epub> <api_key> <source_lang>
```

#### 5. Progress Decoding
```bash
cd src/translation
python decode_progress.py <progress_file> [output_format]
```

## Tool Descriptions

### 1. Document Cleaning (`clean_md.py`)
Cleans formatting issues in Markdown files:
- Remove consecutive blank lines
- Clean leading and trailing whitespace
- Remove special control characters
- Normalize spaces
- Ensure single blank line between paragraphs

### 2. Paragraph Merging (`merge_paragraphs.py`)
Merges short paragraphs to reduce paragraph count:
- Configurable minimum paragraph length threshold
- Intelligent paragraph combination
- Maintains document structure

### 3. Paragraph Reduction (`reduce_paragraphs.py`)
Intelligently reduces paragraph count while maintaining document structure:
- Preserves title and list structure
- Intelligently merges regular paragraphs
- Supports custom target paragraph count

### 4. Translation Tool (`translate_md_to_epub.py`)
Translates Markdown files using DeepSeek API and converts to EPUB:
- Supports progress saving and recovery
- Resume translation after interruption
- Auto-generates progress files
- Supports English and French translation

### 5. Progress Decoding (`decode_progress.py`)
Extracts translated content from translation progress files:
- Displays translation progress statistics
- Extracts translated content
- Supports Markdown and TXT format output
- Lists all progress files

## Recommended Workflow

1. **Document Preprocessing**:
   ```bash
   python main.py clean book.md book_clean.md
   python main.py merge book_clean.md book_merged.md
   python main.py reduce book_merged.md 50 book_reduced.md  # Optional
   ```

2. **Translation Processing**:
   ```bash
   python main.py translate book_merged.md book_translated.epub your_api_key en
   ```

3. **Progress Viewing**:
   ```bash
   python main.py decode --list
   python main.py decode book_merged_progress.json
   ```

## Environment Variables

You can set environment variables to avoid exposing API keys in command line:

```bash
export DEEPSEEK_API_KEY="your_api_key_here"
```

## Dependencies

- `requests`: For API communication
- `markdown`: For Markdown processing
- `ebooklib`: For EPUB generation

## Important Notes

1. **API Key**: Requires valid DeepSeek API key
2. **File Encoding**: All files use UTF-8 encoding
3. **Progress Files**: Translation process automatically generates `*_progress.json` files
4. **Interrupt Recovery**: Press Ctrl+C during translation to save progress and exit
5. **File Size**: Recommend reducing paragraph count before processing to improve translation efficiency

## Development

To contribute to this project:

1. Clone the repository
2. Install in development mode: `pip install -e .`
3. Make your changes
4. Test with the unified CLI: `python main.py --help`

## License

This project is for learning and personal use only.

---

## Multilingual Documentation

- [中文版本](docs/README_CN.md)
- [Version Française](docs/README_FR.md) 