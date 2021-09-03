from pyfiglet import Figlet
from media import Media

class Management:
    def __init__(self):

        self.movielist=[]
        myfile=open('database.txt', 'r')
        data = myfile.read()
        movie_list = data.split('\n')
        
        for i in range(len(movie_list)):
            self.movie_info=movie_list[i].split(',')
            self.movielist.append(self.movie_info)
        myfile.close()

    def ShowMenu():
        print('1-Add movie\n2-Edit movie\n3-Delete movie\n4-Search\n5-Exit ')

    def Addmovie():
        pass 

    def EditProduct():
        pass  

    def Search():
        pass 

    def Deletemovie(self):
        flag = 0
        answer = input('\ngive me the name of the movie you wanna delete: ') 
        for i in range(len(self.movielist)):
            if answer == self.movielist[i][0]:
                self.movielist[i].pop
            else:
                flag += 1
            if flag >= len(self.movielist):
                print("\nThis movie doesn't exist in our list")    

    def Savetodatabase():
        pass

f = Figlet(font='standard')
print(f.renderText('2 4 M o v i e s'))



while True:

    Management.ShowMenu()

    choice = int(input('Please choose a number : '))

    if choice == 1:
        Management.Addmovie()
    
    elif choice == 2:
        Management.EditProduct()
                
    elif choice == 3:
        deletemovie=Management()
        deletemovie.Deletemovie()

    elif choice == 4:
        Management.Search()
           
    elif choice == 5:
        Management.Savetodatabase()
