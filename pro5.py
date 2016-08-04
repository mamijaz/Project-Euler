smallest_Multiple=1
Drange=20


for i in range(1,Drange+1):
    if smallest_Multiple%i:
        for j in range(1,i+1):
            if not (smallest_Multiple*j)%i:
                smallest_Multiple*=j
                break
                

print smallest_Multiple
        
#232792560
