def main():
    #Prompt user for question
    answer = input("What's the time? ")
    #Call convert function
    time = convert(answer)
    #Fix conditions to label breakfast, lunch and dinner
    if time >= 7.0 and time <= 8.0:
        print("Breakfast time")
    elif time >= 12.0 and time <= 13.0:
        print("Lunch time")
    elif time >= 18.0 and time < 19.0:
        print("Dinner time")


def convert(time):
    #Get hours and minutes
    hours, minutes = time.split(":")
    #Convert time into float number
    new_minute = float(minutes) / 60
    new_hour = float(hours)
    #Return result to main function
    return new_hour + new_minute



if __name__ == "__main__":
    main()
