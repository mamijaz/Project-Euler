fo=open('input_pro42.txt','r+')
words=(fo.read()).split(',')

for i in xrange(len(words)):
    words[i]=words[i][1:-1]

def Is_Trianguler_Num(num):
    if not ((2*(num+1.0/8))**0.5-0.5)%1:
        return True

alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']   
count=0

for i in range(len(words)):
    wordsum=0
    for j in str(words[i]):
        wordsum+=alphabet.index(j)+1
    if Is_Trianguler_Num(wordsum):
        count+=1
        
print count

#162
