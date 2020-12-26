user_input=int(input())
main_array=[]
new_array=[]


for i in range(0,user_input):
    array = [int(r) for r in input().split()]
    main_array.append(array)

for col in range(0,user_input):
    result = 1
    for row in range(0,user_input):
        array=main_array[row]
        result=array[col]*result
    new_array.append(result)
print(max(new_array))



