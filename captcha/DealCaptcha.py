from PIL import Image,ImageFilter
import subprocess
image = Image.open('../captcha.gif').convert('L')
image = image.point(lambda x : 0 if x < 45 else 255 )
width = image.size[0]
height = image.size[1]

image.save('../captcha_1.png')

subprocess.call(['tesseract','../captcha_1.png','../output'])

with open('../output.txt','r') as f:
    print f.read()
