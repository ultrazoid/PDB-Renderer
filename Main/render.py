'''
Created on Sep 28, 2012

@author: emerson
'''
#OpenGL imports
from OpenGLContext import testingcontext
from OpenGL.GL import *
from OpenGL.arrays import vbo
from OpenGLContext.arrays import *
from OpenGL.GL import shaders
from OpenGL.GLUT import *
from OpenGL.GLU import *
#Array imports
from numpy import *
from numpy import append
#Self defined Variable imports
import data
import la 
#BaseContext Definition
BaseContext = testingcontext.getInteractive()

class TestContext( BaseContext ):
    """Creates a simple vertex shader..."""
    def OnInit( self):
        Datlocal = open('swamp.txt','r')
        name = Datlocal.read(8)
        lake = data.get(name)
        laker = data.clean(lake)
        dat = coords(laker)
        datas = array(dat)
        print datas
        raw_input("wait:")
        VERTEX_SHADER = shaders.compileShader("""
        void main() {
            gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
        }""", GL_VERTEX_SHADER)
        FRAGMENT_SHADER = shaders.compileShader("""
        void main() {
            gl_FragColor = vec4( 0, 1, 0, 1 );
        }""", GL_FRAGMENT_SHADER)
        self.shader = shaders.compileProgram(VERTEX_SHADER,FRAGMENT_SHADER)
        self.vbo = vbo.VBO(
            array( datas,'f')
        )
    def Render( self, mode):
        """Render the geometry for the scene."""
        shaders.glUseProgram(self.shader)
        glutReshapeWindow( 512 , 512 )
        testcontext.ViewPlatform.setPosition(self, [0,0,512])
        try:
            self.vbo.bind()
            try:
                quad = gluNewQuadric()
                glEnableClientState(GL_VERTEX_ARRAY);
                glVertexPointerf( self.vbo )
                glDrawArrays(glusphere(quad,1,5,5), 0, len(self.vbo))
            finally:
                self.vbo.unbind()
                glDisableClientState(GL_VERTEX_ARRAY);
        finally:
            shaders.glUseProgram( 0 )
            
def draw():
    la.run

def coords(dat):
    coordss = array([[0.0,0.0,0.0]])
    index = 0
    for i in dat:
        drawDict = []
        niek = list(i)
        #x coord grab
        cont = False
        niez = ''
        ind = 30
        while cont==False:
            while ind in range(30,38):                
                nies = niek[ind]
                if nies == '':
                    niez = niez
                elif nies != '':
                    niez += nies
                ind += 1
            drawDict.insert(0,float(niez))
            cont = True
        #y coord grab
        cont = False
        niez = ''
        ind = 38
        while cont==False:
            while ind in range(38,46):                
                nies = niek[ind]
                if nies == '':
                    niez = niez
                elif nies != '':
                    niez += nies
                ind += 1
            drawDict.insert(1,float(niez))
            cont = True
        #z coord grab
        cont = False
        niez = ''
        ind = 46
        while cont==False:
            while ind in range(46,54):                
                nies = niek[ind]
                if nies == '':
                    niez = niez
                elif nies != '':
                    niez += nies
                ind += 1
            drawDict.insert(2,float(niez))
            cont = True
        coordss = append(coordss,[drawDict],axis=0)
        index += 1
        '''
        print drawDict
        print coordss
        raw_input('wait:')
        '''
    return coordss