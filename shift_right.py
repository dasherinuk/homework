spaces=int(input("Enter the amount of spaces you want the numbers to move "))
array=[int(w) for w in input("Enter numbers ").split()]

for j in range(spaces):
    last = array[-1]#save last
    for i in range(len(array)-1, 0, -1):
        array[i] = array[i-1]
    array[0] = last#set last to front

print(*array,sep=" ")


