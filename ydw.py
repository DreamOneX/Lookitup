#!/usr/bin/env python
import sys
import requests
import re
from bs4 import BeautifulSoup


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
    tmp = []
    for i in argv:
        print(cb + fg + red + ce + i)
        try:
            for g in BeautifulSoup(requests.get('https://dict.youdao.com/search?q={}'.format(i)).text, 'html.parser').findAll('div', class_='trans-container')[0].ul.findAll('li'):
                try:
                    pos = cb + fg + blue + ce + \
                        re.search(r'[a-z]+\.', g.text).group()
                    g_dpos = re.sub(r"[a-z]+\. +", '', g.text)
                except AttributeError:
                    pos = cb + fg + blue + ce + \
                        re.search(r'【.+?】', g.text).group()
                    g_dpos = re.sub(r'【.+?】', '', g.text)
                paraphrases = re.split(
                    r"[；]", re.sub(r"[a-z]+\. +", '', g_dpos))
                for h in range(len(paraphrases)):
                    paraphrases[h] = cb + fg + yellow + ce + paraphrases[h]
                    

                print(pos + ' ' + (cb + fg + red + ce + '；').join(paraphrases))
        except IndexError:
            print('Not Found')
        # except:
        #     print('An unbelievable error happened')
    return tmp


if __name__ == '__main__':
    args = sys.argv
    del args[0]
    main(args)
