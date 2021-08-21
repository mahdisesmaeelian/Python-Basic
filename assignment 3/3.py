NumberList = []
temp=0
for i in range (5):
	num=int(input())
	NumberList.append(num)
	
for i in range(len(NumberList)-1):
    if (NumberList[i] < NumberList[i+1]):
        temp+=1
    else:
        temp-=1 

if temp == len(NumberList)-1:
    print("this list is sorted")
else:
    print("this list isn't sorted")    
