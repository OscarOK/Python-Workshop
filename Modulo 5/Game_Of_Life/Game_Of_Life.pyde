from Enviroment import *

def setup():
    frameRate(10)
    size(1000, 900)
    background(0)
    
    global e
    e = Enviroment(width, height, 40)

def draw():
    e.update()
