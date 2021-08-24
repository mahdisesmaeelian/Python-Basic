import imageio
import os

files = os.listdir('gif')
images=[]

for i in range (len(files)):
    image=imageio.imread('gif/'+files[i])
    images.append(image)

imageio.mimsave('mygif.gif',images)      