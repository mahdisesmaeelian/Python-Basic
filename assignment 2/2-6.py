f=[]
n= int(input())

for i in range (n):
    if i>1:
        f.append(f[i-1]+f[i-2])
       
    else:    
        f.append(1)
    
print(f)
    
    
  
    