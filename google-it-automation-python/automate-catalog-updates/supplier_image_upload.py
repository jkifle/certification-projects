#!/usr/bin/env python3

import os
import requests

input_path = "supplier-data/images/"
url = "http://localhost/upload/"

def uploadIMG(file):
  try:   
    with open(file, 'rb') as opened:
      r = requests.post(url, files={'file': opened})
      print("{} uploaded successfully".format(file))
  except:
    print("Error occured while uploading: {}".format(file))

def main():
  for entry in os.listdir(input_path):
    full_path = os.path.join(input_path, entry)
    root, ext = os.path.splitext(full_path)
              
    if ext == ".jpeg":
      uploadIMG(full_path)
      
if __name__ == "__main__":
  main()
