#!/usr/bin/env python3

import os
import datetime
import reports
import emails

def extractDescription(file):
  with open(file) as f:
    name = f"name: {f.readline()}"
    weight = f"weight: {f.readline()}"
  return f"{name}<br/>{weight}<br/><br/>"

def main():
  input_path = "supplier-data/descriptions/"
  
  report_path = "/tmp/processed.pdf"

  body = ""
  for file_path in os.listdir(input_path):
    body += extractDescription(os.path.join(input_path,file_path))

  today = datetime.datetime.today()
  title = f"Processed Update on {today.strftime('%B')} {today.day}, {today.year}"
  
  reports.generate_report(report_path, title, body)
 
  data = {
    "sender": "automation@example.com",
    "receiver": f"{os.environ.get('USER')}@example.com",
    "subject": "Upload Completed - Online Fruit Store",
    "body": "All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
    "attachment": report_path,
  }
  message = emails.generate_email(**data)
  emails.send_email(message)

if __name__ == "__main__":
  main()
