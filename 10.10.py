#hello world
#3 1 2 4
#hell|o wo|rld
#lhel|wo o|rld

open_text = list(input("enter open text: "))#str to list char
key = [int(z)-1 for z in input("Enter key: ").split()]


len_key = len(key)

if len_key > len(open_text):
    print("error key")
else:
    for i in range(0, len(open_text)-(len_key-1),len_key):
        list_char=[]
        for j in range(len_key):
            list_char.append(open_text[i+j])

        for j in range(len_key):
            open_text[i+j] = list_char[key[j]]

    print(*open_text,sep="")
