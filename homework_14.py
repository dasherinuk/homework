user_input=int(input())
main_array=[]
new_array=[]
multiply_array=[]
addition_array=[]


for i in range(0,user_input):
    array = [int(r) for r in input().split()]
    main_array.append(array)
    
#user_input=3    
for col_ind in range(0,user_input):
    res = 1
    for row_ind in range(0,user_input):
        res *= main_array[row_ind][col_ind]#main_array[0][0] main_array[1][0] main_array[2][0]
                                           #main_array[0][1] main_array[1][1] main_array[2][1]
                                           #main_array[0][2] main_array[1][2] main_array[2][2] 
    multiply_array.append(res)
    

for col_ind in range(0,user_input):
    res = 0
    for row_ind in range(0,user_input):
        res += main_array[row_ind][col_ind]#main_array[0][0] main_array[1][0] main_array[2][0]
                                           #main_array[0][1] main_array[1][1] main_array[2][1]
                                           #main_array[0][2] main_array[1][2] main_array[2][2] 
    addition_array.append(res)
    

##if multiply_array>addition_array:
##    print("1")
##if addition_array>multiply_array:
##    print("-1")
##else:
##    print("0")

for i in range(user_input):
    if multiply_array[i]>addition_array[i]:
        res=1
    elif multiply_array[i]<addition_array[i]:
        res=-1
    else:
        res=0
    new_array.append(res)

print(new_array)
