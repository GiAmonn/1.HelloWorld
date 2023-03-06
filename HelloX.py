#Creates variable called name and asks the user to give it a value
name = input("Hey, what's your name?")
match name.index(0):
    case "gio":
        print("Hello, " + name.title() + "!")
    case "eka":
        print("Hello, " + name.title() + "! You look amazing today!")
    case "nika":
        print("Hello, " + name.title() + "! Do you even lift bro?")
    case "elene":
        print("Hello, " + name.title() + "! Wanna go for lunch?")
