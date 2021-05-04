import jieba
import xlwt
import pandas as pd
from xlutils.copy import copy
book = xlwt.Workbook()
sheet1 = book.add_sheet('sheet1')
txt = open("D:/创新设计/yellow.txt", "r", encoding='utf-8').read()
words  = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
ji = 0
for word,count in items:
    sheet1.write(ji,0,word)
    sheet1.write(ji,1,count)
    ji += 1
book.save("D:/创新设计/wordrate(yellow).xlsx")
"""for i in range(15):
    word, count = items[i]
    print(type(word),type(count))"""
    #print ("{0:<10}{1:>5}".format(word, count))