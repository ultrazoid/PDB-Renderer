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
from numpy import *
#BaseContext Definition
BaseContext = testingcontext.getInteractive()

class TestContext( BaseContext ):
    """Creates a simple vertex shader..."""
    def OnInit( self , dat):
        datas = array(dat)
        VERTEX_SHADER = shaders.compileShader("""#version 330
        void main() {
            gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
        }""", GL_VERTEX_SHADER)
        FRAGMENT_SHADER = shaders.compileShader("""#version 330
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
        try:
            self.vbo.bind()
            try:
                glEnableClientState(GL_VERTEX_ARRAY);
                glVertexPointerf( self.vbo )
                glDrawArrays(GL_SPHERES, 0, 9)
            finally:
                self.vbo.unbind()
                glDisableClientState(GL_VERTEX_ARRAY);
        finally:
            shaders.glUseProgram( 0 )
            
def draw(dat):
    TestContext.ContextMainLoop(dat)

def coords(dat):
    coordss = []
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
        coordss.insert(index,drawDict)
        index += 1
    print coordss
    raw_input('wait:')
    return coordss