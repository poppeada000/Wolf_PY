import re
import matplotlib.pyplot as plt

def getContent(file):
    return open('./src/content/'+file+'.txt', 'r').readlines()



if __name__ == '__main__'   :
    getContent('./src/maps/mapdata.txt')