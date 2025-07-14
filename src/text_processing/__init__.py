"""
Text Processing Module

Contains utilities for cleaning, merging, and reducing paragraphs in Markdown documents.
"""

from .clean_md import clean_markdown
from .merge_paragraphs import merge_paragraphs
from .reduce_paragraphs import read_markdown_file, split_into_paragraphs, preserve_structure

__all__ = ['clean_markdown', 'merge_paragraphs', 'read_markdown_file', 'split_into_paragraphs', 'preserve_structure']