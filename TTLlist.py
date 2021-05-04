import matplotlib.pyplot as plt
import pandas as pd

f = pd.read_excel("D:/创新设计/blackping.xlsx")
d = pd.read_excel('D:/创新设计/whiteping.xlsx')
list1 = f['TTL']
dist1 = d['TTL']
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

list2 = f['num']
dist2 = d['num']
x2_data = []
data_dict = {}
for key in list2:
        data_dict[key] = data_dict.get(key, 0) + 1
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
        data_dict[key] = data_dict.get(key, 0) + 1
for i in dist2:
        if not i in a2_data:
            a2_data.append(i)
a2_data.sort()
b2_data = []
for i in a2_data:
        b2_data.append(data_dict[i])

plt.subplot(2,2,1)
plt.plot(x1_data,y1_data, '-', color = 'red',linewidth = 1,label = 'black_list')
plt.plot(a1_data,b1_data,'-',color = 'green',linewidth=1,label='white_list')
plt.title('TTL')
plt.legend()
plt.xlabel('x1')
plt.ylabel('y1')

plt.subplot(2,2,2)
plt.plot(x2_data,y2_data, '-', color = 'red',linewidth = 1,label = 'black_list')
plt.plot(a2_data,b2_data,'-',color = 'green',linewidth=1,label='white_list')
plt.title('tranform_num')
plt.legend()
plt.xlabel('x2')
plt.ylabel('y2')
plt.show()

