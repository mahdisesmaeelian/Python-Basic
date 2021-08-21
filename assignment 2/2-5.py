import random

while True:
    
    randnum=random.randint(1,6)
    print(randnum)
    
    if randnum==6:
        randnum=random.randint(1,6)
    else :
        break