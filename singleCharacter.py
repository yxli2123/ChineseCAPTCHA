"""
This file generates a single Chinese character.
Defines a function whose input is a Chinese character e.g. '中' and output is an 32*32 PIL image.
    character size: 26
    character style: randomly chosen from font folder
    character angle: randomly chosen from -60º to 60º
    character color: dark (0:127, 0:127, 0:127)
    canvas size: 32x32
    canvas background color: white (255, 255, 255)
"""
import os
import random
from PIL import Image, ImageDraw, ImageFont


def randomColor():
    return random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)


def randomFont():
    fontDirectory = './font/'
    fontFiles = os.listdir(fontDirectory)
    font = ImageFont.truetype(os.path.join(fontDirectory, random.choice(fontFiles)), 26)
    return font


def randomAngle():
    return random.randint(-45, 45)


def genSingleCharacter(character):
    # create a white(255, 255, 255) square(32, 32) canvas
    canvas = Image.new('RGBA', (32, 32), (255, 255, 255, 0))

    # ready to draw a character on the canvas
    image = ImageDraw.Draw(canvas)
    image.text((3, 3), character, font=randomFont(), fill=randomColor())

    # rotate the canvas and character on it, fill the outside area with white color
    canvas = canvas.rotate(randomAngle(), fillcolor=(255, 255, 255, 0))
    return canvas

