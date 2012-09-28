'''
Created on Sep 28, 2012

@author: emerson
'''
#OpenGL imports
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

name = 'ball_glut'

def main(dat):
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(600,600)
    glutCreateWindow(name)

    glClearColor(0.,0.,0.,1.)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    lightZeroPosition = [10.,4.,10.,1.]
    lightZeroColor = [0.8,1.0,0.8,1.0] #green tinged
    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
    glEnable(GL_LIGHT0)
    glutDisplayFunc(display(dat))
    glMatrixMode(GL_PROJECTION)
    gluPerspective(40.,1.,1.,40.)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0,0,10,
              0,0,0,
              0,1,0)
    glPushMatrix()
    glutMainLoop()
    return

def display(dat):
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    color = [1.0,0.,0.,1.]
    glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
    for i in dat:
        drawDict = {}
        niek = list(i)
        #x coord grab
        x = 19
        cont = False
        while cont==False:
            if niek[x] == '':
                x -= 1
            if niek[x] != '':
                drawDict['x'] = float(niek[x])
                cont = True
        #y coord grab
        x = 22
        cont = False
        while cont==False:
            if niek[x] == '':
                x -= 1
            if niek[x] != '':
                drawDict['y'] = float(niek[x])
                cont = True
        #z coord grab
        x = 24
        cont = False
        while cont==False:
            if niek[x] == '':
                x -= 1
            if niek[x] != '':
                drawDict['z'] = float(niek[x])
                cont = True
        print niek
        print drawDict
        #transform to coords
        glTranslatef(drawDict['x'],drawDict['y'],drawDict['z'])
        glutSolidSphere(0.25,20,20)
    glPopMatrix()
    glutSwapBuffers()
    return

def draw(dat): 
    main(dat)