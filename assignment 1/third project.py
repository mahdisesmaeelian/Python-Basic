weight=float(input("Enter your weight : "))
height=float(input("Enter your height : "))
BMI=weight/(height/100)**2
print(BMI)
if BMI <=18.5:
    print("You are under weight")
if BMI > 18.5 and BMI<=25:
    print("You are normal")
if BMI > 25 and BMI<=30:
    print("You are over weight")         
if BMI > 30 and BMI<=35:
    print("You are obese") 
if BMI > 35:
    print("You are extremly")        