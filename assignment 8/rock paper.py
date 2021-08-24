import random

options=["rock", "paper", "scissor"]
scores={'computer':0 ,'user':0}

def result():
    if scores['user']>=scores['computer']:
        print("Congratulations you win ^^")
    if scores['user']<=scores['computer']:
        print("You lose!")    
    if scores['user']==scores['computer']:
        print("Win-Win ^^") 

for i in range(10):

    pc_choice=random.choice(options)

    user_choice= input("Choose between 1-rock 2-paper 3-scissor: ")

    print('The pc choice is :',pc_choice)

    if (user_choice=="rock" and pc_choice=="rock") or (user_choice=="paper" and pc_choice=="paper") or (user_choice=="scissor" and pc_choice=="scissor"):
        pass

    elif (user_choice=="rock" and pc_choice=="paper") or (user_choice=="paper" and pc_choice=="scissor") or (user_choice=="scissor" and pc_choice=="rock"):
        scores['computer']+=1

    elif (user_choice=="rock" and pc_choice=="scissor") or (user_choice=="paper" and pc_choice=="rock") or (user_choice=="scissor" and pc_choice=="paper"):
        scores['user']+=1

    print('pc score:',scores['computer'],'user score:',scores['user'])

result()   