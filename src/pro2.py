list1=[1,1]
list2=[]
while True:
    i=list1[-1]+list1[-2]
    if i>4000000:
        break
    list1.append(i)
    if i%2==0:list2.append(i)

print sum(list2)
    
    
    
    
