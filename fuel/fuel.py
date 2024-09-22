while True:
    fraction = input("Rate: ")

    try:
        numerator, denominator = fraction.split("/")
        new_numerator = int(numerator)
        new_denominator = int(denominator)
        if new_numerator > new_denominator:
            print("Invalid values")
        else:
            percentage = round(new_numerator / new_denominator * 100)
            if percentage <= 1:
                print("E")
                break
            elif percentage >= 99:
                print("F")
                break
            else:
                print(f"{int(percentage)}%")
                break
    except(ValueError, SyntaxError, ZeroDivisionError):
        print("Not valid")
