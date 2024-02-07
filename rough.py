from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import cos, sin, pi

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-20, 20, -20, 20)

def circle(rx, ry, cx, cy):
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(cx, cy)
    for i in range(101):
        angle = 2.0 * pi * i / 100
        x = rx * cos(angle)
        y = ry * sin(angle)
        glVertex2f(x + cx, y + cy)
    glEnd()

def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    
    glColor3f(1.0, 1.0, 0.0)
    circle(8, 8, 0, 0)

    glColor3f(0.0, 0.0, 0.0)
    circle(4, 4, 0, -1)

    glColor3f(1.0, 1.0, 0.0)
    circle(4, 4, 0, 0)

    glColor3f(0.0, 0.0, 0.0)
    circle(1, 1, -2, 3)

    glColor3f(0.0, 0.0, 0.0)
    circle(1, 1, 2, 3)

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(50, 100)
    glutInitWindowSize(400, 300)
    glutCreateWindow(b"simple emoji")
    init()
    glutDisplayFunc(myDisplay)
    glutMainLoop()

if __name__ == "__main__":
    main()
