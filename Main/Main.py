'''
PDB RENDERER MAC OS X EDITION
Created on Sep 28, 2012

@author: emerson
'''
from __future__ import division
import string
import data
import render
import os
import pygame, math, numpy
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import camera
import spatial
import vecmath

def extStrip(pdb):
    heck = pdb
    mid = heck[:-4]
    print mid
    new = mid + ".txt"
    print new
    return new

class Spectator:
    def __init__(self, w, h, fov):
        pygame.init()
        pygame.display.set_mode((w,h), pygame.OPENGL | \
            pygame.DOUBLEBUF)
        glMatrixMode(GL_PROJECTION)
        aspect = w/h
        gluPerspective(fov, aspect, 0.001, 100000.0);
        glMatrixMode(GL_MODELVIEW)
        pygame.mouse.set_cursor(*pygame.cursors.load_xbm('cursor.xbm','cursor_mask.xbm'))

    def simple_lights(self):
        glEnable(GL_LIGHTING)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.9, 0.45, 0.0, 1.0))
        glLightfv(GL_LIGHT0, GL_POSITION, (0.0, 10.0, 10.0, 10.0))
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)
            
    def simple_camera_pose(self):
        """ Pre-position the camera (optional) """
        glMatrixMode(GL_MODELVIEW)
        glLoadMatrixf(numpy.array([0.741,-0.365,0.563,0,0,0.839,0.544,
            0,-0.671,-0.403,0.622,0,-0.649,1.72,-4.05,1]))

    def draw_mole(self, stal):
        """ Draw a simple object (optional) """
        for coord in stal:
            print coord
            glTranslatef(coord[0],coord[1],coord[2])
            print "Translating..."
            glutSolidSphere(0.25,32,32)
            print "Drawing"
        

    def loop(self):
        pygame.display.flip()
        pygame.event.pump()
        self.keys = dict((chr(i),int(v)) for i,v in \
            enumerate(pygame.key.get_pressed()) if i<256)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        return True

    def controls_3d(self,mouse_button=1,w_key='w',s_key='s',a_key='a',d_key='d',q_key='q',e_key='e'):
        """ The actual camera setting cycle """
        mouse_dx,mouse_dy = pygame.mouse.get_rel()
        if pygame.mouse.get_pressed()[mouse_button]:
            look_speed = 1
            buffer = glGetDoublev(GL_MODELVIEW_MATRIX)
            c = (-1 * numpy.mat(buffer[:3,:3]) * \
                numpy.mat(buffer[3,:3]).T).reshape(3,1)
            print c
            # c is camera center in absolute coordinates, 
            # we need to move it back to (0,0,0) 
            # before rotating the camera
            glTranslate(c[0],c[1],c[2])
            m = buffer.flatten()
            glRotate(mouse_dx * look_speed, m[1],m[5],m[9])
            glRotate(mouse_dy * look_speed, m[0],m[4],m[8])
            
            # compensate roll
            glRotated(-math.atan2(-m[4],m[5]) * \
                57.295779513082320876798154814105 ,m[2],m[6],m[10])
            glTranslate(-c[0],-c[1],-c[2])

        # move forward-back or right-left
        # fwd =   .1 if 'w' is pressed;   -0.1 if 's'
        key_speed = .001
        fwd = key_speed * (self.keys[w_key]-self.keys[s_key]) 
        strafe = key_speed * (self.keys[a_key]-self.keys[d_key])
        verti = key_speed * (self.keys[q_key]-self.keys[e_key])
        if abs(fwd) or abs(strafe) or abs(verti):
            m = glGetDoublev(GL_MODELVIEW_MATRIX).flatten()
            glTranslate(fwd*m[2],fwd*m[6],fwd*m[10])
            glTranslate(strafe*m[0],strafe*m[4],strafe*m[8])
            glTranslate(verti*m[1],verti*m[5],verti*m[9])

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
    forge = extStrip(fInput)
    print forge
    heckler = open(forge, "w")
    for lline in darter:
        print lline
    coordData = render.coords(darter)
    for atom in coordData:
        print atom
        print "Saving to text File"
        heckler.write(str(atom) + "\n")
    heckler.close()

if pInput == 'N':
    print "User has chosen not to continue"
    print "PDB Renderer will now exit"
    os.sys.exit()

print "Data ready!"
cInput = raw_input("Continue?(y/n)")

if pInput == 'Y':
    #width = int(raw_input('Please enter a window width:'))
    #height = int(raw_input('Please enter a window height:'))
    print "PDB Renderer will now render the data"
    print "Close window to exit!"
    fps = Spectator(1280, 750, 115)
    fps.simple_lights()
    fps.simple_camera_pose()
    fps.draw_mole(coordData)
    fps.simple_camera_pose()
    while fps.loop():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                os.sys.exit()
            if event.type != pygame.QUIT:
                print event
                break
        fps.controls_3d(0,'w','s','a','d','q','e')

if pInput == 'N':
    print "User has chosen not to continue"
    print "PDB Renderer will now exit"
    os.sys.exit()

        
        
        