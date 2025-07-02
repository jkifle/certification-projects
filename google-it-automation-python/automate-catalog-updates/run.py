#! /usr/bin/env python3

import os
import requests
import re

input_path = "supplier-data/descriptions/"
url = "http://34.53.44.114/fruits/"

def createDict(file, image_name):
  feedback = {}
  feedback["name"] = file.readline()
  feedback["weight"] = re.findall(r'\d+',file.readline())
  feedback["description"] = file.readline()
  feedback["image_name"] = image_name
  return feedback

if __name__ == "__main__":
  for file in os.listdir(input_path):
    try: 
      with open(os.path.join(input_path, file), "r") as f:
        imageid = os.path.splitext(os.path.basename(file))[0]
        image_name = f"{imageid}.jpeg"
        requests.post(url, data=createDict(f, image_name))
    except Exception as e: 
      print(e)
