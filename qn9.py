from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def circle(rx, ry, cx, cy):
    glBegin(GL_POLYGON)
    glVertex2f(cx, cy)
    for i in range(361):
        angle = i * math.pi / 180
        x = rx * math.cos(angle)
        y = ry * math.sin(angle)
        glVertex2f(x + cx, y + cy)
    glEnd()

def sun(rx, ry, cx, cy):
    glColor3ub(255, 215, 0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(cx, cy)
    for i in range(361):
        angle = 2 * i * math.pi / 180
        x = rx * math.cos(angle)
        y = ry * math.sin(angle)
        glVertex2f(x + cx, y + cy)
    glEnd()


def hills():
    # Hills 1
    glColor3ub(184, 134, 11)
    glBegin(GL_POLYGON)
    glVertex2d(-40, 300)
    glVertex2d(200, 300)
    glVertex2d(100, 450)
    glEnd()

    # Hills 2
    glColor3ub(218, 165, 32)
    glBegin(GL_POLYGON)
    glVertex2d(150, 300)
    glVertex2d(350, 300)
    glVertex2d(250, 450)
    glEnd()

    # Hills 3
    glColor3ub(184, 134, 11)
    glBegin(GL_POLYGON)
    glVertex2d(300, 300)
    glVertex2d(520, 300)
    glVertex2d(400, 450)
    glEnd()

def car():
    global bx
    
    glPushMatrix()
    glTranslatef(bx, 0, 0)
    # Car body
    glColor3ub(255, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2d(410, 100)
    glVertex2d(490, 100)
    glVertex2d(485, 130)
    glVertex2d(410, 130)
    glEnd()

    glColor3ub(255, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2d(420, 130)
    glVertex2d(475, 130)
    glVertex2d(465, 160)
    glVertex2d(430, 160)
    glEnd()

    # Car window
    glColor3ub(220, 220, 220)
    glBegin(GL_POLYGON)
    glVertex2d(425, 130)
    glVertex2d(445, 130)
    glVertex2d(445, 150)
    glVertex2d(430, 150)
    glEnd()

    glColor3ub(220, 220, 220)
    glBegin(GL_POLYGON)
    glVertex2d(450, 130)
    glVertex2d(470, 130)
    glVertex2d(465, 150)
    glVertex2d(450, 150)
    glEnd()

    # Car wheels
    glColor3ub(0, 0, 0)
    circle(10, 14, 435, 100)
    circle(10, 14, 465, 100)

    glColor3ub(245, 245, 245)
    circle(6, 10, 435, 100)
    circle(6, 10, 465, 100)

    glPopMatrix()

    bx += .5
    if bx > 0:
        bx = -500
    glutPostRedisplay()

def display():
    global bx
    glClear(GL_COLOR_BUFFER_BIT)

    # Ground Color
    glColor3ub(0, 240, 50)
    glBegin(GL_POLYGON)
    glVertex2d(0, 0)
    glVertex2d(500, 0)
    glVertex2d(500, 150)
    glVertex2d(0, 150)
    glEnd()

    # Road
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2d(0, 55)
    glVertex2d(500, 55)
    glVertex2d(500, 115)
    glVertex2d(0, 115)
    glEnd()

    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2d(0, 60)
    glVertex2d(500, 60)
    glVertex2d(500, 110)
    glVertex2d(0, 110)
    glEnd()

    # Hills
    hills()

    # Sun
    sun(20, 20, 175, 450)

    car()

    glutSwapBuffers()

def init():
    glClearColor(0.0, 0.0, 0.9, 0.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0.0, 500, 0.0, 500)  # window size

bx = 10

def main():
    global bx
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(1000, 700)
    glutInitWindowPosition(300, 50)
    glutCreateWindow(b"A Moving Car Scenario")
    init()
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutMainLoop()

main()
