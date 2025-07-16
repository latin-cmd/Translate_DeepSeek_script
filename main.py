#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Translation Toolkit Main Entry Point

Provides a unified command-line interface for all translation toolkit tools.
"""

import sys
import os
import argparse

# Add src to path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from text_processing.clean_md import clean_markdown
from text_processing.merge_paragraphs import merge_paragraphs
from text_processing.reduce_paragraphs import main as reduce_main
from translation.translate_md_to_epub import main as translate_main
from translation.decode_progress import decode_progress, list_progress_files

def clean_command(args):
    """Handle clean command"""
    clean_markdown(args.input, args.output)

def merge_command(args):
    """Handle merge command"""
    merge_paragraphs(args.input, args.output, args.min_length)

def reduce_command(args):
    """Handle reduce command"""
    sys.argv = ['reduce_paragraphs.py', args.input, str(args.count), args.output]
    reduce_main()

def translate_command(args):
    """Handle translate command"""
    sys.argv = ['translate_md_to_epub.py', args.input, args.output, args.api_key, args.lang]
    translate_main()

def decode_command(args):
    """Handle decode command"""
    if args.list:
        list_progress_files()
    else:
        decode_progress(args.progress_file, args.format)

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='Translation Toolkit - A toolkit for Markdown document translation and processing')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Clean command
    clean_parser = subparsers.add_parser('clean', help='Clean markdown files')
    clean_parser.add_argument('input', help='Input markdown file')
    clean_parser.add_argument('output', help='Output markdown file')
    clean_parser.set_defaults(func=clean_command)

    # Merge command
    merge_parser = subparsers.add_parser('merge', help='Merge short paragraphs')
    merge_parser.add_argument('input', help='Input markdown file')
    merge_parser.add_argument('output', help='Output markdown file')
    merge_parser.add_argument('--min-length', type=int, default=150, help='Minimum paragraph length (default: 150)')
    merge_parser.set_defaults(func=merge_command)

    # Reduce command
    reduce_parser = subparsers.add_parser('reduce', help='Reduce paragraph count')
    reduce_parser.add_argument('input', help='Input markdown file')
    reduce_parser.add_argument('count', type=int, help='Target paragraph count')
    reduce_parser.add_argument('output', help='Output markdown file')
    reduce_parser.set_defaults(func=reduce_command)

    # Translate command
    translate_parser = subparsers.add_parser('translate', help='Translate markdown to EPUB')
    translate_parser.add_argument('input', help='Input markdown file')
    translate_parser.add_argument('output', help='Output EPUB file')
    translate_parser.add_argument('api_key', help='DeepSeek API key')
    translate_parser.add_argument('lang', choices=['en', 'fr'], help='Source language (en or fr)')
    translate_parser.set_defaults(func=translate_command)

    # Decode command
    decode_parser = subparsers.add_parser('decode', help='Decode translation progress')
    decode_parser.add_argument('progress_file', nargs='?', help='Progress file to decode')
    decode_parser.add_argument('--format', choices=['md', 'txt'], default='md', help='Output format (default: md)')
    decode_parser.add_argument('--list', action='store_true', help='List all progress files')
    decode_parser.set_defaults(func=decode_command)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    args.func(args)

if __name__ == '__main__':
    main()