input_user=int(input())
main_array=[]

for i in range(0,input_user):
    array = [int(r) for r in input().split()]
    main_array.append(array)
len_array=input_user

sum_first_column=0
for index in range(0,len_array):
    sum_first_column+=main_array[index][0]
    
sum_last_column=0
for index in range(0,len_array):
    sum_last_column+=main_array[index][-1]


if sum_first_column > sum_last_column:
    for i in range(0,len_array):
        main_array[i][0], main_array[i][-1] = main_array[i][-1], main_array[i][0]

    
print(*main_array, sep="\n")

    
    
