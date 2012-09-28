'''
PDB RENDERER MAC OS X EDITION
Created on Sep 28, 2012

@author: emerson
'''
import string
import data
import render
import os
from OpenGL.GL import *
from OpenGL.GLU import *

print "Welcome to ultrazoid_'s PDB renderer: Mac OS X Edition"

cont = False
while cont == False:
    fInput = string.upper(raw_input("Please input the *.pdb file name you would like to render(must be in same directory):"))
    if ".PDB" in fInput:
        try:
            print "*.pdb file recognised"
            print "searching for file..."
            dart = data.get(fInput)
            cont = True
        except IOError:
            print "File not found..."
            print "Did you misspell the name?"
            cont = False
    elif ".PDB" not in fInput:
        print "The filename you entered is not a PDB file..."
        print "Did you forget about the extension?"
        cont = False
pInput = string.upper(raw_input("File Loaded! Would you like to prepare it for rendering?(y/n)"))
if pInput == 'Y':
    print "PDB Renderer will now prepare the data"
    darter = data.clean(dart)
if pInput == 'N':
    print "User has chosen not to continue"
    print "PDB Renderer with now exit"
    os.sys.exit()
print "Data ready!"
cInput = raw_input("Continue?(y/n)")
if pInput == 'Y':
    print "PDB Renderer will now render the data"
    render.draw(darter)
if pInput == 'N':
    print "User has chosen not to continue"
    print "PDB Renderer with now exit"
    os.sys.exit()

        
        
        