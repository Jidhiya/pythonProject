secret_number = 777

print(
    """
    +================================+
    | Welcome to my game, muggle!    |
    | Enter an integer number        |
    | and guess what number I've     |
    | picked for you.                |
    | So, what is the secret number? |
    +================================+
    """)
userInput = int(input("Enter an integer number : "))
while userInput:
    if userInput == 777:
        print("Well done, muggle ! You are free now.")
        break;
    else:
        print("Ha ha ! You're stuck in my loop!")
        userInput = int(input("Enter another integer number : "))

