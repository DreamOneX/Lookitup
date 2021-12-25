#!/usr/bin/env python
import sys
import requests
import re
from bs4 import BeautifulSoup

def global_color_var() -> None:
    '''
    set global color variable
    cb+fg+white+cm+bg+black+ce
    '''
    global fg, bg, black, red, green, yellow, blue, purple, cyan, white, cb, ce, cm
    fg = '3'
    bg = '4'
    black = '0'
    red = '1'
    green = '2'
    yellow = '3'
    blue = '4'
    purple = '5'
    cyan = '6'
    white = '7'
    cb = '\033['
    ce = 'm'
    cm = ';'

def main(argv):
    global_color_var()
    tmp = []
    for i in argv:
        try:
            for g in BeautifulSoup(requests.get('https://dict.youdao.com/search?q={}'.format(i)).text, 'html.parser').findAll('div', class_='trans-container')[0].ul.findAll('li'):
                pos = cb + fg + blue + ce + re.search(r'[a-z]+\.',g.text).group()
                paraphrases = re.split(r"[；]", re.sub(r"[a-z]+\. +", '', g.text))
                for h in range(len(paraphrases)):
                    paraphrases[h] = cb + fg + yellow + ce + paraphrases[h]

                print(pos + ' ' + (cb + fg + red + ce + '；').join(paraphrases))
        except IndexError:
            print('Not Found')
    return tmp

if __name__ == '__main__':
    args = sys.argv
    del args[0]
    main(args)
# re.search(r"[a-z]+\.", main(["one"])[0])
# re.sub(r"[a-z]+\. +", '', main(["run"])[0])
# re.split(r"[；]", main(["run"])[0])
# '；'.join(re.split(r"[；]", main(["run"])[0]))
