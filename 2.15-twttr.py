sentence = input("write something: ")
sen_two = ""

syl = ["A","I","E","O","I"]
for char in sentence :
    if char.upper() in syl:
        sen_two += "" 
    else:
        sen_two += char
print(sen_two)