# Translation Toolkit Project Structure

## Overview

This document describes the organized structure of the Translation Toolkit project after reorganization.

## Directory Structure

```
translation-toolkit/
├── .git/                           # Git repository
├── .gitignore                      # Git ignore file
├── README.md                       # Main project documentation
├── requirements.txt                # Python dependencies
├── setup.py                        # Package installation setup
├── main.py                         # Unified CLI entry point
├── src/                            # Source code directory
│   ├── __init__.py                 # Main package initialization
│   ├── text_processing/            # Text processing utilities
│   │   ├── __init__.py             # Package initialization
│   │   ├── clean_md.py             # Markdown cleaning tool
│   │   ├── merge_paragraphs.py     # Paragraph merging tool
│   │   └── reduce_paragraphs.py    # Paragraph reduction tool
│   └── translation/                # Translation utilities
│       ├── __init__.py             # Package initialization
│       ├── translate_md_to_epub.py # Main translation tool
│       └── decode_progress.py      # Progress decoding tool
└── docs/                           # Documentation directory
    ├── README_CN.md                # Chinese documentation
    ├── README_FR.md                # French documentation
    ├── USAGE_GUIDE.md              # Detailed usage guide
    └── PROJECT_STRUCTURE.md        # This file
```

## File Descriptions

### Root Level Files

- **README.md**: Main project documentation with installation and usage instructions
- **requirements.txt**: Python package dependencies (requests, markdown, ebooklib)
- **setup.py**: Package installation configuration for pip
- **main.py**: Unified command-line interface for all tools
- **.gitignore**: Git ignore patterns for Python and project-specific files

### Source Code (`src/`)

#### Text Processing Module (`src/text_processing/`)

- **clean_md.py**: 
  - Cleans Markdown files by removing extra blank lines
  - Removes special characters and normalizes formatting
  - Ensures consistent paragraph spacing

- **merge_paragraphs.py**:
  - Combines short paragraphs to improve translation quality
  - Configurable minimum paragraph length threshold
  - Maintains document structure while reducing fragment count

- **reduce_paragraphs.py**:
  - Intelligently reduces paragraph count to target number
  - Preserves titles, lists, and document structure
  - Smart merging algorithm for regular paragraphs

#### Translation Module (`src/translation/`)

- **translate_md_to_epub.py**:
  - Main translation tool using DeepSeek API
  - Supports English and French source languages
  - Progress saving and recovery functionality
  - EPUB output generation

- **decode_progress.py**:
  - Extracts translated content from progress files
  - Supports multiple output formats (Markdown, TXT)
  - Progress statistics and file listing

### Documentation (`docs/`)

- **README_CN.md**: Chinese version of project documentation
- **README_FR.md**: French version of project documentation
- **USAGE_GUIDE.md**: Comprehensive usage instructions and examples
- **PROJECT_STRUCTURE.md**: This file - detailed project structure overview

## Key Improvements

### 1. Modular Organization
- Separated text processing from translation functionality
- Clear package structure with proper `__init__.py` files
- Logical grouping of related tools

### 2. Unified Interface
- Single entry point (`main.py`) for all tools
- Consistent command-line interface
- Comprehensive help system

### 3. Better Documentation
- Organized documentation in dedicated directory
- Multiple language support
- Detailed usage guides and examples

### 4. Development Support
- Proper Python package structure
- Installation setup with `setup.py`
- Git ignore configuration for clean repository

### 5. Maintainability
- Clear separation of concerns
- Modular imports and exports
- Consistent coding standards

## Usage Patterns

### Individual Scripts
Each tool can still be run independently:
```bash
cd src/text_processing && python clean_md.py
cd src/translation && python translate_md_to_epub.py
```

### Unified CLI (Recommended)
All tools accessible through main interface:
```bash
python main.py clean input.md output.md
python main.py translate input.md output.epub api_key en
```

### Package Installation
Install as a Python package:
```bash
pip install -e .
```

## Benefits of This Structure

1. **Scalability**: Easy to add new tools and features
2. **Maintainability**: Clear organization makes code easier to maintain
3. **Usability**: Unified interface reduces learning curve
4. **Documentation**: Comprehensive guides for all use cases
5. **Professional**: Standard Python project structure