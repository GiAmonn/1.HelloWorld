def main():
    try:
        guessed = False
        number = int(input("Enter a number: "))
        while number< 0: 
            number = int(input("Enter a number: "))
        
        while guessed == False:
            guess = int(input("Guess the number: "))
            if guess < 0 :
                pass
            elif guess < number:
                print("Too small")
            elif guess > number:
                print("Too large")
            elif guess == number:
                print("Correct: ")
                guessed = True
    except ValueError:
        main()

main()