from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import sys
import cv2

# Function to draw a cube
def draw_cube():
    glutWireCube(1)

# Function to draw a sphere
def draw_sphere():
    glutWireSphere(0.5, 20, 20)

# Function to draw a cone
def draw_cone():
    glutWireCone(0.5, 1, 20, 20)

# Function to display the scene
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glLoadIdentity()
    gluLookAt(3, 3, 3, 0, 0, 0, 0, 1, 0)
    
    glColor3f(1, 0, 0)  # Set color to red
    glTranslatef(-1.5, 0, 0)  # Translate to the left
    draw_cube()

    glColor3f(0, 1, 0)  # Set color to green
    glTranslatef(3, 0, 0)  # Translate to the right
    draw_sphere()

    glColor3f(0, 0, 1)  # Set color to blue
    glTranslatef(-1.0, 0, 1)  # Translate forward and up
    draw_cone()

    glutSwapBuffers()

# Initialize OpenGL parameters
def init():
    glClearColor(0, 0, 0, 1)
    glEnable(GL_DEPTH_TEST)

# Function to handle window resizing
def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (width / height), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

# Capture OpenGL rendering to an OpenCV image
def capture_opengl_to_opencv(width, height):
    glReadBuffer(GL_FRONT)
    pixels = glReadPixels(0, 0, width, height, GL_BGR, GL_UNSIGNED_BYTE)
    image = np.frombuffer(pixels, dtype=np.uint8)
    image = image.reshape((height, width, 3))
    return cv2.flip(image, 0)

# Main function
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(800, 800)
    glutCreateWindow("3D Objects using OpenGL")

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    init()

    # Run the OpenGL loop
    glutMainLoop()

    # Capture the OpenGL rendering to an OpenCV image
    width, height = glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT)
    opengl_image = capture_opengl_to_opencv(width, height)

    # Display the captured image using OpenCV
    cv2.imshow("OpenGL Rendering", opengl_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

