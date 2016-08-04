n=3
list1=[1,1]
term=2
while True:
    term+=1
    i=list1[-1]+list1[-2]
    if len(str(i))>=n:
        break
    list1.append(i)
    

print term
