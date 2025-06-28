#!/usr/bin/env python3


from PIL import Image
import os

folder_path = "images/"
output_folder  = "output/"

def formatIMG(full_path, num):
  try:
    with Image.open(full_path) as im:
      im = im.rotate(num)
      im = im.resize((128,128))
      im = im.convert("RGB")
      base_name = os.path.splitext(os.path.basename(full_path))[0]
      output_path = os.path.join(output_folder, f"{base_name}.jpg")
      im.save(output_path,"JPEG")
  except:
    print("Error occured")


if __name__ == "__main__":
  if not os.path.exists(output_folder):
    os.mkdir(output_folder)
    print("No output folder found, new folder created.")
  
  
  for entry in os.listdir(folder_path):
    full_path = os.path.join(folder_path, entry)
    if os.path.isfile(full_path):
      formatIMG(full_path, 90)
