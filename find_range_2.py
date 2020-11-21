array=[int(z) for z in input("Enter key: ").split()]
max_array=array[0]
for i in range(0,len(array)):
    if max_array<array[i]:
        max_array=array[i]
array[0]=max_array


min_v = array[0]
for i in range(0,len(array)):
    if min_v>array[i]:
        min_v = array[i]
array[0]=min_v

print=array[range]

