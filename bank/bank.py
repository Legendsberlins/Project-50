greeting = input("Greeting? ").lower().strip()
if greeting.startswith("hello"): #if "hello" == greeting[0:5]
    print("$0")
elif greeting.startswith("h"): #elif "h" == greeting[0]:
    print("$20")
else:
    print("$100")
