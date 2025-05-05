import pygame
from pygame.math import Vector3
from OpenGL.GL import *

class Transform:
    def __init__(self, 
                 position=(0.0, 0.0, 0.0), 
                 rotation=(0.0, 0.0, 0.0), 
                 scale=(1.0, 1.0, 1.0)):
        # Ustawiamy parametry z użyciem setterów
        self.set_position(position)
        self.set_rotation(rotation)
        self.set_scale(scale)

    def set_position(self, position):
        self.position = Vector3(position)

    def get_position(self):
        return self.position

    def set_rotation(self, rotation):
        self.rotation = Vector3(rotation)

    def get_rotation(self):
        return self.rotation

    def set_scale(self, scale):
        self.scale = Vector3(scale)

    def get_scale(self):
        return self.scale

    def apply_transform(self):
        #"""
        #Aplikujemy transformacje w kontekście OpenGL:
        #1) Translacja
        #2) Rotacja (Euler: x, y, z)
        #3) Skalowanie
        #"""
        # 1) Translacja
        glTranslatef(self.position.x, self.position.y, self.position.z)

        # 2) Rotacja (Euler angles)
        #  - kolejnoś: x->y->z
        glRotatef(self.rotation.x, 1.0, 0.0, 0.0)
        glRotatef(self.rotation.y, 0.0, 1.0, 0.0)
        glRotatef(self.rotation.z, 0.0, 0.0, 1.0)

        # 3) Skalowanie
        glScalef(self.scale.x, self.scale.y, self.scale.z)

    def move_x(self, amount):
        self.position.x += amount

    def move_y(self, amount):
        self.position.y += amount

    def move_z(self, amount):
        self.position.z += amount
    def move(self, amount:pygame.math.Vector3):
        self.position += amount # wektor ma juz zadana wspolrzedna 
