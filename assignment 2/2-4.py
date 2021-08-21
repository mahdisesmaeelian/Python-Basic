scores=  []
n = int(input("How many students do you have? "))

for i in range (n):
	score=float(input(f"Enter {i+1} student score :"))
	scores.append(score)
	
average=sum(scores)/n
min1= min(scores)
max1=max(scores)

print("The average of class is: ",average)
print("The min is: ",min1)
print("The max is: ",max1)