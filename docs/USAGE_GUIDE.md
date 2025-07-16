# Translation Toolkit Usage Guide

This guide provides detailed instructions for using the Translation Toolkit effectively.

## Quick Start

1. **Installation**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Basic workflow**:
   ```bash
   # Clean your markdown file
   python main.py clean book.md book_clean.md
   
   # Merge short paragraphs
   python main.py merge book_clean.md book_merged.md
   
   # Translate to EPUB
   python main.py translate book_merged.md book_translated.epub YOUR_API_KEY en
   ```

## Command Reference

### Clean Command
```bash
python main.py clean <input_file> <output_file>
```
- Removes extra blank lines
- Cleans special characters
- Normalizes formatting

### Merge Command
```bash
python main.py merge <input_file> <output_file> [--min-length LENGTH]
```
- `--min-length`: Minimum paragraph length (default: 150)
- Combines short paragraphs for better translation

### Reduce Command
```bash
python main.py reduce <input_file> <target_count> <output_file>
```
- Intelligently reduces paragraph count
- Preserves document structure

### Translate Command
```bash
python main.py translate <input_file> <output_file> <api_key> <language>
```
- `language`: Source language (en or fr)
- Supports progress saving and recovery
- Creates EPUB output

### Decode Command
```bash
python main.py decode <progress_file> [--format FORMAT]
python main.py decode --list
```
- `--format`: Output format (md or txt)
- `--list`: List all progress files

## Best Practices

### 1. Document Preparation
- Always clean your document first
- Merge short paragraphs for better translation quality
- Consider reducing paragraph count for large documents

### 2. Translation Tips
- Use environment variables for API keys
- Monitor progress files for recovery
- Press Ctrl+C to safely interrupt translation

### 3. File Organization
- Keep original files separate from processed files
- Use descriptive filenames (e.g., `book_clean.md`, `book_merged.md`)

## Troubleshooting

### Common Issues

1. **Import errors**: Run from project root directory
2. **API errors**: Check your DeepSeek API key
3. **File encoding**: Ensure UTF-8 encoding

### Getting Help
```bash
python main.py --help
python main.py <command> --help
```

## Examples

### Complete Translation Workflow
```bash
# Step 1: Clean
python main.py clean original.md clean.md

# Step 2: Merge paragraphs
python main.py merge clean.md merged.md --min-length 100

# Step 3: Reduce if needed
python main.py reduce merged.md 30 reduced.md

# Step 4: Translate
python main.py translate reduced.md translated.epub YOUR_API_KEY en

# Step 5: Check progress
python main.py decode --list
```

### Resume Interrupted Translation
```bash
# If translation was interrupted, just run the same command
python main.py translate reduced.md translated.epub YOUR_API_KEY en
# The system will detect existing progress and ask if you want to continue
```

### Extract Translated Content
```bash
# Extract as Markdown
python main.py decode reduced_progress.json --format md

# Extract as plain text
python main.py decode reduced_progress.json --format txt
```