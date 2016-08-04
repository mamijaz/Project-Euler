count=0
for i in range(1,10):
    for j in range(1,22):
        if len(str(i**j))==j:
            count+=1
            print i,j
print count

#49
