import random
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Function to create the cover page with random title and subtitle
def create_cover(canvas, doc, title_alignment='center', subtitle_alignment='center'):
    title = f"Report Title - {random.randint(1000, 9999)}"
    subtitle = f"Subtitle - {random.choice(['Analysis', 'Summary', 'Findings'])}"

    canvas.saveState()

    if title_alignment == 'center':
        canvas.setFont('Helvetica-Bold', 24)
        canvas.drawCentredString(300, 500, title)
    elif title_alignment == 'left':
        canvas.setFont('Helvetica-Bold', 24)
        canvas.drawString(100, 500, title)
    elif title_alignment == 'right':
        canvas.setFont('Helvetica-Bold', 24)
        canvas.drawRightString(500, 500, title)

    if subtitle_alignment == 'center':
        canvas.setFont('Helvetica', 18)
        canvas.drawCentredString(300, 450, subtitle)
    elif subtitle_alignment == 'left':
        canvas.setFont('Helvetica', 18)
        canvas.drawString(100, 450, subtitle)
    elif subtitle_alignment == 'right':
        canvas.setFont('Helvetica', 18)
        canvas.drawRightString(500, 450, subtitle)

    canvas.restoreState()

# Output folder
output_folder = "output"

# Create the PDF document in the output folder
output_path = f"{output_folder}/cover_page_random_title.pdf"
doc = SimpleDocTemplate(output_path, pagesize=letter)

# Set the desired alignment (center, left, right)
title_alignment = 'center'
subtitle_alignment = 'right'

# Add cover page
doc.build([Paragraph("Cover Page", getSampleStyleSheet()['Title'])], onFirstPage=lambda c, d: create_cover(c, d, title_alignment, subtitle_alignment))

print(f"Cover page with random title and alignment generated at: {output_path}")
