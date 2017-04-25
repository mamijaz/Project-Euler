def get_input_matrix(name,order):
    fo=open(name,'r+')
    string=(fo.read()).split('\n')
    fo.close()
    metrix=[]
    for line in string[0:order]:
        met=line.split(',')
        for i in range(len(met)):
            met[i]=int(met[i])
        metrix.append(met)
    return metrix

metrix=get_input_matrix('input_pro81_82_83.txt',80)

def min_path_sum(row,col):
    if row==0 and col==0:
        return metrix[row][col]
    elif row==0:
        return metrix[row][col]+metrix[row][col-1]
    elif col==0:
        return metrix[row][col]+metrix[row-1][col]
    else:
        return metrix[row][col]+min(metrix[row-1][col],metrix[row][col-1])

position=0
while position<80:
    for num in range(position):
        metrix[num][position]=min_path_sum(num,position)
        metrix[position][num]=min_path_sum(position,num)
    metrix[position][position]=min_path_sum(position,position)
    position+=1

print metrix[79][79]
    
#427337        
