array = []
size = 20

for index in range(3):
    
    
    for i in range(size):
        array.append(['.']*size)

    for i in range(5):
        for ind in range(1):
            array[i][0]='+'
        
    for i in range(5):
        for ind in range(1):
            array[0][i]='+'
        
    for i in range(5):
        for ind in range(1):
            array[i][5]='+'

    for i in range(5):
        for ind in range(1):
            array[5][i]='+'
    

    
    for i in range(size):
        print(*array[i],sep='')
