input_user=int(input())
main_array=[]

for i in range(0,input_user):
    array = [int(r) for r in input().split()]
    main_array.append(array)
len_array=input_user

# 1 2 3
# 4 5 6
# 7 8 9

sum_first_array=sum(main_array[0])
##for index in range(0,len_array):
##    sum_first_array+=main_array[index][0] 
    
sum_last_array=sum(main_array[-1])
##for index in range(0,len_array):
##    sum_last_array+=main_array[index][-1]


if sum_first_array > sum_last_array:
    main_array[0], main_array[-1] = main_array[-1], main_array[0]

    
print(*main_array, sep="\n")

    
    

