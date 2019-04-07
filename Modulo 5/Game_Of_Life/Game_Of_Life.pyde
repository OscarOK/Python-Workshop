from Enviroment import *

def setup():
    frameRate(10)
    #size(1000, 900)
    fullScreen()
    background(0)
    
    global e
    e = Enviroment(width, height, 10)

def draw():
    e.update()
