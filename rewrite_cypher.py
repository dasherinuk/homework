text_open=list(input("Enter your text:"))
key_text=[int(n)-1 for n in input("Enter your key:").split()]

len_key=len(key_text)
if len_key>len(text_open):
    print("Incorrect key")

else:
    for i in range(0,len(text_open)-(len_key-1),len_key):
        array=[]
        for p in range(len_key):
            array.append(text_open[i+p])
        for p in range(len_key):
            text_open[i+p]=array[key_text[p]]


print(*text_open,sep="")
