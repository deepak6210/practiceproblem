import random
print("Welcome you in this game it's a multi player random number choice game ")
print("Please enter the name of player one")
player_12 = input()
print("please enter the name of player two")
player_22 = input()
print("Enter the starting of list")
no_1 = int(input())
print("Enter the ending of  the list")
no_2 = int(input())
if no_1<no_2:
    lst = list(range(no_1, no_2))
    choice = random.choice(lst)
    choice1 = random.choice(lst)
    n = 1
    while n <= 2:
        if n == 1:
            choice = choice
        else:
            choice = choice1
        print(f"Please select the number in the range of {no_1} to {no_2}")
        if n == 1:
            print(f"it's your turn {player_12} Best of luck")
        else:
            print(f"it's your turn {player_22} Best of luck")
        chance = 1
        while (True):
            print(f"it's your {chance} chance ")
            sel_number = int(input())
            if sel_number not in range(no_1, no_2):
                print(f"please provide a number in a range of {no_1} to {no_2} you wasted your one chance")
                chance = chance + 1
                continue
            elif sel_number>choice:
                print(f"Your number is greater than the random number next time take a smaller number")
                print(f"Your range of the number is {no_1} to {no_2}")
                chance =chance +1
                continue
            elif sel_number<choice:
                print("Your number is smaller than the random number next time select a bigger number")
                print(f"your range of the number is {no_1} to {no_2}")
                chance = chance +1
                continue
            else:
                print(f"You guess the right number in {chance} chance congratulation")
                if n == 1:
                    player_1 = chance
                else:
                    player_2 = chance
                n = n+1
                break
else:
    print("Please provide the valid range your starting range is smaller than ending range")
    exit()


if player_1 < player_2:
    print(f"{player_12} wins in {player_1} chance")
    print(f"{player_22} lost the game")
elif player_1 == player_2:
    print(f"no body win both {player_12} & {player_22} take {player_1} chance to complete the game")
else:
    print(f"{player_22} win in {player_2} chance")
    print(f"{player_22} lost the game")
print("Thank you to both of you to play this game ")

