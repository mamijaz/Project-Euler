target = 100
numbers = [x for x in range(1,target)]
ways = [1] + [0]*target

for number in numbers:
    for i in range(number, target+1):
        ways[i] += ways[i-number]

print ways[target]

#190569291
