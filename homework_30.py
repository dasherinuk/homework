# 1 2 3 4 5
# 3 5 1 2 8
# 2 6 7 9 0
 
 
array = [int(r) for r in input().split()]
array2 = [int(r) for r in input().split()]
array3 = [int(r) for r in input().split()]
len_array= max( (len(array),len(array2), len(array3)) )
array_result = []

while len(array) < len_array:
    array.append(0)
while len(array2) < len_array:
    array2.append(0)
while len(array3) < len_array:
    array3.append(0)

for i in range(0,len_array):
    maximum=max([array[i],array2[i],array3[i]])
    array_result.append(maximum)





print(array_result)
