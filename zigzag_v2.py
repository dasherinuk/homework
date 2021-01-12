array = []
size = 20
for i in range(size):
    array.append([' ']*size)

#for j in range(0, 20):
   
    
for i in range(0,5):
    array[0][0]='+'
for i in range(0,5):
    array[1][1]='+'
    


for i in range(size):
    print(*array[i],sep='')

