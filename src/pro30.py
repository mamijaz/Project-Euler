list1=[]
for j in range(10,100):
    i=str(j)
    a=int(i[0])
    b=int(i)
    s=a**5+b**5
    if i==str(s):list1.append(int(i))
for j in range(100,1000):
    i=str(j)
    a=int(i[0])
    b=int(i[1])
    c=int(i[2])
    s=a**5+b**5+c**5
    if i==str(s):list1.append(int(i))
for j in range(1000,10000):
    i=str(j)
    a=int(i[0])
    b=int(i[1])
    c=int(i[2])
    d=int(i[3])
    s=a**5+b**5+c**5+d**5
    if i==str(s):list1.append(int(i))
for j in range(10000,100000):
    i=str(j)
    a=int(i[0])
    b=int(i[1])
    c=int(i[2])
    d=int(i[3])
    e=int(i[4])
    s=a**5+b**5+c**5+d**5+e**5
    if i==str(s):list1.append(int(i))
for j in range(100000,1000000):
    i=str(j)
    a=int(i[0])
    b=int(i[1])
    c=int(i[2])
    d=int(i[3])
    e=int(i[4])
    f=int(i[5])
    s=a**5+b**5+c**5+d**5+e**5+f**5
    if i==str(s):list1.append(int(i))
    
print sum(list1)
