fo=open('input_pro59.txt','r+')
st=fo.read().split(',')
st=[int(i) for i in st]

a=97
b=97
c=97
def Decrypt(a,b,c,msg):
    length=len(msg)
    for i in range(0,length,+3):
        msg[i]=chr(msg[i]|a)
    for j in range(1,length,+3):
        msg[j]=chr(msg[j]|b)
    for k in range(2,length,+3):
        msg[k]=chr(msg[k]|c)
    message=''
    for i in msg:
        message+=i
    if message[:2].isalpha():
        print message[:2]

for a in range(97,97+26):
    for b in range(97,97+26):
        for c in range(97,97+26):
            Decrypt(a,b,c,st[:])

