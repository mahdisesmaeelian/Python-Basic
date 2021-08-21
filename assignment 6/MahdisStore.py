from pyfiglet import Figlet
import qrcode
def ShowMenu():
    print(' 1-Add product \n 2-Edit product \n 3-Delete product \n 4-Creat QrCode \n 5-Buy \n 6-Exit \n 7-Search \n 8-show list')

def AddProduct():
    productid=1006
    mydict={}
    mydict['id']=productid
    mydict['name']=input(('Enter a name of your product:'))
    mydict['price']=float(input('Enter the price of your product:'))
    mydict['count']=int(input('Enter the number of your stock: '))
    dictlist.append(mydict)
    print("Your producted added successfully")
    productid+=1
def showlist():
    for i in range(len(dictlist)):
        print(dictlist[i]['id'],',',dictlist[i]['name'],',',dictlist[i]['price'],',',dictlist[i]['count'])

def EditProduct():
    edition=input('Enter the name of the product that you wanna edit:')
    for i in range(len(dictlist)):
        if edition==dictlist[i]['name']:
            editing =int(input("What do you want to edit ? \n 1-Product's name \n 2-Product's price \n 3-Product's count\n :"))
    if editing==1:
        new=input('Enter the name you want:')
        dictlist[i]['name']=new
        print('Your product updated successfully',dictlist[i]) 
    elif editing==2:
        new=input('Enter the new price :')
        dictlist[i]['price']=new
        print('Your product updated successfully',dictlist[i])       
    elif editing==3:
        new=input('Enter the new count of the product:')
        dictlist[i]['count']=new
        print('Your product updated successfully',dictlist[i]) 
    else:
        print("index out of range")        

def DeleteProduct():
    delete=input('Enter the name of the product that you wanna delete:')
    for i in range(len(dictlist)):
        if delete==dictlist[i]['name']:
            del dictlist[i]
            break
    print("this product deleted successfully")  

def ShowQrcode():
    productqr=input('Enter the ID of the product:')
    for i in range(len(dictlist)):
        if productqr==dictlist[i]['id']:
          myqr=qrcode.make(dictlist[i])
          myqr.save(f'qrcode{i}.png')
          print('QrCode created')
          break

def Search():
    search=input('Enter the name of the product that you are looking for:')
    flag=0
    for i in range(len(dictlist)):
        if search==dictlist[i]['name']:
            print("here you are:", dictlist[i])
        else:
            flag+=1
        if flag>=5:    
            print("This product doesn't exist")

def buy():
    shoppingbasket=[]

    while True:
        ProductId=input('Enter the products id: ')
        flag=0
        for i in range(len(dictlist)):
            if ProductId == dictlist[i]['id']:
                tedad=int(input('how many of this product you want? : '))
                if tedad <= dictlist[i]['count']:
                    dictlist[i]['count']-=tedad
                    shoppingbasket.append({'name':dictlist[i]['name'],
                    'price':int(dictlist[i]['price']),
                    'count':tedad})
                    print("Product added to your basket successfully!")
                    

                    dictlist[i]['count']-=tedad

                    break
                else:
                    print("We don't have this much of this product^^")   
            else:
                flag+=1
            if flag>=5:    
                print("This product doesn't exist")

        buyagain=input("You wanna buy sth else? (yes or no):")
        if buyagain=='no' or buyagain=='No':
            break
            
    total_price=0
    print(shoppingbasket)
    for i in range(len(shoppingbasket)):
        total_price+=shoppingbasket[i]['price']*shoppingbasket[i]['count']
    print("Total price is:",total_price)
    print("Thanks for shopping^^")

def savetodatabase():
    myfile=open('database.txt', 'w')

    for i in range (len(dictlist)):
        line=str(dictlist[i]['id'])+','+str(dictlist[i]['name'])+','+str(dictlist[i]['price'])+','+str(dictlist[i]['count'])
        myfile.write(line)
        if i < len(dictlist)-1:
            myfile.write('\n')
    myfile.close()
    exit()    
def readDB():
    myfile=open('database.txt', 'r')
    data = myfile.read()

    editing=0
    count=0

    product_list = data.split('\n')

    for i in range(len(product_list)):
        product_info=product_list[i].split(',')
        mydict={}
        mydict['id']=product_info[0]
        mydict['name']=product_info[1]
        mydict['price']=product_info[2]
        mydict['count']=int(product_info[3])
        dictlist.append(mydict)
        
    myfile.close()

    print(dictlist)
    f = Figlet(font='standard')
    print(f.renderText('Mahdis Store'))

dictlist=[]
readDB()
while True:

    ShowMenu()

    choice = int(input('Please choose a number : '))

    if choice == 1:
        AddProduct()
    
    elif choice == 2:
        EditProduct()
                
    elif choice == 3:
        DeleteProduct()

    elif choice == 4:
        ShowQrcode()

    elif choice == 5:
        buy()

    elif choice == 6:
        savetodatabase()
           
    elif choice == 7:
        Search()

    elif choice == 8:
        showlist()