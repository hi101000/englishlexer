#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 12:09:52 2020

@author: ishan
"""

import json

while True:
    y=input("enter a word\n")
    if y=='.q' or y=='.Q':
        break
    z=y.split()
    with open('dict.json', 'r+') as f:
        dictionary=json.loads(f.read())
        for word in z:
            try:
                print("\n", dictionary[0][word])
            except:
                    print('that word is not in the dictionary\n')
                    dtype=input('what type of word is that, like a greeting or question or something like that:\n')
                    dictionary[0][word]=dtype
                    with open('dict.json', 'r+') as f:
                        x=[dictionary[0]]
                        json.dump(x, f)
                        dictionary.pop()