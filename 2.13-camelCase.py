var = input("Write in camelCase: ")
snake_case = ""
for char in var:
    if char.isupper():
        snake_case += "_" + char.lower()
    else:
        snake_case += char

print("Here's your snake_case:" + snake_case)