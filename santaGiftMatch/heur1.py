#!/usr/bin/env python

import csv

F_DIR = './01_Input/'

wishlist = []
goodkids = []




with open(F_DIR + 'child_wishlist.csv', newline='') as fwish:
  fwish_reader = csv.reader(fwish, delimiter=',')
  for row in fwish_reader:
    wishlist.append(row)


with open(F_DIR + 'gift_goodkids.csv', newline='') as fgood:
  fgood_reader = csv.reader(fgood, delimiter=',')
  for row in fgood_reader:
    goodkids.append(row)


print(goodkids[0])
print(wishlist[0]) 


