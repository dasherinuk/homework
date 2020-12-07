userInput=input()
amount_list=int(userInput)
main_array=[]
for i in range(0,amount_list):
    array = [int(r) for r in input().split()]
    main_array.append(array)
sums_of_arrays=[]
for array in main_array:
    sums_of_arrays.append(sum(array))
print(max(sums_of_arrays))
