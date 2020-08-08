import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
vertices = ((-1, 1, -1), (-1, 1, 1), (1, 1, 1), (1, 1, -1), (-1, -1, -1), (-1, -1, 1), (1, -1, 1),
            (1, -1, -1))

edges = ((0, 1), (0, 3), (0, 4), (2, 1), (2, 3), (2, 6), (5, 1), (5, 4), (5, 6), (7, 3), (7, 4), (7, 6))


def cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, display[0] / display[1], 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()
