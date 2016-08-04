import time

start=time.time()
D=2
y=1
max_x_to_the_power_two=0
D_for_max_X=[]
D_range=1000
Except=[61,97,106,109,139,149,151]


def IsSquare(num):
    if not num%1 and not(num**0.5)%1:
        return True
    else:
        return False

for D in range(2,D_range+1):
    if IsSquare(D)or D in Except:
        continue
    
    print D
    
    y=1
    while True:
        X_to_the_power_two=1+D*(y**2)
        if IsSquare(X_to_the_power_two):
            if X_to_the_power_two>max_x_to_the_power_two:
                max_x_to_the_power_two=X_to_the_power_two;
                D_for_max_X.append(D);
            break
        y+=1
       
    
print 'D_for_max_X :',D_for_max_X[-1]
print time.time()-start
