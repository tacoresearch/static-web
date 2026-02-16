#!/usr/bin/env python3
"""
Markdown to HTML converter for static website generator
"""

import os
import sys
import markdown
from pathlib import Path

def convert_markdown_to_html(md_file_path, output_dir):
    """
    Convert a single Markdown file to HTML
    
    Args:
        md_file_path (str): Path to the Markdown file
        output_dir (str): Directory to output the HTML file
    
    Returns:
        str: Path to the generated HTML file
    """
    # Read the Markdown file
    with open(md_file_path, 'r', encoding='utf-8') as file:
        md_content = file.read()
    
    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content, extensions=['fenced_code', 'tables', 'toc'])
    
    # Generate output file path
    relative_path = os.path.relpath(md_file_path, 'content')
    html_filename = os.path.splitext(relative_path)[0] + '.html'
    html_file_path = os.path.join(output_dir, html_filename)
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(html_file_path), exist_ok=True)
    
    # Write HTML file
    with open(html_file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)
    
    return html_file_path

def convert_all_markdown(content_dir, output_dir):
    """
    Convert all Markdown files in content directory to HTML
    
    Args:
        content_dir (str): Directory containing Markdown files
        output_dir (str): Directory to output HTML files
    
    Returns:
        list: List of converted file paths
    """
    converted_files = []
    
    # Walk through content directory
    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if file.endswith('.md'):
                md_file_path = os.path.join(root, file)
                html_file_path = convert_markdown_to_html(md_file_path, output_dir)
                converted_files.append(html_file_path)
    
    return converted_files

if __name__ == "__main__":
    # Example usage
    if len(sys.argv) != 3:
        print("Usage: python markdown_to_html.py <content_dir> <output_dir>")
        sys.exit(1)
    
    content_dir = sys.argv[1]
    output_dir = sys.argv[2]
    
    converted_files = convert_all_markdown(content_dir, output_dir)
    
    print(f"Converted {len(converted_files)} files:")
    for file in converted_files:
        print(f"  {file}")