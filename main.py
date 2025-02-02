answer = 5
user_input=input("ENTER YOUR NUMBER: ")
if type(user_input) != int:
    print("user input must be interger")
if user_input == answer:
    print("you won")
else:
    print("you lost")