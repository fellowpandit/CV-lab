## 2D  and 3D image rotating

import cv2
import numpy as np

# Load an image
image = cv2.imread('image.png')

# Get image dimensions
height, width = image.shape[:2]

# Define the rotation angle in degrees
angle = 45

# Calculate the rotation matrix
rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)

# Apply the rotation to the image
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

# Display the original and rotated images
cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

angle = 0.0  # Initial rotation angle
rotation_speed = 2.0  # Speed of rotation

def draw_cube():
    glBegin(GL_QUADS)
    
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(-1, 1, -1)

    glEnd()

def display():
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glRotatef(angle, 1, 1, 0)  # Rotate around the x and y axes

    draw_cube()

    glutSwapBuffers()

def update_rotations(value):
    global angle
    angle += rotation_speed
    glutPostRedisplay()
    glutTimerFunc(16, update_rotations, 0)  # Update every 16 milliseconds
    
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
    glutCreateWindow(b"Rotating 3D Cube")

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_COLOR_MATERIAL)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, 1, 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(3, 3, 5, 0, 0, 0, 0, 1, 0)

    glutReshapeFunc(myReshape)
    glutDisplayFunc(display)
    glutTimerFunc(16, update_rotations, 0)  # Start the rotation timer

    glutMainLoop()

if __name__ == "__main__":
    main()
