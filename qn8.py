from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import sys

vertices = np.array(
    [
        -1.0,
        -1.0,
        -1.0,
        1.0,
        -1.0,
        -1.0,
        1.0,
        1.0,
        -1.0,
        -1.0,
        1.0,
        -1.0,
        -1.0,
        -1.0,
        1.0,
        1.0,
        -1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        -1.0,
        1.0,
        1.0,
    ],
    dtype=np.float32,
)


normals = np.array(
    [
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
    ],
    dtype=np.float32,
)


colors = np.array(
    [
        0.0,
        0.0,
        0.0,
        1.0,
        0.0,
        0.0,
        1.0,
        1.0,
        0.0,
        0.0,
        1.0,
        0.0,
        0.0,
        0.0,
        1.0,
        1.0,
        0.0,
        1.0,
        1.0,
        1.0,
        1.0,
        0.0,
        1.0,
        1.0,
    ],
    dtype=np.float32,
)

cubeIndices = np.array(
    [0, 3, 2, 1, 2, 3, 7, 6, 0, 4, 7, 3, 1, 2, 6, 5, 4, 5, 6, 7, 0, 1, 5, 4],
    dtype=np.uint8,
)

theta = [0.0, 0.0, 0.0]
axis = 2


def draw():
    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_COLOR_ARRAY)
    glEnableClientState(GL_NORMAL_ARRAY)

    glVertexPointer(3, GL_FLOAT, 0, vertices)
    glColorPointer(3, GL_FLOAT, 0, colors)
    glNormalPointer(GL_FLOAT, 0, normals)
    glDrawElements(GL_QUADS, 24, GL_UNSIGNED_BYTE, cubeIndices)

    glDisableClientState(GL_NORMAL_ARRAY)
    glDisableClientState(GL_COLOR_ARRAY)
    glDisableClientState(GL_VERTEX_ARRAY)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glRotatef(theta[0], 1.0, 0.0, 0.0)
    glRotatef(theta[1], 0.0, 1.0, 0.0)
    glRotatef(theta[2], 0.0, 0.0, 1.0)
    draw()

    glBegin(GL_LINES)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(1.0, 1.0, 1.0)
    glEnd()

    glFlush()
    glutSwapBuffers()


def spinCube():
    global theta, axis
    theta[axis] += 0.1
    if theta[axis] > 360.0:
        theta[axis] -= 360.0
    glutPostRedisplay()


def mouse(btn, state, x, y):
    global axis
    if btn == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        axis = 0
    if btn == GLUT_MIDDLE_BUTTON and state == GLUT_DOWN:
        axis = 1
    if btn == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        axis = 2


def myReshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    if w <= h:
        glOrtho(-2.0, 2.0, -2.0 * h / w, 2.0 * h / w, -10.0, 10.0)
    else:
        glOrtho(-2.0 * w / h, 2.0 * w / h, -2.0, 2.0, -10.0, 10.0)

    glMatrixMode(GL_MODELVIEW)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Spinning color cube")

    glutReshapeFunc(myReshape)
    glutDisplayFunc(display)
    glutIdleFunc(spinCube)
    glutMouseFunc(mouse)

    glEnable(GL_DEPTH_TEST)
    glEnableClientState(GL_COLOR_ARRAY)
    glEnableClientState(GL_NORMAL_ARRAY)
    glEnableClientState(GL_VERTEX_ARRAY)
    glColorPointer(3, GL_FLOAT, 0, colors)

    glutMainLoop()


main()
