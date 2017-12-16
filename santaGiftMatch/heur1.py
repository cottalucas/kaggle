#!/usr/bin/env python

import csv

F_DIR = './01_Input/'

wishlist = []
goodkids = []

wish_dics = []
good_dics = []

child_in_gift = [False for x in range(1000000)]


def calc_gain(child_id, gift_id):
  '''
    Returns the total gain when the gift [gift_id] is assigned to the
    child [child_id].
    i.e.: The sum of the childhappiness and gifthappiness.
  '''
  gifthappiness = -1
  childhappiness = -1
  
  if gift_id in wishlist[child_id]:
    childhappiness = wish_dics[child_id][gift_id]
  
  if child_id in goodkids[gift_id]:
    gifthappiness = good_dics[gift_id][child_id]
  
  return (childhappiness + gifthappiness)




with open(F_DIR + 'child_wishlist.csv', newline='') as fwish:
  fwish_reader = csv.reader(fwish, delimiter=',')
  for row in fwish_reader:
    row = [int(x) for x in row[1:]]
    wishlist.append(row)

    cur_dic = {}
    l = len(row)
    w = len(row)
    for elem in row:
      elem = int(elem)
      cur_dic[elem] = float(2*w)/l
      w -= 1
    wish_dics.append(cur_dic)



with open(F_DIR + 'gift_goodkids.csv', newline='') as fgood:
  fgood_reader = csv.reader(fgood, delimiter=',')
  for row in fgood_reader:
    row = [int(x) for x in row[1:]]
    goodkids.append(row)

    cur_dic = {}
    l = len(row)
    w = len(row)
    for elem in row:
      elem = int(elem)
      cur_dic[elem] = float(2*w)/l
      child_in_gift[elem] = True
      w -= 1
    good_dics.append(cur_dic)




# List of pairs (child, gift)
resp = []


# Optimize twins
for i in range(0, 3999, 2):
  gifts = wishlist[i] + wishlist[i+1]
  best_gift_id = wishlist[i][0]
  best_gift_w = float(-2)
  for g in gifts:
    gain = calc_gain(i, g) + calc_gain(i+1, g)
    if gain > best_gift_w:
      best_gift_w = gain
      best_gift_id = g
  resp.append((i,   best_gift_id))
  resp.append((i+1, best_gift_id))



# Optimize non-twins
for i in range(4000, len(wishlist)):
  if child_in_gift[i] == False:
    # The kid gets his most wanted gift...
    resp.append((i, wishlist[i][0]))
  else:
    best_gift_id = wishlist[i][0]
    best_gift_w = float(-2)
    for gift_id in wishlist[i]:
      gain = calc_gain(i, gift_id)
      if gain > best_gift_w:
        best_gift_w = gain
        best_gift_id = gift_id
    # TODO: Check each gift not in the wishlist, but has child i in
    #       its goodkids.
    resp.append((i, best_gift_id))


fout = open('out', 'w')
fout.write('ChildId,GiftId')
for (child_id, gift_id) in resp:
  fout.write(str(child_id) + ',' + str(gift_id) + '\n')
fout.close()
