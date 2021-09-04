from media import Media
class Series(Media):
    def __init__(self,n,di,I,u,du,c,cat):
        Media.__init__(self,n,di,I,u,du,c,cat)
        #self.numberofep = ep

    def show(self):
        print('hi')    
