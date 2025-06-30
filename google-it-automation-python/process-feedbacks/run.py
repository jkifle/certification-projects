#! /usr/bin/env python3

import os
import requests

input_path = "/data/feedback/"

def createDict(file):
  feedback = {}
  feedback["title"] = file.readline()
  feedback["name"] = file.readline()
  feedback["date"] = file.readline()
  feedback["feedback"] = file.readline()
  return feedback
    

if __name__ == "__main__":
  for file in os.listdir(input_path):
    try:
      with open(os.path.join(input_path, file),"r") as f:
        requests.post("http://34.69.212.140/feedback/", data=createDict(f))
    except Exception as e:
      print(e)
