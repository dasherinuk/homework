array = []
size = 20
for i in range(size):
    array.append([' ']*size*3)

##for i in range(0,7):
##    array[i+i][10]='+'

for i in range(0,5):
    array[i+i+5][i+i]='/'
    array[i+i+5][-i+i]='/'
    array[i+i+11][i+i]='/'
    array[i+i+11][-i+i]='/'
    
##    array[i][i*3//2]='+'
##    array[i][i*2]='+'
##
##
##    array[i][-i*3-1]='+'
##    array[i][-i*2-1]='+'
##    array[i][-i*2]='+'

for i in range(size):
    print(*array[i],sep='')



