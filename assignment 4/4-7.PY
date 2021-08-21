listnum1=[]
listnum2=[]

num1 = int(input(" Enter the first number : "))
num2 = int(input(" Enter the second number : "))

for i in range(1,num2+1):
    listnum1.append(num1*i)
for i in range(1,num1+1):
    listnum2.append(num2*i)

print(listnum1) 
print(listnum2) 

for i in range(1,len(listnum1)):
    if listnum1[i] in listnum2:
        kmm=listnum1[i]
        break

print("the kmm of these two number is : ",kmm)      

  