userInput = int(input("please enter a number to proceed: "))

if(userInput <= 10):
    action = int(input("please enter an action to perform: 1.Addition 2.Sub 3: multiplication 4.divide with 10: " ))
    num = int(input("please enter a number to perform the action with"))
    if(action ==1):
        userInput += num
        print(userInput)
    elif(action == 2):
        userInput -= num
        print(userInput)
    elif(action == 3):
        userInput *= num
        print(userInput)
    elif(action ==4):
        userInput /= num
        print(userInput)
    else:
        print("Enter a valid action")                 
else:
    print("Enter a number within 10")