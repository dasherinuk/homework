array=[]
amount=int(input("Enter the amount of elements"))

for i in range (0,amount):
    element_input=int(input("Enter your element"))
    array.append(element_input)

print(array)

for i in range(0,amount):
    if array[i] > 0:
        array[i]=1
    elif array[i] < 0:
        array[i]=-1

print(array)

