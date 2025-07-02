#!/usr/bin/env python3

from PIL import Image
import os

input_path = "supplier-data/images/"

def formatIMG(full_path):
  try:
    with Image.open(full_path) as im:
      im = im.resize((600,400))
      im = im.convert("RGB")
      base_name = os.path.splitext(os.path.basename(full_path))[0]
      output_path = os.path.join(input_path, f"{base_name}.jpeg")
      im.save(output_path,"JPEG")
  except:
    print("Error occured")

def main():
  for entry in os.listdir(input_path):
    full_path = os.path.join(input_path, entry)
    if os.path.isfile(full_path):
      formatIMG(full_path)


if __name__ == "__main__":
  main()
