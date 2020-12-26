input_user=int(input())
main_array=[]

for i in range(0,input_user):
    array = [int(r) for r in input().split()]
    main_array.append(array)
len_array=input_user

for ind in range(0,len_array//2): #(0,-1) (1,-2), (2,-3), (3,-4)
    print(ind)
    left_index = ind
    right_index = -ind-1
    sum_left_column=0
    for index in range(0,len_array):
        sum_left_column+=main_array[index][left_index]
        
    sum_right_column=0
    for index in range(0,len_array):
        sum_right_column+=main_array[index][right_index]

    print(sum_left_column, sum_right_column, left_index, right_index)
    if sum_left_column > sum_right_column:
        for i in range(0,len_array):
            main_array[i][left_index], main_array[i][right_index] = main_array[i][right_index], main_array[i][left_index]

        
print(*main_array, sep="\n")

    
