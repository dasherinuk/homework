array = []
size = 20
for i in range(size):
    array.append(['.']*size)

for i in range(5):
    for ind in range(5):
        array[i][ind]='+'

for i in range(5):
    for ind in range(5):
        array[i+5][ind+5]='+'



for i in range(5):
    for ind in range(5):
        array[i+10][ind+10]='+'



for i in range(size):
    print(*array[i],sep='')

