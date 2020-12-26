user_input=int(input())
user_input=int(input())
main_array=[]
new_array=[]
len_user_input=user_input

for i in range(0,user_input):
    array = [int(r) for r in input().split()]
    main_array.append(array)

for col in range(0,len_user_input):
    array=[]

    for row in range(0,len_user_input):
        arr = main_array[row]
        val = arr[col]
        array.append(val)


    new_array.append(array)


for index in range(0,len_user_input):
    multiply=user_input[index]=user_input[i+1]

print(max(multiply))


print(*new_array, sep="\n")



    
