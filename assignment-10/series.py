from media import Media
class Series(Media):
    def __init__(self,movielist):
        Media.__init__(self,movielist[0],movielist[1],movielist[2],movielist[3],movielist[4],movielist[5],movielist[6])
        self.numberofep = movielist[7]

    def edit_series(self):
        print("\n1-edit name\n2-edit director\n3-edit IMDB\n4-edit url\n5-edit duration\n6-edit casts\n7-edit category\n8-edit number of episodes")
        choice = input("\nEnter the number of the option you wanna edit according to the menu : ")

        if choice == '1':
            newinput = input('Enter new name: ')
            self.name = newinput
            print("This movie edited")
        if choice == '2':
            newinput = input('Enter new director: ')
            self.director = newinput
            print("This movie edited")
        if choice == '3':
            newinput = input('Enter new IMDB: ')
            self.IMDB = newinput
            print("This movie edited")
        if choice == '4':
            newinput = input('Enter new url: ')
            self.url = newinput
            print("This movie edited")
        if choice == '5':
            newinput = input('Enter new duration: ')
            self.duration = newinput
        if choice == '6':
            newinput = input('Enter new casts: ')
            self.casts = newinput
            print("This movie edited")
        if choice == '7':
            newinput = input('Enter new category: ')
            self.category = newinput
            print("This movie edited")
        if choice == '8':
            newinput = input('Enter new number of episods: ')
            self.numberofep = newinput
            print("This movie edited")
        else:
            print('Wrong input') 