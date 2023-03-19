try:
    menu = []
    num = 1
    while True:
        item = input("choose item: ").title()
        itemn = str(num) + " "+ item
        num +=1
        menu.append(itemn)

except EOFError:
    print("\n".join(menu))