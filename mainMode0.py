import random
from CAPTCHA import genImage
from textCAPTCHA import genTextImage
import pandas as pd

if __name__ == '__main__':
    mode = 0
    fp = open("./ChineseCharacterTable.txt", "r")
    ChineseString = fp.read()
    fp.close()

    if mode == 0:
        head = ['string', 'left0', 'top0', 'right0', 'bottom0',
                'left1', 'top1', 'right1', 'bottom1',
                'left2', 'top2', 'right2', 'bottom2',
                'left3', 'top3', 'right3', 'bottom3']
        posTable = pd.DataFrame(columns=head)
        for i in range(10):
            string = random.sample(ChineseString, 4)
            string = "".join(string)
            image, position = genImage(string)
            position = list(position.flatten())
            posTable.loc[i] = [string] + position
            image.save('./image/{:0>5d}.png'.format(i))
            if i % 100 == 0:
                print("Image CAPTCHA has finished {:0>5d}".format(i))
        posTable.to_csv('./pos.csv')

    if mode == 1:
        fp = open("./textImageLabel.txt", "w")
        for i in range(10):
            string = random.sample(ChineseString, 4)
            string = "".join(string)
            fp.write(string+'\n')
            image = genTextImage(string)
            image.save('./textImage/{:0>5d}.png'.format(i))
            if i % 100 == 0:
                print("Text CAPTCHA generator has finished {:0>5d}".format(i))
