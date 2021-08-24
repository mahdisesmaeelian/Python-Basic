n=int(input('Enter a number: '))
a=1

for i in range(n):
    for o in range(n-i):
        print(end='  ')
    for j in range(a):
        print('*', end=' ')
    a+=2    
    print()

for i in range(n+1):
    for o in range(i):
        print(end='  ')
    for j in range(a):
        print('*', end=' ')
    a-=2    
    print()        