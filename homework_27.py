array = [int(r) for r in input().split()]
len_array=len(array)
array2=array[1::2]#array[start:finish:step]
print(array2)
print(sum(array2))

