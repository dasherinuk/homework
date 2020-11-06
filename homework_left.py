array=[]
input_amount=int(input("Enter the amount of elements"))

for i in range (0,input_amount):
    element_input=int(input("Enter your element"))
    array.append(element_input)

print(array)

for i in range(input_amount+1, 0, +1):# if ammount = 5 then i = 4 ... 1
    array[i] = array[i+1]

array[0]=0
print(array)
