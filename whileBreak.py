userInput = input("Enter the secret word:")

while True:
    if userInput == 'chupacabra':
        print("You've successfully left the loop")
        break;
    else:
        userInput = input("Try again ! Enter the secret word:")