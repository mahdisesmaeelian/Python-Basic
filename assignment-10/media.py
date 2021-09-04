import pytube
class Media:
    def __init__(self,n,di,I,u,du,c,cat):
        self.name = n
        self.director = di  
        self.IMDB = I
        self.url = u
        self.duration = du
        self.casts = c
        self.category =cat
        
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