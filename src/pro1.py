list1=[]
for i in range(0,1000,3):
    if i not in list1:list1.append(i)
for i in range(0,1000,5):
    if i not in list1:list1.append(i)
print sum(list1)
    
