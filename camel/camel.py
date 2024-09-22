#Ask user for input
camelCase = input("camelCase: ")
#print snakecase
snake_case = print("snake_case: ", end = "")
#convert input to snakecase
for i in camelCase:
    if i.isupper():
        print("_"+ i.lower(), end = "")
    else:
        print(i, end = "")
print()
