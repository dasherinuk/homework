array=[int(z) for z in input("Enter key: ").split()]
max_array=array[0]
for i in range(0,len(array)):
    if max_array<array[i]:
        max_array=array[i]



min_v = array[0]
for i in range(0,len(array)):
    if min_v>array[i]:
        min_v = array[i]

print(min_v, max_array)
print(max_array - min_v)

