try:
    menu = []
    listn = 0
    while True:
        item = input("choose item: ")
        menu.append(item)

except EOFError:
    print("\n".join(menu))