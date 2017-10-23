# coding: utf8
from PIL import Image

im = Image.open("captcha.gif")
im.convert("P")

print im.histogram()
