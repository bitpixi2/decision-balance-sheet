# Decision Balance Sheet

This repository contains a Python script and assets to generate an editable
PDF **Decision Balance Sheet**.  It reproduces the decision balance sheet
originally produced by **Practical Happiness** and edited by **Kasey
Robinson** of Hackeroos.  The resulting PDF includes a logo at the top,
a clear title, explanatory paragraphs, a wide multi‑line field for your
decision topic, and four large form fields for weighing the advantages
and disadvantages of staying the same versus making a change.

## Contents

- `generate_decision_sheet.py` – a Python script that uses
  [`reportlab`](https://pypi.org/project/reportlab/) to build the PDF and
  [`Pillow`](https://pypi.org/project/Pillow/) to embed the logo image.
  When run it produces `DecisionBalanceSheet_Editable.pdf` in the current
  directory.
- `logo.png` – the illustration used on the cover of the worksheet.
- `LICENSE` – the complete Creative Commons Attribution‑ShareAlike 4.0
  International license text under which this work is distributed.

## Usage

1. Install the dependencies (ReportLab and Pillow).  You can do this
   using pip:

   ```bash
   pip install reportlab Pillow
   ```

2. Run the script to generate the PDF:

   ```bash
   python generate_decision_sheet.py
   ```

   The script creates a file called `DecisionBalanceSheet_Editable.pdf` in
   the current directory.  Open it with a PDF viewer such as Adobe
   Acrobat, Preview or a modern web browser to fill in the form fields.

## Attribution

This worksheet is based on the original by [Practical Happiness]
(https://www.practicalhappiness.co.uk) and edited by Kasey
Robinson of [Hackeroos](https://www.hackeroos.com.au).  Please
retain this attribution if you modify or share the document.  For
license terms, see the `LICENSE` file.
