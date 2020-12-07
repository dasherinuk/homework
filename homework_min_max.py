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
