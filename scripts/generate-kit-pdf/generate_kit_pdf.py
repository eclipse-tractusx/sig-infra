#########################################################################################
# Copyright (c) 2025 Contributors to the Eclipse Foundation
#
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright ownership.
#
# This program and the accompanying materials are made available under the
# terms of the Apache License, Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# SPDX-License-Identifier: Apache-2.0
#########################################################################################


#!/usr/bin/env python3
"""
Generate a single PDF from the kit-template markdown files.
This script combines all markdown files from the kit-template folder
and converts them to a PDF document.
"""

import os
import sys
from pathlib import Path
import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

def collect_markdown_files(base_path):
    """
    Collect all markdown files from the kit-template directory in a logical order.
    """
    md_files = []
    
    # Define the order of files/folders to process
    ordered_structure = [
        'README.md',
        'adoption-view/adoption-view.md',
        'development-view/development-view.md',
        'development-view/architecture.md',
        'operations-view/operations-view.md',
        'documentation/sample-data.md',
        'industry-extensions/automotive/overview.md',
        'industry-extensions/shop-floor/overview.md',
        'success-stories/my-app.md',
        'changelog.md'
    ]
    
    for relative_path in ordered_structure:
        full_path = base_path / relative_path
        if full_path.exists():
            md_files.append(full_path)
    
    return md_files

def read_markdown_file(file_path):
    """Read markdown file content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""

def markdown_to_html(md_content, base_path):
    """Convert markdown content to HTML."""
    md = markdown.Markdown(extensions=[
        'extra',
        'codehilite',
        'toc',
        'tables',
        'fenced_code',
        'nl2br'
    ])
    return md.convert(md_content)

def create_pdf_styles():
    """Create CSS styles for the PDF."""
    return """
        @page {
            size: A4;
            margin: 2cm;
            @top-right {
                content: counter(page);
            }
        }
        
        body {
            font-family: 'DejaVu Sans', Arial, sans-serif;
            font-size: 11pt;
            line-height: 1.6;
            color: #333;
        }
        
        h1 {
            font-size: 24pt;
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
            margin-top: 30px;
            margin-bottom: 20px;
            page-break-before: always;
        }
        
        h1:first-of-type {
            page-break-before: avoid;
        }
        
        h2 {
            font-size: 18pt;
            color: #34495e;
            margin-top: 25px;
            margin-bottom: 15px;
        }
        
        h3 {
            font-size: 14pt;
            color: #7f8c8d;
            margin-top: 20px;
            margin-bottom: 10px;
        }
        
        h4, h5, h6 {
            font-size: 12pt;
            color: #95a5a6;
            margin-top: 15px;
            margin-bottom: 10px;
        }
        
        p {
            margin-bottom: 10px;
            text-align: justify;
        }
        
        code {
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 9pt;
        }
        
        pre {
            background-color: #f8f8f8;
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 10px;
            overflow-x: auto;
            margin: 15px 0;
            page-break-inside: avoid;
        }
        
        pre code {
            background-color: transparent;
            padding: 0;
            font-size: 9pt;
        }
        
        blockquote {
            border-left: 4px solid #3498db;
            padding-left: 15px;
            margin-left: 0;
            color: #7f8c8d;
            font-style: italic;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
            page-break-inside: avoid;
        }
        
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        
        th {
            background-color: #3498db;
            color: white;
            font-weight: bold;
        }
        
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        
        ul, ol {
            margin-bottom: 15px;
            padding-left: 30px;
        }
        
        li {
            margin-bottom: 5px;
        }
        
        a {
            color: #3498db;
            text-decoration: none;
        }
        
        img {
            max-width: 100%;
            height: auto;
            page-break-inside: avoid;
        }
        
        .section-divider {
            page-break-before: always;
        }
        
        .toc {
            page-break-after: always;
        }
    """

def generate_pdf(kit_template_path, output_path):
    """
    Generate a PDF from the kit-template markdown files.
    
    Args:
        kit_template_path: Path to the kit-template directory
        output_path: Path where the PDF should be saved
    """
    print("Starting PDF generation...")
    
    # Collect all markdown files
    md_files = collect_markdown_files(kit_template_path)
    print(f"Found {len(md_files)} markdown files to process")
    
    if not md_files:
        print("Error: No markdown files found!")
        sys.exit(1)
    
    # Combine all markdown content
    combined_content = []
    
    # Add title page
    combined_content.append("# Kit Template Documentation\n\n")
    combined_content.append("---\n\n")
    
    for md_file in md_files:
        print(f"Processing: {md_file.name}")
        content = read_markdown_file(md_file)
        
        if content:
            # Add section separator
            relative_path = md_file.relative_to(kit_template_path)
            combined_content.append(f'<div class="section-divider"></div>\n\n')
            combined_content.append(f"<!-- Source: {relative_path} -->\n\n")
            combined_content.append(content)
            combined_content.append("\n\n")
    
    # Convert combined markdown to HTML
    full_markdown = "".join(combined_content)
    html_content = markdown_to_html(full_markdown, kit_template_path)
    
    # Create complete HTML document
    html_doc = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Kit Template Documentation</title>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # Generate PDF
    print("Generating PDF...")
    font_config = FontConfiguration()
    css = CSS(string=create_pdf_styles(), font_config=font_config)
    
    html = HTML(string=html_doc, base_url=str(kit_template_path))
    html.write_pdf(output_path, stylesheets=[css], font_config=font_config)
    
    print(f"PDF generated successfully: {output_path}")
    print(f"File size: {os.path.getsize(output_path) / 1024:.2f} KB")

def main():
    """Main function."""
    # Get the repository root (assuming script is in scripts/ directory)
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    
    # Path to kit-template directory
    kit_template_path = repo_root / "docs-kits" / "kit-template"
    
    # Output path
    output_path = repo_root / "kit-template.pdf"
    
    # Check if kit-template directory exists
    if not kit_template_path.exists():
        print(f"Error: Kit template directory not found at {kit_template_path}")
        sys.exit(1)
    
    # Generate the PDF
    try:
        generate_pdf(kit_template_path, output_path)
    except Exception as e:
        print(f"Error generating PDF: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
