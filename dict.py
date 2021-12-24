#!/usr/bin/env python
import sys
import requests
from bs4 import BeautifulSoup


def main(argv):
    for i in argv:
        try:
            for g in BeautifulSoup(requests.get('https://dict.youdao.com/search?q={}'.format(i)).text, 'html.parser').findAll('div', class_='trans-container')[0].ul.findAll('li'):
                print(g.text)
        except IndexError:
            print('Not Found')

if __name__ == '__main__':
    args = sys.argv
    del args[0]
    main(args)
