#提取URL静态特征
import xlwt
import pandas as pd
from xlutils.copy import copy

def translate(a,b):
    f = pd.read_excel(a)
    book = xlwt.Workbook()
    sheet1 = book.add_sheet('sheet1')
    url_list = f['url']
    num_list = []
    call_list = []
    letter_list = []
    rate_list = []
    letter = 0
    digit = 0
    for i in url_list:
        num_list.append(len(i) - i.count('.'))
    ji = 1
    for data in num_list:
        sheet1.write(ji,1,data)
        ji += 1
    for i in url_list:
        call_list.append(i.count('.'))
    ji = 1
    for data in call_list:
        sheet1.write(ji,2,data)
        ji += 1
    for i in url_list:
        for s in i:
            if s.isalpha() or s.isdigit():
                letter += 1
        letter_list.append(len(i) - letter)
        letter = 0
    ji = 1
    for data in letter_list:
        sheet1.write(ji,3,data)
        ji += 1
    for i in url_list:
        for s in i:
            if s.isdigit():
                digit += 1
        a = digit/len(i)
        rate_list.append(a)
        digit = 0
    ji = 1
    for data in rate_list:
        sheet1.write(ji,4,data)
        ji += 1
    split_list1 = []
    num1 = []
    tongji1 = []
    digit2 = 0
    for i in url_list:
        split_list1.append(i.split('.'))
    for i in split_list1:
        for s in i:
            for x in s:
                if x.isdigit():
                    digit2 += 1
            num1.append(digit2)
            digit2 = 0
        tongji1.append(max(num1))
        num1 = []
    ji = 1
    for data in tongji1:
        sheet1.write(ji,5,data)
        ji += 1
    num2 = 0
    tongji2 = []
    for i in url_list:
        for x in range(len(i)-1):
            if (i[x].isdigit() and i[x+1].isalpha()) or (i[x].isalpha() and i[x+1].isdigit()):
                num2 += 1
        tongji2.append(num2/len(i))
        num2 = 0
    ji = 1
    for data in tongji2:
        sheet1.write(ji,6,data)
        ji += 1
    book.save(b)

if __name__ == 'main':
    translate('D:/white.xlsx','D:/vic(1).xlsx')#D:/white.xlsx为白名单列表文件保存位置
    translate('D:/black.xlsx','D:/vic(2).xlsx')#D:/black.xlsx为黑名单列表文件保存位置
""""        if s.isdigit():
          digit2 += 1"""