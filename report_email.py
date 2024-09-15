#!/usr/bin/env python3

import os
import datetime
import reports
import emails

def process_data(data):
    """
    Process the data and to pass in generate-report  function for PDF report.
    """
    with open(data, "r") as file:
        lines = file.read()
        lines = lines.split("\n")
        name = lines[0]
        weight = lines[1]
        paragraph = [["name: {}".format(name)], ["weight: {}".format(weight)]]

    return paragraph

if __name__ == "__main__":
    paragraph = []
    path = os.path.expanduser("generate_fruit_report\description")
    # path = os.path.expanduser("~/supplier-data/descriptions/")
    for file in os.listdir(path):
        paragraph.extend(process_data(os.path.join(path, file)))

    title = "Processed Update on {}".format(datetime.date.today().strftime("%B %d, %Y"))
    reports.generate_report("processed.pdf", title, paragraph)

    message = emails.generate_email("sample.email@gmail.com","student.automation@inverv.com",
                          "Upload Completed - Online Fruit Store",
                          "All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
                          "processed.pdf")
                        #   "/tmp/processed.pdf")
    sends = emails.send_email(message)
    # reports.generate_report("/tmp/processed.pdf", title, paragraph)