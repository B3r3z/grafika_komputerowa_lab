from pygame.locals import DOUBLEBUF, OPENGL, QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_ESCAPE, K_SPACE
from OpenGL.GL import glMatrixMode, glLoadIdentity, glViewport, glDisable, glEnable, glClear, GL_PROJECTION, GL_MODELVIEW, GL_DEPTH_TEST, GL_TEXTURE_2D, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, GL_POLYGON, glColor3f, glPushMatrix, glPopMatrix
from OpenGL.GLU import gluOrtho2D, gluPerspective, gluLookAt
from Object import Object
from Cube import Cube
from Button import Button
from Settings import window_width, window_height, gui_width, gui_height
from Transform import Transform
import os
import pygame
from Grid import *
from DisplayNormals import *  # import DisplayNormals helper



# --- Inicjalizacja Pygame i okna OpenGL ---
pygame.init()
pygame.display.set_caption('OpenGL w Pythonie - Przycisk i Klawiatura')
screen = pygame.display.set_mode((window_width, window_height), DOUBLEBUF | OPENGL)

done = False
objects_3d = []
objects_2d = []

# --- Obsługa ścieżki do tekstury ---
texture_path = os.path.join("..", "lab2b", "lena.png")
if not os.path.exists(texture_path):
    texture_path = os.path.join("lab2b", "lena.png")
if not os.path.exists(texture_path):
    print(f"Warning: Texture file not found at {texture_path} or alternate.")
    texture_path = None  # Brak tekstury, obsłuż w Cube/Mesh3D

# --- Tworzenie obiektu 3D (kostka) ---
cube = Object("Cube")
cube.add_component(Transform((0, 0, -5), (0, 0, 15), (1, 1, 1))) # Transformacja: pozycja, rotacja, skala
cube.add_component(Cube(GL_POLYGON, texture_path))

cube2 = Object("Cube")
cube2.add_component(Transform((0, 2.5 , -5))) # Transformacja: pozycja, rotacja, skala
cube2.add_component(Cube(GL_POLYGON, texture_path))
cube.add_component(DisplayNormals(cube.get_component(Cube).vertices, 
                                   cube.get_component(Cube).triangles)) # Dodanie komponentu DisplayNormals do drugiej kostki

# ----inicjalizacja i ryspwanie sitki ---
grid = Object("Grid")
grid.add_component(Transform((0,0,-5))) #
grid.add_component(Grid(0.5 ,8,(255,0,255))) #siatka z odstepem 0.5, sakala 10, kolor
objects_3d.append(grid)
objects_3d.append(cube)
objects_3d.append(cube2)

clock = pygame.time.Clock()
fps = 30
move_speed = 0.1  # Szybkość przesuwania kostki

# ustaw viewport wg rzeczywistego rozmiaru okna
glViewport(0, 0, screen.get_width(), screen.get_height())
glEnable(GL_DEPTH_TEST)

# przygotowanie animacji kostki
trans: Transform = cube.get_component(Transform)
trans2: Transform = cube2.get_component(Transform)
start_position = pygame.math.Vector3(-3, 0, -5)
end_position   = pygame.math.Vector3( 3, 0, -5)
v = end_position - start_position
t = 0.0
dt = 0
animating = True
trans.set_position(start_position)

# --- Funkcja ustawiająca rzutowanie 2D ---
def set_2d():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, gui_width, 0, gui_height)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glViewport(0, 0, window_width, window_height)
    glDisable(GL_DEPTH_TEST)
    glDisable(GL_TEXTURE_2D)

# --- Funkcja ustawiająca rzutowanie 3D ---
def set_3d():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (window_width / window_height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    # Camera at (0, 2, 0), looking at (0, 0, -5), with Up vector (0, 1, 0)
#    gluLookAt(0, 2, 0,  # Eye position (slightly above the origin)
#              0, 0, -5, # Target position (where the grid/cube center is)
#              0, 1, 0)  # Up vector (positive Y is up)
    gluLookAt(0, 0, 5, 
             0, 0, 0,
             0, 1, 0)
    glViewport(0, 0, window_width, window_height)
    glEnable(GL_DEPTH_TEST)

# --- Pętla główna programu ---
while not done:
    events = pygame.event.get()

    # --- Obsługa zdarzeń klawiatury (tryb event-based) ---
    for event in events:
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN:
            trans: Transform = cube.get_component(Transform)
            if trans is not None:
                if event.key == K_LEFT:
                    trans.move_x(-move_speed)
                elif event.key == K_RIGHT:
                    trans.move_x(move_speed)
                elif event.key == K_UP:
                    trans.move_y(move_speed)
                elif event.key == K_DOWN:
                    trans.move_y(-move_speed)
                elif event.key == K_SPACE: # 
                    trans.move(pygame.math.Vector3(0.5, 0,0))
                

            if event.key == K_ESCAPE:
                done = True
    # --- Możliwa alternatywa: obsługa ciągłego wciśnięcia klawiszy ---
    # keys = pygame.key.get_pressed()
    # trans: Transform = cube.get_component(Transform)
    # if trans is not None:
    #     if keys[K_LEFT]:
    #         trans.move_x(-move_speed)
    #     if keys[K_RIGHT]:
    #         trans.move_x(move_speed)
    #     if keys[K_UP]:
    #         trans.move_y(move_speed)
    #     if keys[K_DOWN]:
    #         trans.move_y(-move_speed)
    # if keys[K_ESCAPE]:
    #     done = True

    # animacja: przesuń kostkę od start do end
    if animating and t <= 1.0:
        trans.set_position(start_position + t * v)
        t += 0.0001 * dt

    glPushMatrix()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # --- Renderowanie sceny 3D ---
    set_3d()
    for o in objects_3d:
        o.update(events)
        # Reset color to white after each object is drawn
        glColor3f(1.0, 1.0, 1.0)

    glPopMatrix()

    # --- Renderowanie GUI 2D ---
    set_2d()
    for o in objects_2d:
        o.update(events)

    pygame.display.flip()
    dt = clock.tick(fps)

# --- Zakończenie programu ---
pygame.quit()