array = []
size = 20
for i in range(size):
    array.append([' ']*size*2)

##for j in range(0, 20):
##    for i in range(5):
##        array[j][i+j]='+'
##    for i in range(5):
##        array[j+1][i+j]='+'

for ind in range(0,20,2):
    for i in range(0,40,2):
        array[ind][i]="*"
    for i in range(1,40,2):
        array[ind+1][i]="*"

for i in range(size):
    print(*array[i],sep='')


print(len(array))
print(len(array[0]))
