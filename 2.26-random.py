import random 
completed = False

while completed == False:
    mark = 0
    for i in range(10):
        a = random.randint(1,10)
        b = random.randint(1,10)
        value = a + b
        guess = input(str(a) + "+"+ str(b) + "=")
        if int(guess) <= 0:
            pass
        if int(guess) == value:
            mark += 1
            pass
        else:
            print("EEE")
    print("Coreect answers " + str(mark))
    completed =  True