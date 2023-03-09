quote = input("What is the quote? ")
name = input("Who said it? ").title()

quotes={
        "Carl Sagan":"\"We are a way for the cosmos to know itself.\"",
        "Charles Dickens":"\"No space of regret can make amends for one life's opportunity misused.\"",
        "The Cranberries":"\"But in ya heeeeaad\"",
        "Buzz Aldrin":"\"Mars is there, waiting to be reached.\"",
        "Shakira":"\"Hips don\'t lie\"",

        }

if quotes[name] == quote:
    print("Well this was unexpected")
else: 
    print(name + " said: " + quotes[name])