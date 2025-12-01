# Scripts

This directory contains utility scripts for the Eclipse Tractus-X documentation.

## Generate Kit Template PDF

The `generate_kit_pdf.py` script generates a single PDF document from all markdown files in the `docs-kits/kit-template` folder.

### Prerequisites

- Python 3.11 or higher
- System dependencies for WeasyPrint (on Ubuntu/Debian):

  ```bash
  sudo apt-get install libpango-1.0-0 libpangoft2-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
  ```

### Installation

Install Python dependencies:

```bash
pip install -r scripts/requirements.txt
```

### Usage

Run the script from the repository root:

```bash
python scripts/generate_kit_pdf.py
```

This will generate a `kit-template.pdf` file in the repository root.

### GitHub Workflow

The PDF is automatically generated via GitHub Actions when:

- Changes are pushed to the `main` branch that affect the kit-template folder
- A pull request modifies the kit-template folder
- The workflow is manually triggered

The generated PDF is uploaded as an artifact and can be downloaded from the workflow run page.

### Customization

To modify which files are included or the order they appear in the PDF, edit the `ordered_structure` list in the `collect_markdown_files()` function.

To adjust PDF styling, modify the CSS in the `create_pdf_styles()` function.
