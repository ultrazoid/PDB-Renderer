'''
Created on Sep 28, 2012

@author: emerson
'''
import string

def get(Filename):
    fileOpen = open(Filename, 'r')
    fileGot = fileOpen.readlines()
    fileOpe = open('swamp.txt','w')
    fileOpe.write(Filename)
    fileOpe.close()
    return fileGot

def clean(ProccessedList):
    ready = []
    xx = 0
    for lineOfData in ProccessedList:
        line = string.split(lineOfData,' ')
        if 'ATOM' == line[0]:
            ready.insert(xx,lineOfData)
        xx += 1
    return ready