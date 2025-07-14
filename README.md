# Translation Toolkit

A comprehensive Python toolkit for processing and translating Markdown documents.

## 📁 Project Structure

```
translation-toolkit/
├── src/                    # Source code
│   ├── cleaners/          # Document cleaning modules
│   ├── processors/        # Text processing modules
│   ├── translators/       # Translation modules
│   ├── converters/        # Format conversion modules
│   └── utils/             # Utility functions
├── docs/                  # Documentation
│   ├── README.md          # English documentation
│   ├── README_CN.md       # Chinese documentation
│   └── README_FR.md       # French documentation
├── tests/                 # Unit tests
├── examples/              # Usage examples
├── requirements.txt       # Python dependencies
└── setup.py              # Installation script
```

## 🚀 Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Install the package:
```bash
pip install -e .
```

3. Use the command-line tools:
```bash
# Clean markdown files
translation-toolkit clean input.md output.md

# Merge paragraphs
translation-toolkit merge input.md output.md

# Reduce paragraphs
translation-toolkit reduce input.md output.md --max-paragraphs 50

# Translate and convert to EPUB
translation-toolkit translate input.md output.epub --api-key YOUR_API_KEY
```

## 📖 Documentation

- [English Documentation](docs/README.md)
- [中文文档](docs/README_CN.md)
- [Documentation Française](docs/README_FR.md)

## 📄 License

MIT License