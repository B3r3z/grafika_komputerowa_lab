import pygame
from mesh3D import *  # Importujemy naszą klasę Mesh3D z pliku Mesh3D.py
from cube import *
from pygame.locals import *
from OpenGL.GLU import *


pygame.init()  # Inicjujemy moduły Pygame

screen_width = 500
screen_height = 500
# Tworzymy okno 500×500 z trybem OpenGL i podwójnym buforowaniem
screen = pygame.display.set_mode((screen_width,
                                  screen_height),
                                  DOUBLEBUF|OPENGL)
pygame.display.set_caption('OpenGL in Python')
done = False
white = pygame.Color(255, 255, 255)
#OpenGL.gluPerspective(45,screen_width/screen_height, 0.1, 100.0)
#glMatrixMode(GL_PROJECTION)   # mówimy: "teraz modyfikuję macierz projekcji"
#glLoadIdentity()              # zerujemy macierz projekcji
gluPerspective(45, float(screen_width)/screen_height, 0.1, 100.0)
#glOrtho(-1, 1, 1, -1, 0.1, 50.0)
glTranslatef(0.0,0.0,-4)
#mesh = Mesh3D()  # Tworzymy obiekt siatki (mesh)
mesh = cube()
# Pętla główna aplikacjis
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  # Wyjście z pętli, gdy zamykamy okno

    # Czyścimy bufor koloru i bufor głębi
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glRotatef(1,1,0.5,0)
    mesh.draw()  # Wywołujemy metodę rysującą model
    pygame.time.wait(50)
    pygame.display.flip()  # Prezentujemy nowo narysowaną klatkę

pygame.quit()  # Sprzątanie i zakończenie programu
