import pygame
from mesh3D import *
from cube import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Object import *
from transform import *

pygame.init()
clock = pygame.time.Clock()
fps = 24
screen_width = 500
screen_height = 500
angle1 = 0.0
angle2 = 0.0
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')

glEnable(GL_DEPTH_TEST)  # Włącz test głębi
glEnable(GL_LIGHTING)    # Włącz oświetlenie
glEnable(GL_LIGHT0)      # Aktywacja pierwszego światła
glEnable(GL_COLOR_MATERIAL)

# Konfiguracja światła
glLightfv(GL_LIGHT0, GL_POSITION, (5, 5, 5, 0))
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


#mesh = Object("Cube_1")
#mesh.add_component(Transform((0, 0, -1)))  # Pozycja pierwszego obiektu
#mesh.add_component(Cube(GL_POLYGON, "lab2b/lena.png"))
#
#mesh2 = Object("Cube_2")
#mesh2.add_component(Transform((1.5, 0, -1)))  # Przesunięcie drugiego obiektu w bok
#mesh2.add_component(Cube(GL_POLYGON, "lab2b/lena.png"))

mesh = Object("Cube_1")
transform1 = Transform(position=(0,0,-1), rotation=(0,0,0))
mesh.add_component(transform1)
mesh.add_component(Cube(GL_POLYGON, "lab2b/lena.png"))

mesh2 = Object("Cube_2")
transform2 = Transform(position=(1.5,0,-1), rotation=(0,0,0))
mesh2.add_component(transform2)
mesh2.add_component(Cube(GL_POLYGON, "lab2b/baboonC.png"))



done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMaterialfv(GL_FRONT, GL_AMBIENT, (0.2, 0.2, 0.2, 1))
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.8, 0.0, 0.0, 1))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (1, 1, 1, 1))
    glMaterialf(GL_FRONT, GL_SHININESS, 50.0)

    angle1+= 1
    angle2+= 2
    transform1.rotation.y = angle1
    transform2.rotation.x = angle2
    mesh.update()
    mesh2.update()

    #pygame.time.wait(50)
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()