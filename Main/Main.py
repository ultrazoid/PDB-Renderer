'''
PDB RENDERER MAC OS X EDITION
Created on Sep 28, 2012

@author: emerson
'''
from __future__ import division
from __future__ import print_function

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
import sys

def extStrip(pdb):
    heck = pdb
    mid = heck[:-4]
    print(mid)
    new = mid + ".obj"
    print(new)
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
            print(coord)
            glTranslatef(coord[0],coord[1],coord[2])
            print("Translating...")
            glutSolidSphere(0.25,32,32)
            print("Drawing")
        

    def loop(self):
        pygame.display.flip()
        pygame.event.pump()
        self.keys = dict((chr(i),int(v)) for i,v in \
            enumerate(pygame.key.get_pressed()) if i<256)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        return True

    def controls_3d(self,mouse_button, w_key, s_key, a_key, d_key, q_key, e_key, cameraView):
        """ The actual camera setting cycle """
        mouse_dx,mouse_dy = pygame.mouse.get_rel()
        if pygame.mouse.get_pressed()[mouse_button]:
            look_speed = 1
            
            # c is camera center in absolute coordinates, 
            # we need to move it back to (0,0,0) 
            # before rotating the camera
            glTranslate(cameraView[0],cameraView[1],cameraView[2])
            m = buffer.flatten()
            glRotate(mouse_dx * look_speed, m[1],m[5],m[9])
            glRotate(mouse_dy * look_speed, m[0],m[4],m[8])
            
            # compensate roll
            glRotated(-math.atan2(-m[4],m[5]) * \
                57.295779513082320876798154814105 ,m[2],m[6],m[10])
            glTranslate(-cameraView[0],-cameraView[1],-cameraView[2])

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

def print_vertex(v,ff):
    print("v {} {} {}".format(v[0], v[1], v[2]), file=ff)
    print_vertex.count += 1
    return print_vertex.count
print_vertex.count = 0
 
def print_normal(v,ff):
    print("vn {} {} {}".format(v[0], v[1], v[2]), file=ff)
    print_normal.count += 1
    return print_normal.count
print_normal.count = 0
 
def print_face(vertices, norm,ff):
    out = "f"
    for v in vertices:
        out += " {}//{}".format(v, norm)
    print(out, file=ff)
 

 
def cube(x, y, z, size, ff):
    ftr = print_vertex((x + size, y + size, z - size), ff)
    ftl = print_vertex((x - size, y + size, z - size), ff)
    fbr = print_vertex((x + size, y - size, z - size), ff)
    fbl = print_vertex((x - size, y - size, z - size), ff)
    btr = print_vertex((x + size, y + size, z + size), ff)
    btl = print_vertex((x - size, y + size, z + size), ff)
    bbr = print_vertex((x + size, y - size, z + size), ff)
    bbl = print_vertex((x - size, y - size, z + size), ff)
 
    # front
    print_face([ftl, ftr, fbr], front, ff)
    print_face([ftl, fbr, fbl], front, ff)
    # back
    print_face([btr, btl, bbl], back, ff)
    print_face([btr, bbl, bbr], back, ff)
    # left
    print_face([btl, ftl, fbl], left, ff)
    print_face([btl, fbl, bbl], left, ff)
    # right
    print_face([ftr, btr, bbr], right, ff)
    print_face([ftr, bbr, fbr], right, ff)
    # top
    print_face([ftl, btr, ftr], top, ff)
    print_face([ftl, btl, btr], top, ff)
    # bottom
    print_face([fbl, fbr, bbr], back, ff)
    print_face([fbl, bbr, bbl], back, ff)


print("Welcome to ultrazoid_'s PDB renderer: Mac OS X Edition")

cont = False
while cont == False:
    fInput = string.upper(raw_input("Please input the *.pdb file name you would like to render(must be in same directory):"))
    if ".PDB" in fInput:
        try:
            print("*.pdb file recognised")
            print("searching for file...")
            dart = data.get(fInput)
            cont = True
        except IOError:
            print("File not found...")
            print("Did you misspell the name?")
            cont = False
    elif ".PDB" not in fInput:
        print("The filename you entered is not a PDB file...")
        print("Did you forget about the extension?")
        cont = False

pInput = string.upper(raw_input("File Loaded! Would you like to prepare it for rendering?(y/n)"))
if pInput == 'Y':
    cont = False
    while cont == False:
        numInput = str(raw_input("Please input point size as a float less than 1:"))
        if "0." in numInput:
            print("Size recognised")
            cont = True
        elif "0." not in numInput:
            print("You didn't enter a float less than 1. Try Again")
            cont = False
    sizeConv = float(numInput)
    print("PDB Renderer will now prepare the data")
    darter = data.clean(dart)
    forge = extStrip(fInput)
    print(forge)
    heckler = open(forge, "w")
    top = print_normal((0, 1, 0), heckler)
    bottom = print_normal((0, -1, 0), heckler)
    left = print_normal((-1, 0, 0), heckler)
    right = print_normal((1, 0, 0), heckler)
    front = print_normal((0, 0, -1), heckler)
    back = print_normal((0, 0, 1), heckler)
    for lline in darter:
        print(lline)
    coordData = render.coords(darter)
    noot = []
    for atom in coordData:
        print(atom)
        print("Saving to obj File")
        noot.append(str(atom))
    for babe in noot:
        point = map(lambda x: float(x), babe[1:-2].split())
        cube(point[0], point[1], point[2], sizeConv, heckler)    
    heckler.close()

if pInput == 'N':
    print("User has chosen not to continue")
    print("PDB Renderer will now exit")
    os.sys.exit()

print("Data ready!")
cInput = raw_input("Continue?(y/n)")

if pInput == 'Y':
    #width = int(raw_input('Please enter a window width:'))
    #height = int(raw_input('Please enter a window height:'))
    print("PDB Renderer will now render the data")
    print("Close window to exit!")
    fps = Spectator(1280, 750, 115)
    fps.simple_lights()
    fps.simple_camera_pose()
    fps.draw_mole(coordData)
    fps.simple_camera_pose()
    buffer = glGetDoublev(GL_MODELVIEW_MATRIX)
    c = (-1 * numpy.mat(buffer[:3,:3]) * numpy.mat(buffer[3,:3]).T).reshape(3,1)
    while fps.loop():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                os.sys.exit()
            if event.type != pygame.QUIT:
                print(event)
                print(c)
                break
        fps.controls_3d(1,'w','s','a','d','q','e',c)

if pInput == 'N':
    print("User has chosen not to continue")
    print("PDB Renderer will now exit")
    os.sys.exit()

        
        
        