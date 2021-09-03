from media import Media
class Film(Media):
    def __init__(self,n,di,I,u,duh,dum,c):
        Media.__init__(self,n,di,I,u,duh,dum,c)
        pass
    def show(self):
        print('hi',self.name)    

movie1=Film('Coda','Sian Heder',8.1,'https://www.imdb.com/title/tt10366460/?ref_=ext_shr_lnk',1, 51 ,'Emilia Jones')
movie1.show()