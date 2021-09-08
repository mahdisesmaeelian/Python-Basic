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
        print(f'Movie name :', self.name)
        print('--------------------------------') 

    def download(self):
        print('Downloading...')
        link = self.url
        first_stream = pytube.YouTube(link).streams.first()
        first_stream.download(output_path='./', filename='movie.mp4')
        print('\nThis movie downloaded succssefuly')