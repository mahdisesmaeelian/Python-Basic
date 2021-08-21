n = int (input("enter the length of table: "))

khayampaskal=[[None for i in range(n)]for j in range (n)]

for i in range(n):
    khayampaskal[i][0]=1
    khayampaskal[i][i]=1    

for i in range(2,n):
    for j in range(1,i):
        khayampaskal[i][j]=khayampaskal[i-1][j]+khayampaskal[i-1][j-1]    

for i in range(n):
    for j in range(i+1):
        print(khayampaskal[i][j], end='\t')
    print()