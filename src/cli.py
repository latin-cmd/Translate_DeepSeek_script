#!/usr/bin/env python3
"""
Translation Toolkit Command Line Interface
"""

import argparse
import sys
from pathlib import Path

# Import modules from the package
from cleaners.markdown_cleaner import main as clean_main
from processors.merge_paragraphs import main as merge_main
from processors.reduce_paragraphs import main as reduce_main
from converters.epub_translator import main as translate_main
from utils.progress_decoder import main as decode_main


def main():
    """Main entry point for the translation toolkit CLI."""
    parser = argparse.ArgumentParser(
        description="Translation Toolkit - A comprehensive toolkit for Markdown translation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  translation-toolkit clean input.md output.md
  translation-toolkit merge input.md output.md
  translation-toolkit reduce input.md output.md --max-paragraphs 50
  translation-toolkit translate input.md output.epub --api-key YOUR_KEY
  translation-toolkit decode progress_file.progress
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Clean command
    clean_parser = subparsers.add_parser('clean', help='Clean Markdown files')
    clean_parser.add_argument('input', help='Input Markdown file')
    clean_parser.add_argument('output', help='Output Markdown file')
    
    # Merge command
    merge_parser = subparsers.add_parser('merge', help='Merge short paragraphs')
    merge_parser.add_argument('input', help='Input Markdown file')
    merge_parser.add_argument('output', help='Output Markdown file')
    
    # Reduce command
    reduce_parser = subparsers.add_parser('reduce', help='Reduce paragraph count')
    reduce_parser.add_argument('input', help='Input Markdown file')
    reduce_parser.add_argument('output', help='Output Markdown file')
    reduce_parser.add_argument('--max-paragraphs', type=int, default=100,
                              help='Maximum number of paragraphs (default: 100)')
    
    # Translate command
    translate_parser = subparsers.add_parser('translate', 
                                           help='Translate Markdown to EPUB')
    translate_parser.add_argument('input', help='Input Markdown file')
    translate_parser.add_argument('output', help='Output EPUB file')
    translate_parser.add_argument('--api-key', required=True,
                                help='DeepSeek API key')
    translate_parser.add_argument('--base-url', 
                                default='https://api.deepseek.com',
                                help='API base URL')
    
    # Decode command
    decode_parser = subparsers.add_parser('decode', 
                                        help='Decode progress files')
    decode_parser.add_argument('progress_file', help='Progress file to decode')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    # Route to appropriate function based on command
    if args.command == 'clean':
        sys.argv = ['clean', args.input, args.output]
        clean_main()
    elif args.command == 'merge':
        sys.argv = ['merge', args.input, args.output]
        merge_main()
    elif args.command == 'reduce':
        sys.argv = ['reduce', args.input, args.output, 
                   '--max-paragraphs', str(args.max_paragraphs)]
        reduce_main()
    elif args.command == 'translate':
        sys.argv = ['translate', args.input, args.output,
                   '--api-key', args.api_key,
                   '--base-url', args.base_url]
        translate_main()
    elif args.command == 'decode':
        sys.argv = ['decode', args.progress_file]
        decode_main()


if __name__ == '__main__':
    main()