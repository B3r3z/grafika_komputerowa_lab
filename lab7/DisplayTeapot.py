# --- Importy ---
# Unikaj import * dla lepszej czytelności i unikania konfliktów nazw
from pygame.locals import DOUBLEBUF, OPENGL, QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_ESCAPE
from OpenGL.GL import glMatrixMode, glLoadIdentity, glViewport, glDisable, glEnable, glClear, GL_PROJECTION, GL_MODELVIEW, GL_DEPTH_TEST, GL_TEXTURE_2D, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, GL_POLYGON
from OpenGL.GLU import gluOrtho2D, gluPerspective
from Object import Object
from Cube import Cube
from Button import Button
from Settings import window_width, window_height, gui_width, gui_height
from Transform import Transform
import os
import pygame
from LoadMesh import *

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
cube.add_component(Transform((0, 0, -5)))
#cube.add_component(Cube(GL_POLYGON, texture_path))

#cube.add_component(LoadMesh(GL_LINE_LOOP, os.path.join("models", "teapot.obj")))
cube.add_component(LoadMesh(GL_TRIANGLES, os.path.join("models", "teapot.obj")))
objects_3d.append(cube)

# --- Definicje kolorów (pygame.Color) ---
myWhite = pygame.Color(255, 255, 255)
myGreen = pygame.Color(0, 255, 0)
myRed = pygame.Color(255, 0, 0)
myBlue = pygame.Color(0, 0, 255)
myYellow = pygame.Color(255, 255, 0)

# --- Callback przycisku ---
def button_click_action():
    print("Hello Button")

# --- Tworzenie przycisku 2D ---
button1 = Object("Button1")
button1.add_component(Button(screen, (50, 50), 100, 30,
                            myGreen,  # Kolor normalny
                            myYellow,  # Kolor po najechaniu
                            myRed,     # Kolor po kliknięciu
                            button_click_action))
objects_2d.append(button1)

clock = pygame.time.Clock()
fps = 30
move_speed = 0.1  # Szybkość przesuwania kostki

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

    # --- Czyszczenie buforów ---
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # --- Renderowanie sceny 3D ---
    set_3d()
    for o in objects_3d:
        o.update(events)

    # --- Renderowanie GUI 2D ---
    set_2d()
    for o in objects_2d:
        o.update(events)

    pygame.display.flip()
    clock.tick(fps)

# --- Zakończenie programu ---
pygame.quit()