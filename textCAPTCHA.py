from PIL import Image, ImageDraw
from singleCharacter import genSingleCharacter
import random


def randomLightColor():
    return random.randint(128, 255), random.randint(128, 255), random.randint(128, 255)


def genBackgroundImage(number):
    width = 32*number
    height = 32
    canvas = Image.new("RGB", (width, height), randomLightColor())
    draw = ImageDraw.Draw(canvas)
    for i in range(0, number*12):
        randomPointStart = (random.randint(0, width), random.randint(0, height))
        randomPointEnd = (random.randint(0, width), random.randint(0, height))
        draw.line([randomPointStart, randomPointEnd], randomLightColor())
    return canvas


def genTextImage(string):
    num = len(string)
    backgroundImage = genBackgroundImage(num)
    characterPosition = [(32*i+random.randint(0, 8), 0) for i in range(num)]
    for i in range(num):
        characterImage = genSingleCharacter(string[i])
        backgroundImage.paste(characterImage, characterPosition[i], characterImage)
    return backgroundImage


