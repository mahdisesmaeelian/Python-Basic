def sum():
    result=(complex1['a']+complex2['c'])
    resulti=(complex1['bi']+complex2['di'])
    print('The sum of these two complex number is: ',result,'+',resulti,'i')
    return result,resulti

def minus():
    result=(complex1['a']-complex2['c'])
    resulti=(complex1['bi']-complex2['di'])
    print('The substraction of these two complex number is: ',result,'+(',resulti,')i') 
    return result,resulti

def mul():
    result=(complex1['a']*complex2['c'])-(complex1['bi']*complex2['di'])
    resulti=(complex1['bi']*complex2['c'])+(complex1['a']*complex2['di'])
    print('The multiply of these two complex number is: ',result,'+(',resulti,')i')
    return result,resulti        
    
complex1={'a':4, 'bi':12}
complex2={'c':7 ,'di':6} 

sum()
minus()
mul()