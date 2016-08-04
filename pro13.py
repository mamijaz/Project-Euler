fo=open('input_pro13.txt','r+')
txt=fo.read();
st=[]
for i in txt.split():
    st.append(int(i))
print (str(sum(st)))[:10]
