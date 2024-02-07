from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math


def drawCircle(cx, cy, radius, num_segments):
    glBegin(GL_TRIANGLE_FAN)
    for i in range(num_segments):
        theta = 2.0 * math.pi * i / num_segments
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        glVertex2f(cx + x, cy + y)
    glEnd()


def drawHouse():
    # Draw the base of the house
    glBegin(GL_QUADS)
    glColor3f(0.79, 0.76, 0.89)  # Gray color
    glVertex2f(-1.0, -1.0)
    glVertex2f(1.0, -1.0)
    glVertex2f(1.0, 1.0)
    glVertex2f(-1.0, 1.0)
    glEnd()

    # Draw the roof
    glBegin(GL_TRIANGLES)
    glColor3f(0.58, 0.29, 0)  # Brown color
    glVertex2f(-1.2, 1.0)
    glVertex2f(1.2, 1.0)
    glVertex2f(0.0, 2.0)
    glEnd()

    # Draw the door
    glBegin(GL_QUADS)
    glColor3f(0.58, 0.29, 0.2)  # Different Brown color
    glVertex2f(-0.2, -1.0)
    glVertex2f(0.2, -1.0)
    glVertex2f(0.2, 0.0)
    glVertex2f(-0.2, 0.0)
    glEnd()

    # Draw the circular windows
    glColor3f(0.53, 0.81, 0.94)  # Light grey
    drawCircle(0.0, 0.6, 0.2, 100)  # window

    glBegin(GL_POINTS)
    glColor3f(0.58, 0.29, 0)  # Brown color
    for i in range(200):
        theta = 2.0 * math.pi * i / 200
        x = 0.21 * math.cos(theta)
        y = 0.21 * math.sin(theta)
        glVertex2f(x, 0.6 + y)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2f(0, 0.8)
    glVertex2f(0, 0.4)

    glVertex2f(0.2, 0.6)
    glVertex2f(-0.2, 0.6)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # Draw the house
    drawHouse()

    glFlush()


def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-2.0, 2.0, -2.0, 2.0)
    glMatrixMode(GL_MODELVIEW)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"House with Circular Windows")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set background color to white

    glutMainLoop()


if __name__ == "__main__":
    main()
