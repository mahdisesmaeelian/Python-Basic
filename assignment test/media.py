class Media:
    def __init__(self,n,di,I,u,du,c,cat):
        self.name = n
        self.director = di  
        self.IMDB = I
        self.url = u
        self.duration = du
        self.casts = c
        self.category =cat
        
    def showinfo():
        pass

    def download():
        pass

    # def readDB():
    #     movielist=[]
    #     myfile=open('database.txt', 'r')
    #     data = myfile.read()
    #     movie_list = data.split('\n')
        
    #     for i in range(len(movie_list)):
    #         movie_info=movie_list[i].split(',')
    #         mydict={}
    #         mydict['name']=movie_info[0]
    #         mydict['director']=movie_info[1]
    #         mydict['IMDB']=movie_info[2]
    #         mydict['url']=movie_info[3]
    #         mydict['durationh']=movie_info[4]
    #         mydict['durationm']=movie_info[5]
    #         mydict['casts']=movie_info[6]
    #         mydict['type']=movie_info[7]
    #         movielist.append(mydict)

    #     myfile.close()
    #     print(movielist) 


# Media.readDB()
# movie1=Media(1,2,3,4,5,6,7)