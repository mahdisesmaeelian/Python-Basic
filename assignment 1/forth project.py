firt_name=input("Please enter the firstname: ")
last_name=input("Please enter the lastname: ")
math=int(input("enter your score in math: "))
history=int(input("enter your score in history: "))
science=int(input("enter your score in science: "))
average = (math+history+science)/3

if average<12:
    print("you fail! :(")
elif average>=12 and average<17:
    print("your score is normal ;)")
elif average>=17 and average<=20:
    print("you are great *o* ")        