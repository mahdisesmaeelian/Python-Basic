def sum(x,y):
    result={}
    result['s'] = x ['s'] * y ['m'] + x ['m'] * y ['s']
    result['m'] = x ['m'] * y ['m']
    return result

def minus(x,y):
    result={}
    result['s'] = x ['s'] * y ['m'] - x ['m'] * y ['s']
    result['m'] = x ['m'] * y ['m']
    return result  

def mul(x,y):
    result={}
    result['s'] = x ['s'] * y ['s']
    result['m'] = x ['m'] * y ['m']
    return result    

def divide(x,y):
    result={}
    result['s'] = x ['s'] / y ['s']
    result['m'] = x ['m'] / y ['m']
    return result

s1=int(input('surat adad aval ro vared kon : '))
m1=int(input('makhraj adad aval ro vared kon : '))
s2=int(input('surat adad dovom ro vared kon : '))
m2=int(input('makhraj adad dovom ro vared kon : '))


num1={'s':s1, 'm':m1}
num2={'s':s2, 'm':m2}

while True:
    choose=input("choose 1-sum 2-minus 3-mul 4-divide :")

    if choose=='1':
        result=sum(num1,num2)
        print(result)
    elif choose=='2': 
        result=minus(num1,num2)
        print(result)
    elif choose=='3':
        result=mul(num1,num2)
        print(result) 
    elif choose=='4': 
        result=divide(num1,num2)
        print(result)