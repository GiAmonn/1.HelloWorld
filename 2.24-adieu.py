try:    
    names = []
    while True:
        name = input("Write a name:").title()
        names.append(name)
        
except:
    print(names)
    sentence = "Adieu "
    if len(names) == 1:
        print("Aduie " + names[0])
    elif len(names) == 2:
        sentence = "Adieu " + names[0] + " and " + names[1]
    elif len(names) > 2:
        for i in range(len(names) - 2):
            sentence = sentence + names[i] + ", "
        final_sentence =  sentence + names[len(names)-2 ] + " And " + names[len(names)-1]
print(final_sentence)
