def Cion_Dividing():
    target = 60000
    while True:
        print target
        numbers = [x for x in range(1,target)]
        ways = [1] + [0]*target
        for number in numbers:
            for i in range(number, target+1):
                ways[i] += ways[i-number]
        for i in ways:
            if not i%1000000:
                return ways.index(i)
        target+=target
            
print Cion_Dividing()
