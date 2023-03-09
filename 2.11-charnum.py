#Counts number of characters in the text 

def main():
    textinput = input("Tell me something: ")
    if textinput != "":
        print(textinput + " has "+ str(len(textinput)) + " characters")
    else:
        print("Don't be shy")
        main()

main()