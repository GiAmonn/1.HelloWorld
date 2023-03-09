#Takes the name and quote of a celebrity and informs user if they're right or wrong
#if not guessed correctly prints the actual quote from the ecelebrity

quote = input("What is the quote? ")
name = input("Who said it? ").title()

quotes=[
        "\"We are a way for the cosmos to know itself.\"",
        "\"No space of regret can make amends for one life's opportunity misused.\"",
        "\"But in ya heeeeaad.\"",
        "\"Mars is there, waiting to be reached.\"",
        "\"Hips don\'t lie.\"",
        ]
match name:
    case "Carl Sagan":
        print(name + " said: " + quotes[0])
    case "Charles Dickens":
        print(name + " said: " + quotes[1])
    case "The Cranberries" :
        print(name + " said: " + quotes[2])
    case "Buzz Aldrin":
        print(name + " said: " + quotes[3])
    case "Shakira":
        print(name + " said: " + quotes[4])
    case _:
        print("Try again")