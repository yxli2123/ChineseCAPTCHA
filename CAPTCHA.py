import os
import random
from PIL import Image
import numpy as np
from singleCharacter import genSingleCharacter


def randomBackgroundImage():
    imageDirectory = './backgroundImage/'
    imageFiles = os.listdir(imageDirectory)
    image = Image.open(os.path.join(imageDirectory, random.choice(imageFiles)))
    image = image.resize((200, 200))
    return image


def randomPosition(number, size):
    x = np.arange(size//2, 200 - size)
    y = np.arange(size//2, 200 - size)
    position = np.zeros((number, 4), dtype='int')
    for i in range(number):
        pos_x = random.choice(x)
        pos_y = random.choice(y)
        position[i] = np.array([[pos_x, pos_y, pos_x + size, pos_y + size]])
        x = np.concatenate((x[x <= pos_x], x[x >= pos_x + size]))
        y = np.concatenate((y[y <= pos_y], y[y >= pos_y + size]))
    return position


def genImage(string):
    num = len(string)
    backgroundImage = randomBackgroundImage()
    characterPosition = randomPosition(num, 32)
    for i in range(num):
        characterImage = genSingleCharacter(string[i])
        backgroundImage.paste(characterImage, characterPosition[i], characterImage)
    return backgroundImage, characterPosition


