#! /usr/bin/env python3

import os
import requests
import re

input_path = "supplier-data/descriptions/"
url = "http://34.132.45.55/fruits/"

def createDict(file):
  feedback = {}
  feedback["name"] = file.readline()
  weight = re.findall(r'\d+',file.readline())
  feedback["description"] = file.readline()
  #feedback["image_name"] = file.readline()
  
  return feedback

if __name__ == "__main__":
  for file in os.listdir(input_path):
    try:
      with open(os.path.join(input_path, file), "r") as f:
        requests.post(url, data=createDict(f))
    except Exception as e:
      print(e)
