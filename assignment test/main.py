from pyfiglet import Figlet
import film
import series
import clip
import documentary

movielist=[]

def AddMedia():
    myfile=open('database.txt', 'r')
    data = myfile.read()
    movie_list = data.split('\n')
        
    for i in range(len(movie_list)):
        movie_info=movie_list[i].split(',')
        movielist.append(movie_info)

    for i in range(len(movielist)):
        if movielist[i][6]=='movie':
            media= film.Film(movielist[i][0],movielist[i][1],movielist[i][2],movielist[i][3],movielist[i][4],movielist[i][5],movielist[i][6])   

        elif movielist[i][6]=='series':
            media= series.Series(movielist[i][0],movielist[i][1],movielist[i][2],movielist[i][3],movielist[i][4],movielist[i][5],movielist[i][6])

        elif movielist[i][6]=='clip':
            media= clip.Clip(movielist[i][0],movielist[i][1],movielist[i][2],movielist[i][3],movielist[i][4],movielist[i][5],movielist[i][6])

        elif movielist[i][6]=='series':
            media= documentary.Documentry(movielist[i][0],movielist[i][1],movielist[i][2],movielist[i][3],movielist[i][4],movielist[i][5],movielist[i][6])   

        myfile.close()


def ShowMenu():
    print('1-Add movie\n2-Edit movie\n3-Delete movie\n4-Search\n5-Exit ')
        
def Addmovie():
    newmovie=[input('Enter name: '),input('Enter director: '),input('Enter IMDB: '),input('Enter url: '),input('Enter duration: '),input('Enter casts: '), input('Enter category: ')]
    movielist.append(newmovie)
    print('Media added succssesfuly')

def Editmovie():
    flag = 0
    answer = input('\ngive me the name of the movie you wanna edit: ')
    choice = input('What do you want to do? 1-edit name 2-edit director 3-edit IMDB score 4-edit url 5-edit duration 6-edit casts 7-edit category : ') 
   
    for i in range(len(movielist)):

        if answer == movielist[i][0]:
            if choice == '1':
                movielist[i][0]=input('Enter new name : ')
            if choice == '2':
                movielist[i][1]=input('Enter new director : ') 
            if choice == '3':
                movielist[i][2]=input('Enter new IMDB score : ')
            if choice == '4':
                movielist[i][3]=input('Enter new URL : ') 
            if choice == '5':
                movielist[i][4]=input('Enter new duration : ') 
            if choice == '6':
                movielist[i][5]=input('Enter new casts : ') 
            if choice == '7':
                movielist[i][6]=input('Enter new category : ')  
            print("Succssesfuly edited")                      
        else:
            flag += 1
        if flag >= len(movielist):
            print("\nThis movie doesn't exist in our list")    

def Search():
    pass 

def Deletemovie():
    flag = 0
    answer = input('\ngive me the name of the movie you wanna delete: ') 
    for i in range(len(movielist)):
        if answer == movielist[i][0]:
            del movielist[i]
            print("This media deleted succssesfuly")

        # else:
        #     flag += 1

        # if flag >= len(movielist):
        #     print("\nThis movie doesn't exist in our list")           

def Savetodatabase():
    myfile=open('database.txt', 'w')

    for i in range (len(movielist)-1):
        line=str(movielist[i][0])+','+str(movielist[i][1])+','+str(movielist[i][2])+','+str(movielist[i][3])+','+str(movielist[i][4])+','+str(movielist[i][5])+','+str(movielist[i][6])
        myfile.write(line)
        if i < len(movielist)-1:
            myfile.write('\n')
    myfile.close()
    exit() 

f = Figlet(font='standard')
print(f.renderText('2 4 M o v i e s'))

AddMedia()

while True:
    ShowMenu()
    choice = int(input('Please choose a number : '))

    if choice == 1:
        Addmovie()
    
    elif choice == 2:
        Editmovie()
                
    elif choice == 3:
        Deletemovie()

    elif choice == 4:
        Search()

    elif choice == 5:
        exit()

    else:    
        break       

    Savetodatabase()   
    