import pytube
class Media:
    def __init__(self):

        self.movielist = []
        myfile = open('database.txt', 'r')
        data = myfile.read()
        movie_list = data.split('\n')

        for i in range(len(movie_list)):
            movie_info = movie_list[i].split(',')
            self.movielist.append(movie_info)
        myfile.close()

    def showinfo(self):
        for i in range(len(self.movielist)):
            print(f'Movie {i} info is :', self.movielist[i])
            print('--------------------------------')    

    def download(self):
        flag = 0
        answer = input('\ngive me the name of the movie you wanna download: ')
        for i in range(len(self.movielist)):
            if answer == self.movielist[i][0]:
                link = self.movielist[i][4]
                first_stream = pytube.YouTube(link).streams.first()
                first_stream.download(output_path='./', filename='movie.mp4')
            else:
                flag += 1
            if flag >= len(self.movielist):
                print("This movie doesn't exist in our list")
        
showinfo = Media().showinfo()
moviedownload = Media().download()