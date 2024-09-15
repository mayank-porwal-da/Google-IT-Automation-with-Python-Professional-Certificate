#!/usr/bin/env python3
"""
This script generates a PDF report based on the provided data.
"""

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attachment, title, paragraph):
    report = SimpleDocTemplate(attachment)
    styles = getSampleStyleSheet()
    content = []
    report_title = Paragraph(title, styles["h1"])
    empty_line = Spacer(1,20)
    content.append(report_title)
    content.append(empty_line)
    para_count = 0
    for para in paragraph:
        content.append(Paragraph(para[0], styles["Normal"]))
        para_count += 1
        if para_count % 2 == 0:
            content.append(Spacer(1, 12))
    report.build(content)