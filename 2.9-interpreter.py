exps = input("Expressions: ").split()
x = float(exps[0])
y = (exps[1])
z = float(exps[2])

match y:
    case "/":
        print(x/z)
    case "*":
        print(x*z)
    case "+":
        print(x+z)
    case "-":
        print(x-z)
