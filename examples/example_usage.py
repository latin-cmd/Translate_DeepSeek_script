#!/usr/bin/env python3
"""
Example usage of the Translation Toolkit modules
"""

import sys
sys.path.append('..')

from src.cleaners.markdown_cleaner import clean_markdown
from src.processors.merge_paragraphs import merge_paragraphs
from src.processors.reduce_paragraphs import main as reduce_main
from src.utils.progress_decoder import decode_progress

def demo_cleaning():
    """Demonstrate markdown cleaning."""
    print("=== Markdown Cleaning Demo ===")
    clean_markdown("sample.md", "sample_cleaned.md")
    print()

def demo_merging():
    """Demonstrate paragraph merging."""
    print("=== Paragraph Merging Demo ===")
    merge_paragraphs("sample_cleaned.md", "sample_merged.md", min_length=50)
    print()

def demo_reduction():
    """Demonstrate paragraph reduction."""
    print("=== Paragraph Reduction Demo ===")
    # Set up argv for reduce_main
    original_argv = sys.argv
    sys.argv = ['reduce_paragraphs.py', 'sample_merged.md', 'sample_reduced.md', '--max-paragraphs', '10']
    reduce_main()
    sys.argv = original_argv
    print()

if __name__ == "__main__":
    print("Translation Toolkit - Usage Examples\n")
    
    # Run demos
    demo_cleaning()
    demo_merging()
    demo_reduction()
    
    print("\nAll demos completed! Check the output files in the examples directory.")