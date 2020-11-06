array=[]
UserInput= int(input("Enter amount numbers: "))

for i in range (0,UserInput):
    enter=int(input("Enter a number:"))
    array.append(enter)

print(array)
print(min(array))
print(max(array))


