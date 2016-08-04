def findSumOfSqr(num):
    sum1=0
    for i in range(num+1):
        sum1=sum1+i**2
    return sum1
def findSqrOfSum(num):
    sum1=0
    for i in range(num+1):
        sum1=sum1+i
    return sum1**2
print (findSqrOfSum(100)-findSumOfSqr(100))
