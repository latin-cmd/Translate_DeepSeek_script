# Tests Directory

This directory is for unit tests and integration tests for the Translation Toolkit.

## Test Structure

```
tests/
├── test_cleaners/
│   └── test_markdown_cleaner.py
├── test_processors/
│   ├── test_merge_paragraphs.py
│   └── test_reduce_paragraphs.py
├── test_converters/
│   └── test_epub_translator.py
└── test_utils/
    └── test_progress_decoder.py
```

## Running Tests

To run all tests:
```bash
python -m pytest tests/
```

To run specific tests:
```bash
python -m pytest tests/test_cleaners/
```

## Writing Tests

Use pytest for writing tests. Example:

```python
import pytest
from src.cleaners.markdown_cleaner import clean_markdown

def test_clean_markdown():
    # Test implementation
    pass
```