#!/usr/bin/python
import re
#-----------------------------------------------------------

buildques = []
pages = ["Coyote","Grey_Fox","Red_Fox","Grey_Wolf"]
collected_data = {"Title":"","Subtitle":"","Weight":"","Height":"","Length":"","Color":"","Pyhsical attributes":"","Image " : ""}

def getoffset(words) :
    p = re.compile(r'(.+): ')
    if p.match(words) == None   :
        return ""
    return str(p.match(words).group(0))

#Opens content files
def getContent(file):
    return open('/home/pi/Desktop/WOLF_PY/src/content/'+file+'.txt', 'r').readlines()

#Initalizes Collected Data
def buildqueinit():
    [(buildques.append([i,dict()]))for i in pages]

def queText(text, pos)  :
    find = re.compile(r'(Title:|Subtitle:|Weight:|Height:|Length:|Physical attributes:|Image: )(.+)')
    for i in text :
        found = find.search(i)
        if found != None:
            buildques[pos][1][found.group(1)] = found.group(2)

#Add doc ques to build ques
def buildque()  :
    buildqueinit()
    for i in range(len(pages)) :
        text = getContent(pages[i])
        queText(text, i)
    return (buildques)

if __name__ == '__main__'   :
    print(buildque())