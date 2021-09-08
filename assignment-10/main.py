from enum import Flag
from typing import cast
from media import Media
from pyfiglet import Figlet
from film import Film
from series import Series
from clip import Clip
from documentary import Documentry

class Main:
    def __init__(self):
    
        try:
            myfile=open('database.txt', 'r')
        except:
            print("Database doesn't found")  

        self.movielist=[]

        data = myfile.read()
        movie_list = data.split('\n')       

        for i in range(len(movie_list)):
             
            movie_info=movie_list[i].split(',')

            if movie_info[6]=='movie':
                self.movielist.append(Film(movie_info)) 

            elif movie_info[6]=='series':
                self.movielist.append(Series(movie_info))

            elif movie_info[6]=='clip':
                self.movielist.append(Clip(movie_info))

            elif movie_info[6]=='documentory':
                self.movielist.append(Documentry(movie_info))
                
            myfile.close()
        self.ShowMenu()

    def ShowMovielist(self):
        for i in self.movielist:
            i.showinfo()  

    def AddMovie(self):
        name =input('Enter name :')
        director = input('Enter director : ')  
        IMDB = input('Enter IMDB : ')
        url = input('Enter url : ')
        duration = input('Enter duration : ')
        casts = input('Enter casts : ')
        category =input('Enter category : ')

        if category == 'series':
            epnum = input('Enter the number of series episodes : ')
            movie_info = [name,director,IMDB,url,duration,casts,category,epnum]
        else:
            movie_info = [name,director,IMDB,url,duration,casts,category]

        if category=='movie':
            self.movielist.append(Film(movie_info)) 

        elif category=='series':
            self.movielist.append(Series(movie_info))

        elif category=='clip':
            self.movielist.append(Clip(movie_info))

        elif category=='documentory':
            self.movielist.append(Documentry(movie_info))

        else:
            print("This type of category doesn't exist!")

        self.ShowMovielist()
        self.ShowMenu()   

    def EditMovie(self):
        flag=0
        choise = input("\nEnter the name of the movie that you wanna edit : ")

        for media in self.movielist:

            if choise == media.name:

                if media.category == 'series':
                    media.edit_series()

                if media.category == 'movie':
                    media.edit_film()

                if media.category == 'clip':
                    media.edit_clip()

                if media.category == 'documentory':
                    media.edit_documentory()

            else:
                flag+=1

            if flag>=5:    
                print("This movie doesn't exist")    

        self.ShowMenu()

    def Deletemovie(self):

        flag=0
        choise = input("\nEnter the name of the movie that you wanna delete : ")
         
        for media in self.movielist:
            if choise == media.name:
                self.movielist.remove(media)
                print("\nThis movie deleted succssesfuly\n")
            else:
                flag+=1

            if flag>=5:    
                print("This movie doesn't exist")    

        self.ShowMenu()

    def Download(self):
        flag = 0
        answer = input('\ngive me the name of the movie you wanna download: ')
        for media in self.movielist:
            if answer == media.name:
                media.download()
            else:
                flag += 1

            if flag >= len(self.movielist):
                print("\nThis movie doesn't exist in our list")    
        self.ShowMenu()

    def Searchbydu(self):
        firstdu = input("Give me the first duration like this [00:00]: ")
        secdu = input("Give me the second duration like this [00:00]: ")
        firstdu = firstdu.split(':')
        h1 = int(firstdu[0])
        min1 = int(firstdu[1])
        du1 = h1*3600 + min1*60
        secdu = secdu.split(':')
        h2 = int(secdu[0])
        min2 = int(secdu[1])
        du2 = h2*3600 + min2*60

        for media in self.movielist:
            moviedu = media.duration.split(':')
            h3 = int(moviedu[0])
            m3 = int(moviedu[1])
            moviedu3 = h3*3600 + m3*60

            if du1 <= moviedu3 <= du2:
                print("This movie seems near to your input duration : ",media.name)

    def Savetodatabase(self):
        myfile=open('database.txt', 'w')
        
        for media in self.movielist: 
            if media.category == 'series':   
                myfile.write((media.name)+','+(media.director)+','+(media.IMDB)+','+(media.url)+','+(media.duration)+','+(media.casts)+','+(media.category)+','+(media.numberofep))
            else:
                myfile.write((media.name)+','+(media.director)+','+(media.IMDB)+','+(media.url)+','+(media.duration)+','+(media.casts)+','+(media.category))
            if media != self.movielist[-1]:
                myfile.write('\n')

        myfile.close()
        print("Database updated succssefully")
        exit() 

    def ShowMenu(self):
        
        print('1-Add movie\n2-Edit movie\n3-Delete movie\n4-Search by duration\n5-Show movielist\n6-Download movie\n7-Save and Exit ')
    
        choice = input('Please choose a number : ')
                
        if choice == '1':
            self.AddMovie()
            
        elif choice == '2':
            self.EditMovie()
                        
        elif choice == '3':
            self.Deletemovie()

        elif choice == '4':
            self.Searchbydu()

        elif choice == '5':
            self.ShowMovielist()

        elif choice == '6':
            self.Download()

        elif choice == '7':
            self.Savetodatabase()

        else:    
            print('Wrong input') 
            

f = Figlet(font='standard')
print(f.renderText('2 4 M o v i e s'))

main = Main()