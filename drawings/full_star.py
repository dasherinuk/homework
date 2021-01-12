array = []
size = 20
for i in range(size):
    array.append([' ']*size*3)

for i in range(0,10):
    array[i+1][size//2]='+'
    array[size//2][i+10]='+'
    array[size//2][i+4]='+'
    array[i+10][size//2]='+'
    array[i][4]='+'
    array[i][10]='+'
##    array[5][i]='+'
##
##
for i in range(size):
    print(*array[i],sep='')
