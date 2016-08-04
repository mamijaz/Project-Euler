maxsum=0
for a in xrange(1,100):
    for b in xrange(1,100):
        numsum=0
        for i in str(a**b):
            numsum+=int(i)
        if numsum>maxsum:
            maxsum=numsum

print maxsum

#972
        
        
