import math
first_number = int(input("please enter the first number: "))
answer=(input("do you want to use any of (radical) (tan),(cos),(sin) or (factorials) functions? "))
if answer== "yes":
    sign=(input("so choose the function you want:"))
    if sign=="radical":
        result=math.sqrt(first_number)
        print(result)
    elif sign=="tan":
        result=math.tan(math.radians(first_number))
        print(result)
    elif sign=="cos":
        result=math.cos((first_number))
        print(result) 
    elif sign=="sin":
        result=math.sin(math.radians(first_number))
        print(result)   
    elif sign=="factorial":
        result=math.factorial(first_number)
        print(result)       
else:
    second_number = int(input("please enter the second number: "))
    sign = input("what do you want? + - / *: ")
    if sign == "+":
        print("the result is :" ,first_number+second_number)
    elif sign == "-":
        print("the result is :" ,first_number-second_number)
    elif sign == "*":
        print("the result is :" ,first_number*second_number)
    elif sign == "/" and second_number != 0:
        print("the result is :" ,first_number/second_number)
    elif second_number == 0:
        print("error")
