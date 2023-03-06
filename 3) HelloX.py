#Exercise 3: Greets you based on your name.
name = input("Hey, what's your name? ")
match name[0]:
    case "g":
        print("Hello, " + name.title() + "!")
    case "m":
        print("Hello, " + name.title() + "! You look amazing today!")
    case "a":
        print("Hello, " + name.title() + "! Do you even lift bro?")
    case "t":
        print("Hello, " + name.title() + "! Wanna go for lunch?")
    case _:
        print("No special greeting for you " + name.title())