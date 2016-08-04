p=0
for i in range(100,1000):
    for j in range(100,1000):
        if str(i*j)==str(i*j)[::-1]:
            if p<i*j:
                p=i*j
print p
            
       
       
        
        
