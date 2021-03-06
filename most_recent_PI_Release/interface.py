#!/usr/bin/python
from application import *
import pygame 
import time
import os
import numpy as np
#import matplotlib as plt
#from gpiozero import Button#Gpio Integration this may be unix operatble
from time import sleep
import sys
#import wx

#filepath= dirname
path = (os.path.dirname(os.path.realpath(__file__)))
print(path)
pygame.init()
#app = wx.App(False)
display_width=1920
display_height = 1080
kioskDisplay = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Interactive Map")
background_image = pygame.image.load(path+"/src/img/park3.jpeg")#This loads the JPEG to its origonal size
background_image = pygame.transform.scale(background_image,(display_width,display_height))
TitleText = pygame.font.SysFont('gentium',100)
SubtitleText = pygame.font.SysFont('gentium',40)
ContentText = pygame.font.SysFont('gentium',35)
clock = pygame.time.Clock()
masterQue = []
txt_height = [0]
lastY = ((display_height/8)+(2*display_height/10))
pygame.mouse.set_visible(False)
#Needs an array passed into with location 0 the pygame object and 
# location 
def build(building):
    kioskDisplay.blit(building[0],building[1])

#Used to create loaded image objects 
def load_img(path,width,height) :
    load = pygame.image.load(path)
    return pygame.transform.scale(load,(width,height))

#Will Create a build ready object
def text_objects(text, font, pos, masterloc):
    textSurface = font.render(text, True, (255,255,255))
    rect = textSurface.get_rect()
    if len(pos) == 2:
        rect.center = pos
        masterQue[masterloc][1].append((textSurface, rect)) 
    elif len(pos) == 4:
        blit_text(kioskDisplay,text,(pos[0],pos[1]),font,masterloc,True)
    elif len(pos) == 3:
        blit_text(kioskDisplay,text,(pos[0], pos[1]),font,masterloc,False)        
    #return textSurface, rect

def blit_text(surface, text, pos, font,masterloc,center, color=pygame.Color('white')):
    total_width = 0
    oriX, oriY = pos
    if center == True   :
        total_width = font.size(text)[0]
        print(total_width)
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    max_width = display_width*(1/2)
    #print(max_width)
    x, y = pos
    if total_width >= max_width    :
        x = x - (max_width/2)
    if total_width < max_width and total_width > 0  :
        x = x-(total_width/2)
    offset = getoffset(text)
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= (oriX + max_width) and center == False:
                x = pos[0]+(font.size(offset)[0])
                txt_height.append(word_height) # Reset the x.
                y += word_height  # Start on new row.
                #lastY += word_height
            elif center == True and x + word_width >= (oriX + max_width/2):
                total_width = total_width + oriX - x
                if total_width < max_width :
                    x =  oriX - (total_width/2)
                elif total_width >= max_width   :
                    x = oriX - (max_width/2)
                y += word_height
                #lastY += word_height# Start on new row.
            masterQue[masterloc][1].append((word_surface, (x, y)))
            #lastY +=word_height
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.f
        #lastY += word_height

def pageDiv()  :
    content = buildque()
    pos = 0
    
    for i in content    :
        #txt_height = [0]
        masterQue.append([i[0],[]])
        contentCount = len(i[1])
        keys = list(i[1].keys())
        stored = 0
        lastY = ((display_height/8)+(2*display_height/10))
        for x in range(len(keys))   :
            if keys[x] == 'Title:':
                contentCount -= 1
                text_objects(i[1][keys[x]], TitleText, (display_width/2,display_height/10),pos)
            elif keys[x] == 'Subtitle:':
                contentCount -= 1
                text_objects(i[1][keys[x]], SubtitleText, (display_width/2,2*display_height/10,0,0),pos)
            elif keys[x] == 'Image: ':
                rended = load_img(path+i[1][keys[x]],int(display_width/3),int(display_height/3))
                masterQue[pos][1].append((rended, ((display_width/2)+(display_width/10),6*(display_height/10))))
            else:
                if len(keys[x]+i[1][keys[x]])>0:
                    stored +=1
                    #text_objects(keys[x]+i[1][keys[x]], ContentText, (display_width*.05,((display_height/8)+(2*display_height/10))+ (sum(txt_height))+(x*40),0),pos)
                    #print(lastY)
                    text_objects(keys[x]+i[1][keys[x]], ContentText, (display_width*.05,lastY+sum(txt_height)+(stored*40),0),pos)
        pos += 1
        t = sum(txt_height)
        txt_height.append(-1*t)
        

def newpage():
    kioskDisplay.blit(background_image,[0,0])

def goHome():
    kioskDisplay.blit(background_image,[0,0])
    pygame.display.update()
    print("The application went home")
    height = int(display_height/2)
    width = int(display_width/5)
    img = load_img(path+"/src/img/wolfparklogo.jpg",width,height)
    build([img,[(display_width/2)-(width/2),(display_height/2)-(height/2)]])
    pygame.display.update()
    
def done():
    pygame.quit()
    exit()

if __name__ == '__main__'   :
    intro = True
    print(pygame.font.get_fonts())
    kioskDisplay.blit(background_image,[0,0])
    pygame.display.update()
    pageDiv()
    goHome()
    time.sleep(3)
    kioskDisplay.blit(background_image,[0,0])
    i = 0
    while intro == True:
        
        kioskDisplay.blit(background_image,[0,0])
        pygame.display.update()
        for x in masterQue[i][1]:
            build(x)
            pygame.display.update()
        i+=1
        if (i>3)    :
            intro = False
        time.sleep(5)
    pygame.quit()
    exit()