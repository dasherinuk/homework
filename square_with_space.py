array = []
size = 20
for i in range(size):
    array.append(['.']*size)

for j in range(0, 15, 5):
    for i in range(5):
        array[i+j][j]='+'
            
    for i in range(5):
        array[j][i+j]='+'
            
    for i in range(5):
        array[i+j][j+4]='+'

    for i in range(5):
        array[j+4][i+j]='+'
    

    
for i in range(size):
    print(*array[i],sep='')
