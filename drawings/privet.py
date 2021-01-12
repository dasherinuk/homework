array = []
size = 20
for i in range(size):
    array.append([' ']*size*3)

for i in range(0,5):
    array[0][i]='+'
    array[i][0]='+'
    array[i][5]='+'

for i in range(0,5):
    array[15][i]='+'
    array[i][15]='+'
    array[i][20]='+'

##for i in range(0,5):
##    array[0][i+5]='+'
##    array[i+5][0]='+'
##    array[i+5][5]='+'
    #array[i][10]='+'

##    array[i][15]='+'
##    array[20][5]='+'
##    array[i][0]='+'
##    array[i][5]='+'
##    

##for i in range(0,20):
##    array[5][i]='+'
##    array[i][5]='+'
##    array[i][10]='+'
##    array[10][i]='+'

##for i in range(0,2):
##    array[i][5]='+'
##    array[i][5]='+'
  


    

for i in range(size):
    print(*array[i],sep='')
