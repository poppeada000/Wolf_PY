import pygame 
import numpy as np
import matplotlib as plt
from gpiozero import Button#Gpio Integration this may be unix operatble
from time import sleep
import sys
import wx #this is a windows tool kit change to gtk for Unix systems
#This document will be used to generate the main screen.
#-----------------------------------------------------------
buildque = []
app = wx.App(False)
display_width, display_height = wx.GetDisplaySize()
colors = {"black":(0,0,0),"white":(255,255,255),'red' : (255,0,0), 'green' : (0,255,0)}
clock = pygame.time.Clock()
kioskDisplay = pygame.display.set_mode((0, 0), (600,800))#pygame.FULLSCREEN)
pygame.display.set_caption("Interactive Map")

background_image = pygame.image.load("./src/img/park.jpg")#This loads the JPEG to its origonal size
background_image = pygame.transform.scale(background_image,(display_width,display_height))

#Pre Condition: There is nothing passed into this function
#Post Condition: This will be treated as a boolean function 
# and will return 1 for successful and 0 for error
def display_window()    :
    intro = True
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        buildque.append([background_image,[0,0]])
        kioskDisplay.blit(background_image,[0,0])
        #largeText = pygame.font.Font('freesansbold.ttf',40)
        #TextSurf, TextRect = text_objects("Powered By EPICS", largeText)
        #TextRect.center = ((display_width/2),(display_height/4))
        #gameDisplay.blit(TextSurf, TextRect)
        kioskDisplay.blit(pygame.image.load("./src/img/wolfparklogo.jpg"),[(display_width/2),(display_height/4)])
        #button1=button("Snapdragon projects",50,200,250,25,white,red,"Play")
        #button2=button("Overlook of Snapdragon",50,250,250,25,white,red,"Play")
        pygame.display.update()
        clock.tick(15)

def text_objects(text, font):
    textSurface = font.render(text, True, colors['green'])
    return textSurface, textSurface.get_rect()

#Trys to build the object will return False if it fails to build
def build(builing, loc):
    try:
        kioskDisplay.blit(building, loc)
        return True
    except  :
        return False

#Used to create loaded image objects 
def load_img(path,width,height) :
    load = pygame.image.load(path)
    scaled = pygame.transform.scale(load,(width,height))
    return scaled

def message_display(text):
    largeText = pygame.font.Font('comicsans',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    kioskDisplay.blit(TextSurf, TextRect)

#This is Controls current page
def button(msg,x,y,h,w,ic,ac,action=None):
    #mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

if __name__ == '__main__' :
    display_window()


display_window()
quit()
    
