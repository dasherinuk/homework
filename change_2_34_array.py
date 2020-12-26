input_user=int(input()) #user enters the amount of arrays he wants
main_array=[]           #variable is made

for i in range(0,input_user):  #for i in range(0,the amount of arrays
    array = [int(r) for r in input().split()] #user enters arrays
    main_array.append(array)  #arrays are appended into variable main_array

# 10 20 30 40
# 90 88 87 65
# 11 12 12 23
# 56 34 56 78
    
for ind in range(0,input_user//2): 
    #print(ind)
    top_index = ind              #left_index=0 to middle 
    bottom_index = -ind-1          #right_index=end to middle
    sum_top_array=sum(main_array[top_index])

    sum_bottom_array=sum(main_array[bottom_index])
    
    if sum_top_array > sum_bottom_array:
            main_array[top_index], main_array[bottom_index] = main_array[bottom_index], main_array[top_index]

        
print(*main_array, sep="\n")

    

