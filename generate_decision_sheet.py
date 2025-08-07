"""
Generate an editable PDF decision balance sheet.

This script constructs a self‑contained PDF form based on the design of a
decision balance sheet.  It uses the ReportLab toolkit to draw text and
interactive form fields, and Pillow via ReportLab's image support to embed
a logo at the top of the page.

To run this script you must have the `reportlab` and `Pillow` packages
installed.  Install them using pip if necessary:

    pip install reportlab Pillow

Running the script will create a file named ``DecisionBalanceSheet_Editable.pdf``
in the current working directory.

"""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from reportlab.lib.utils import simpleSplit


def generate_pdf(output_path: str = "DecisionBalanceSheet_Editable.pdf", logo_path: str = "logo.png") -> None:
    """Generate the editable decision balance sheet PDF.

    Args:
        output_path: Destination PDF filename.
        logo_path:   Path to the PNG image used at the top of the page.
    """
    # Create a canvas for the PDF.
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter

    # Margins and layout constants.
    left_margin = 0.75 * inch
    right_margin = 0.75 * inch
    content_width = width - left_margin - right_margin

    # Draw the logo centred at the top.
    try:
        logo = ImageReader(logo_path)
        logo_width = 2.0 * inch
        logo_height = 1.5 * inch
        logo_x = (width - logo_width) / 2.0
        logo_y = height - logo_height - 0.5 * inch
        c.drawImage(logo, logo_x, logo_y, width=logo_width, height=logo_height, preserveAspectRatio=True, mask='auto')
    except Exception:
        # If the image cannot be loaded, skip drawing it.
        pass

    # Title below the logo.
    title_y = height - 2.3 * inch
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(width / 2.0, title_y, "Decision Balance Sheet")

    # Body text paragraphs.
    body_font = "Helvetica"
    body_size = 10
    c.setFont(body_font, body_size)
    paragraphs = [
        "This worksheet can be used to help you make a decision on whether you want to make certain changes in your life (e.g. stopping some old behaviours or doing something new).",
        "It is best to complete each section, even if it seems that some of the answers in different sections are similar. Make sure you include both short-term and long-term advantages and disadvantages."
    ]
    # Starting position for the text.
    text_y = title_y - 0.4 * inch
    for para in paragraphs:
        lines = simpleSplit(para, body_font, body_size, content_width)
        for line in lines:
            c.drawString(left_margin, text_y, line)
            text_y -= 0.18 * inch
        # Extra space between paragraphs
        text_y -= 0.15 * inch

    # Field: Decision Topic
    field_spacing = 0.2 * inch
    c.setFont("Helvetica-Bold", 10)
    c.drawString(left_margin, text_y, "The Decision Topic")
    # Height to accommodate roughly two lines of text.
    decision_height = 0.5 * inch
    # y-coordinate for bottom of the text field rectangle.
    decision_field_y = text_y - 0.25 * inch - decision_height
    c.acroForm.textfield(
        name="DecisionTopic",
        x=left_margin,
        y=decision_field_y,
        width=content_width,
        height=decision_height,
        borderStyle='solid',
        borderColor=colors.black,
        fillColor=None,
        textColor=colors.black,
        forceBorder=True,
        multiline=True,
    )
    # Update cursor position below the decision field.
    current_y = decision_field_y - 0.4 * inch

    # Define the four quadrants for advantages/disadvantages.
    categories = [
        ("Advantages of Staying the Same", "AdvStay"),
        ("Disadvantages of Staying the Same", "DisadvStay"),
        ("Advantages of Changing", "AdvChange"),
        ("Disadvantages of Changing", "DisadvChange"),
    ]

    # Dimensions for each field in two columns.
    column_gap = 0.5 * inch
    col_width = (content_width - column_gap) / 2.0
    row_height = 1.3 * inch

    for row in range(2):
        for col in range(2):
            index = row * 2 + col
            label, field_name = categories[index]
            x_pos = left_margin + col * (col_width + column_gap)
            # Draw the label
            c.setFont("Helvetica-Bold", 10)
            c.drawString(x_pos, current_y, label)
            # Field rectangle directly beneath the label
            field_y = current_y - 0.25 * inch - row_height
            c.acroForm.textfield(
                name=field_name,
                x=x_pos,
                y=field_y,
                width=col_width,
                height=row_height,
                borderStyle='solid',
                borderColor=colors.black,
                fillColor=None,
                textColor=colors.black,
                forceBorder=True,
                multiline=True,
            )
        # After finishing a row, move down for the next row
        current_y = field_y - 0.6 * inch

    # Footer text near the bottom.
    c.setFont("Helvetica", 7)
    footer_y_1 = 0.6 * inch
    footer_y_2 = 0.45 * inch
    c.drawCentredString(width / 2.0, footer_y_1, "Based on the original by Practical Happiness - www.practicalhappiness.co.uk")
    c.drawCentredString(width / 2.0, footer_y_2, "Edited by Kasey Robinson from Hackeroos - www.hackeroos.com.au")

    # Finalize the page.
    c.showPage()
    c.save()


if __name__ == "__main__":
    generate_pdf()
