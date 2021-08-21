num1 = int(input(" Enter the first number : "))
num2 = int(input(" Enter the second number : "))


if num1 > num2:
    lessnum = num2
else:
    lessnum = num1

for i in range(1,lessnum+1):
    if((num1 % i == 0) and (num2 % i == 0)):
        bmm = i 

print(bmm)             


