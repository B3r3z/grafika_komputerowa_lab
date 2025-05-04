import pygame
from mesh3D import *
from cube import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from lab4.Object import *
from transform import *
pygame.init()
clock =pygame.time.Clock()
fps = 24
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')

glEnable(GL_DEPTH_TEST)  # Włącz test głębi
glEnable(GL_LIGHTING)    # Włącz oświetlenie
glEnable(GL_LIGHT0)      # Aktywacja pierwszego światła
glEnable(GL_COLOR_MATERIAL)
# Konfiguracja światła
glLightfv(GL_LIGHT0, GL_POSITION, (5, 5, 5, 1))
glLightfv(GL_LIGHT0, GL_AMBIENT,  (0.1, 0.1, 0.1, 1))
glLightfv(GL_LIGHT0, GL_DIFFUSE,  (1, 1, 1, 1))
glLightfv(GL_LIGHT0, GL_SPECULAR, (1, 1, 1, 1))

# Konfiguracja macierzy
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, float(screen_width) / screen_height, 0.1, 100.0)

glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
glTranslatef(0.0, 0.0, -4)

#mesh = Cube(GL_POLYGON, "lab2b/lena.png")
mesh = Object("Cube") #nowy obiekt "Cube"
mesh.add_component(Transform((0,0,-1)))
mesh.add_component(Cube(GL_POLYGON,"lab2b/lena.png"))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Konfiguracja materiału obiektu
    glMaterialfv(GL_FRONT, GL_AMBIENT, (0.2, 0.2, 0.2, 1))
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.8, 0.0, 0.0, 1))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (1, 1, 1, 1))
    glMaterialf(GL_FRONT, GL_SHININESS, 50.0)

    glRotatef(1, 1, 0.5, 0)
    #mesh.draw()
    mesh.update()
    pygame.time.wait(50)
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
