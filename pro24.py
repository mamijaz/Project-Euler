import itertools
a=list(itertools.permutations(range(10), 10))
b=''
for i in a[1000000-1]:
    b=b+str(i)
print b
