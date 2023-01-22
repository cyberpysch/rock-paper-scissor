from random import randint


def game(computer_input,user_input):
     #for all possible condition
    if computer_input==user_input:#for draw match
        return None

    elif computer_input=="stone":#for computer selects rock
        if user_input=="paper":#user slects paper
            return True #print(f"Hurray! You Wins you selects {user_input} over computer {computer_input}")
        elif user_input=="scissor":
            return False #print(f"You Lose! computer selects {computer_input} over your {user_input}")

    elif computer_input=="paper":#paper
        if user_input=="scissor":
            return True #print(f"Hurray! You Wins you selects {user_input} over computer {computer_input}")
        elif user_input=="stone":#rock
            return False# print(f"You Lose! computer selects {computer_input} over your {user_input}")

    elif computer_input=="scissor":#scissor
        if user_input=="stone":#rock
            return True #print(f"Hurray! You Wins you selects {user_input} over computer {computer_input}")
        elif user_input=="paper":#paper
            return False #print(f"You Lose! computer selects {computer_input} over your {user_input}")

    

 # convert number to objects
rand_no=randint(1,3)
if rand_no==1:
    computer_input="stone"
elif rand_no==2:
    computer_input="paper"
elif rand_no==3:
    computer_input="scissor"

user_input=int(input("Selects 1 for 'stone', 2 for 'paper' and 3 for 'scissor' :"))
if user_input==1:
    user_input="stone"
elif user_input==2:
    user_input="paper"
elif user_input==3:
    user_input="scissor"


print(f"Computer selects {computer_input}")

a=game(computer_input=computer_input , user_input=user_input)

if a==True:
    print(f"Hurray! You Wins you selects {user_input} over computer {computer_input}")
elif a==None:
    print(f" This match is Draw computer selects {computer_input} and Player selects {user_input}")
elif a==False:
    print(f"You Lose! computer selects {computer_input} over your {user_input}") 