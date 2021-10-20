import random

list = ['✋🏻','🤚🏻']
userscore = 0
pc1score = 0
pc2score = 0

for i in range (5):

    pc1 = random.choice(list)
    pc2 = random.choice(list)
    userchoice = input('Enter number 1 for ✋🏻 or number 2 for 🤚🏻 : ')

    if userchoice == '1':
        user = '✋🏻'
    elif userchoice == '2':
        user = '🤚🏻'
    else:
        print('Try again')

    print(pc1,pc2,user)

    if pc1 == pc2 != user :
        userscore += 1
    elif pc1 != pc2 == user :
        pc1score += 1
    elif pc2 != pc1 == user :
        pc2score += 1
    
    print('(pc1 score :',pc1score,')(pc2 score :',pc2score,')(Your score :',userscore,')')

if userscore > pc2score and userscore > pc1score:
    print('You Win!')

elif pc1score > pc2score and pc1score > userscore:
    print('PC1 Win!')

elif pc2score > pc1score and pc2score > userscore:
    print('PC2 Win!')

elif pc1score == pc2score > userscore:
    print("PC1 and PC2 Win")

elif pc1score == userscore > pc2score:
    print("PC1 and You Win")

elif pc2score == userscore > pc1score:
    print("PC2 and You Win")    