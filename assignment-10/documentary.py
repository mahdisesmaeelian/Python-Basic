from media import Media
class Documentry(Media):
    def __init__(self,n,di,I,u,du,c,cat):
        Media.__init__(self,n,di,I,u,du,c,cat)
        pass
    def show(self):
        print('hi')    
