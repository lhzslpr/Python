import os
import os.path
from PIL import Image

def ResizeImage(filein, fileout, width, height, type):
    img = Image.open(filein)
    out = img.resize((width, height),Image.ANTIALIAS)
    #resize image with high-quality
    out.save(fileout, type)
    print("success")
if __name__ == "__main__":
    filein = r'./in.png'
   
    width = input("input width: ")
    height = input("input height: ")
    type = 'png'

    fileout = r'./out.png'
    ResizeImage(filein, fileout, width, height, type)
