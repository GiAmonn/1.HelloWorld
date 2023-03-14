def main():

    plate = input("Plate: ")
    char_remove = [" ",".",",","!","?"]
    for char in char_remove:
        plate = str(plate).replace(char, "")
    print("hello" + plate)

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    ss = str(s)
    print(s)
    if len(s) >= 2 and len(s) <= 6 and ss[0:2].isalpha() == True and ss[len(s)-2:].isdigit() == True :
            return True
main()