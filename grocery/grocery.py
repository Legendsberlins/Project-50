grocery = {}
while True:
    try:
        item = input("")
        if item in grocery: #Check if item is already in dict and increment its value if so
            grocery[item] += 1
        else: #if not give it value 1
            grocery[item] = 1
    except EOFError: #stop loop if user clicks ctrl + d
        for key in sorted(grocery.keys()): #sort items alphabetically
            print(grocery[key], key.upper())
        break





