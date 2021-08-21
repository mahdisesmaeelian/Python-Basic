import random
list1=[]

n=int(input("set the lenght of list : "))

while True:
    RandomNum=random.randint(1,100)
    
    if RandomNum in list1:
        break
    else:
        list1.append(RandomNum)

print(list1)
    