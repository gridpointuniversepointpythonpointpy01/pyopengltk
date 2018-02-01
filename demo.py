
from __future__ import print_function

"""
entry point for Tkinter Window with OpenGL
"""

import sys
if sys.version_info[0] < 3 :
    from Tkinter import Tk, YES, BOTH
else:
    from tkinter import Tk, YES, BOTH

from pyopengltk import OpenGLFrame
import OpenGL.GL as GL
import OpenGL.GLU as GLU
import math, time

class AppOgl(OpenGLFrame):

    def initgl(self):
        GL.glViewport( 0, 0, self.width, self.height)
        GL.glClearColor(1.0,1.0,1.0,0.0)
        GL.glColor3f(0.0,0.0, 0.0)
        GL.glPointSize(4.0)
        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GLU.gluOrtho2D(-5,5,-5,5)
    

    def redraw(self):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        GL.glBegin(GL.GL_POINTS)
        npt = 100
        for i in range(npt):
            x = -5.0 + i*10.0/npt 
            y = math.sin(x+ time.time())*5/2
            GL.glVertex2f(x, y )
        GL.glEnd()
        GL.glFlush()

if __name__ == '__main__':
    root = Tk()
    app = AppOgl(root, width=320, height=200)
    app.pack(fill=BOTH, expand=YES)
    app.animate=10
    app.mainloop()
