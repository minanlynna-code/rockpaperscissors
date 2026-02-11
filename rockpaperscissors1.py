import random
print("Welcome to The Game...")
choice = ["Rock", "Scissors","Paper"]
computer_choice = random.choice(choice)
round = 1
while round <= 3:
    print("rock scissors paper")
    user_choice = input("Your Choice is: ")
    if(computer_choice == user_choice):
        print("Tie")  
    else:
        if(computer_choice == choice[0]):
            if(user_choice == choice[1]):
                print("You Lost!")
            elif(user_choice == choice[2]):
                print("You win!") 
        elif(computer_choice == choice[1]):
            if(user_choice == choice[0]):
                print("You win!")
            elif(user_choice == choice[2]):
                print("You Lost!")
        elif(computer_choice == choice[2]):
            if(user_choice == choice[0]):
                print("You Lost!")
            elif(user_choice == choice[1]):
                print("You win!")
    print("The computer choice is " + computer_choice)
    round += 1




