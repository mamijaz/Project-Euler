fo=open('input_pro22.txt','r+')
st=(fo.read()).split(',')

for i in range(len(st)):
    st[i]=st[i][1:-1]
    
st=sorted(st)

char=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

total_name_worth=0

for i in range(len(st)):
    worth=0
    for j in st[i]:
        worth+=(char.index(j)+1)
    total_name_worth+=(worth*(i+1))

print total_name_worth
      
if 'COLIN' in st:
    worth=0
    for j in 'COLIN':
        worth+=(char.index(j)+1)
    print worth,(worth*(st.index('COLIN')+1))
