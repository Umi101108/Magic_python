# coding: utf8
from PIL import Image
import argparse

ascii_char = list(u"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

IMG = 'ascii_dora.png'
WIDTH = 90
HEIGHT = 60

# 将256灰度映射到70个字符上
def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126*r + 0.7152*g + 0.0722*b)
    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]


if __name__ == '__main__':
    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
    
    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'
    print txt