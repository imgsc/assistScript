# coding=utf-8

from PIL import Image

char_arr = list("#$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.")

im = Image.open("toux.jpg")

im = im.convert("RGBA")

txt = ""


def get_char(r, g, b, alpha):
    if alpha == 0:
        return " "
    gray = 0.2126 * r + 0.7152 * g + 0.0722 * b
    unit = (256.0 + 1) / len(char_arr)
    return char_arr[int(gray / unit)]


for i in range(im.height):
    for j in range(im.width):
        txt += get_char(*im.getpixel((j, i)))
    txt += "\n"
print(txt)