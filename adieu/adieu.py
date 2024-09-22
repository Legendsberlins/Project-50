import inflect

# assign engine function of inflect module to a variable
p = inflect.engine()
# create a list of names
names = []
try:
    # loop infinitely prompting user
    while True:
        name = input("")
        # append the names the user types into the names list
        names.append(name)
# if the user types in ctrl + d
except EOFError:
    # join names typed by the user using join method in inflect module
    concatenated_names = p.join(names)
    # print names concatenated with Adieu
    print("Adieu, adieu, to", concatenated_names)


"""for i in names: #This would have been done if the aim was to print Adieu for each name typed
    print("Adieu, ", end = "")"""
