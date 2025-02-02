answer = 5
attempts = 2

while True:
    user_input = input("Guess the Number: ")
    try:
        if int(user_input) == answer:
            print("You Won!")
            break
        elif int(user_input) != answer:
            if attempts != 0:
                print(f"Match Failed, try again {attempts} attempts left.")
                attempts -= 1
            else:
                print("You Lost!")
                break

    except ValueError:
        if attempts != 0:
                print("Try again, {attempts} attempts left.")
                attempts -= 1
        else:
            print("You Lost")
            break