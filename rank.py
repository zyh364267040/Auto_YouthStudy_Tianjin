# -*- coding: utf-8 -*-
# @Time    : 2023/3/23 22:31
# @Author  : 之落花--falling_flowers
# @File    : rank.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup
import time
import argparse


def main():
    parser = argparse.ArgumentParser(description='Required parameters')
    parser.add_argument('-c', '--cookie', type=str, required=True, help='cookie')
    parser.add_argument('-o', '--once', type=str, help='只获取一次排名(y/n)', default='n')
    parser.add_argument('-i', '--interval', type=int, help='刷新间隔(s)', default=1)
    args = parser.parse_args()
    header = {'Cookie': f'JSESSIONID={args.cookie}'}
    while True:
        with requests.get('http://admin.ddy.tjyun.com/zm/rank', headers=header, allow_redirects=False) as resp:
            if resp.status_code in (502, 504, 400, 302):
                print('rank error')
                break
            page = BeautifulSoup(resp.text, 'html.parser')
            span = page.find('span', class_='total')
            print('\r次数:', span.text, end='')
            time.sleep(abs(args.interval))
        if args.once == 'y':
            break


if __name__ == '__main__':
    main()
