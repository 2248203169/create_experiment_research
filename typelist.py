#可视化展示数据
import matplotlib.pyplot as plt
import pandas as pd

f = pd.read_excel("D:/创新设计/vic(1).xlsx")
d = pd.read_excel('D:/创新设计/vic(2).xlsx')
list1 = f['length']
dist1 = d['length']
x1_data = []
data_dict = {}
for key in list1:
    data_dict[key] = data_dict.get(key,0) + 1
for i in list1:
    if not i in x1_data:
        x1_data.append(i)
x1_data.sort()
y1_data = []
for i in x1_data:
    y1_data.append(data_dict[i])

a1_data = []
data_dict = {}
for key in dist1:
    data_dict[key] = data_dict.get(key,0) + 1
for i in dist1:
    if not i in a1_data:
        a1_data.append(i)
a1_data.sort()
b1_data = []
for i in a1_data:
    b1_data.append(data_dict[i])

list2 = f['split']
dist2 = d['split']
x2_data = []
data_dict = {}
for key in list2:
    data_dict[key] = data_dict.get(key,0) + 1
for i in list2:
    if not i in x2_data:
        x2_data.append(i)
x2_data.sort()
y2_data = []
for i in x2_data:
    y2_data.append(data_dict[i])

a2_data = []
data_dict = {}
for key in dist2:
    data_dict[key] = data_dict.get(key,0) + 1
for i in dist2:
    if not i in a2_data:
        a2_data.append(i)
a2_data.sort()
b2_data = []
for i in a2_data:
    b2_data.append(data_dict[i])

list3 = f['special']
dist3 = d['special']
x3_data = []
data_dict = {}
for key in list3:
    data_dict[key] = data_dict.get(key,0) + 1
for i in list3:
    if not i in x3_data:
        x3_data.append(i)
x3_data.sort()
y3_data = []
for i in x3_data:
    y3_data.append(data_dict[i])

a3_data = []
data_dict = {}
for key in dist3:
    data_dict[key] = data_dict.get(key,0) + 1
for i in dist3:
    if not i in a3_data:
        a3_data.append(i)
a3_data.sort()
b3_data = []
for i in a3_data:
    b3_data.append(data_dict[i])

list4 = f['rate']
dist4 = d['rate']
x4_data = []
data_dict = {}
for key in list4:
    data_dict[key] = data_dict.get(key,0) + 1
for i in list4:
    if not i in x4_data:
        x4_data.append(i)
x4_data.sort()
y4_data = []
for i in x4_data:
    y4_data.append(data_dict[i])

a4_data = []
data_dict = {}
for key in dist4:
    data_dict[key] = data_dict.get(key,0) + 1
for i in dist4:
    if not i in a4_data:
        a4_data.append(i)
a4_data.sort()
b4_data = []
for i in a4_data:
    b4_data.append(data_dict[i])

list5 = f['max_num']
dist5 = d['max_num']
x5_data = []
data_dict = {}
for key in list5:
    data_dict[key] = data_dict.get(key,0) + 1
for i in list5:
    if not i in x5_data:
        x5_data.append(i)
x5_data.sort()
y5_data = []
for i in x5_data:
    y5_data.append(data_dict[i])

a5_data = []
data_dict = {}
for key in dist5:
    data_dict[key] = data_dict.get(key,0) + 1
for i in dist5:
    if not i in a5_data:
        a5_data.append(i)
a5_data.sort()
b5_data = []
for i in a5_data:
    b5_data.append(data_dict[i])

list6 = f['change']
dist6 = d['change']
x6_data = []
data_dict = {}
for key in list6:
    data_dict[key] = data_dict.get(key,0) + 1
for i in list6:
    if not i in x6_data:
        x6_data.append(i)
x6_data.sort()
y6_data = []
for i in x6_data:
    y6_data.append(data_dict[i])

a6_data = []
data_dict = {}
for key in dist6:
    data_dict[key] = data_dict.get(key,0) + 1
for i in dist6:
    if not i in a6_data:
        a6_data.append(i)
a6_data.sort()
b6_data = []
for i in a6_data:
    b6_data.append(data_dict[i])

plt.subplot(2,2,1)
plt.plot(x1_data,y1_data, '-', color = 'red',linewidth = 1,label = 'black_list')
plt.plot(a1_data,b1_data,'-',color = 'green',linewidth=1,label='white_list')
plt.title('length')
plt.legend()
plt.xlabel('x1')
plt.ylabel('y1')

plt.subplot(2,2,2)
plt.plot(x2_data,y2_data, '-', color = 'red',linewidth = 1,label = 'black_list')
plt.plot(a2_data,b2_data,'-',color = 'green',linewidth=1,label='white_list')
plt.title('split')
plt.legend()
plt.xlabel('x2')
plt.ylabel('y2')

plt.subplot(2,2,3)
plt.plot(x3_data,y3_data, '-', color = 'red',linewidth = 1,label = 'black_list')
plt.plot(a3_data,b3_data,'-',color = 'green',linewidth=1,label='white_list')
plt.title('special')
plt.legend()
plt.xlabel('x3')
plt.ylabel('y3')

plt.subplot(2,2,4)
plt.plot(x4_data,y4_data, '-', color = 'red',linewidth = 1,label = 'black_list')
plt.plot(a4_data,b4_data,'-',color = 'green',linewidth=1,label='white_list')
plt.title('rate')
plt.legend()
plt.xlabel('x4')
plt.ylabel('y4')
plt.show()

plt.subplot(2,2,1)
plt.plot(x5_data,y5_data, '-', color = 'red',linewidth = 1,label = 'black_list')
plt.plot(a5_data,b5_data,'-',color = 'green',linewidth=1,label='white_list')
plt.title('max_num')
plt.legend()
plt.xlabel('x5')
plt.ylabel('y5')

plt.subplot(2,2,2)
plt.plot(x6_data,y6_data, '-', color = 'red',linewidth = 1,label = 'black_list')
plt.plot(a6_data,b6_data,'-',color = 'green',linewidth=1,label='white_list')
plt.title('change')
plt.legend()
plt.xlabel('x6')
plt.ylabel('y6')
plt.show()