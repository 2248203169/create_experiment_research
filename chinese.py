with open("D:/创新设计/H.txt","r",encoding='utf-8') as f:
    s = f.read()
    result = "".join(i for i in s if ord(i) > 256)
    f.close()
with open("D:/创新设计/yellow.txt",'w',encoding='utf-8') as f:
    f.write(result)
    f.close()