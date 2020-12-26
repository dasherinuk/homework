userInput=input()
amount_list=int(userInput)
main_array=[]
for i in range(0,amount_list):
    array = [int(r) for r in input().split()]
    main_array.append(array)



array_maximum=[]
for array in main_array:
    array_maximum.append(max(array))
    


print(min(array_maximum))

# 1 2 3 4 5
# 9 8 1 2 7
# 7 8 1 9 4
# 8 1 4 2 1 
# 0 1 4 2 5

#1 + 8 + 1 + 2 + 5 ?
