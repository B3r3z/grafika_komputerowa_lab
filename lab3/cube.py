from OpenGL.GL import *
from mesh3D import Mesh3D
import pygame

class Cube(Mesh3D):
    def __init__(self, draw_type, filename):
        super().__init__()
        
        # Definiujemy listę wierzchołków (x, y, z)
        self.vertices = [
            (-0.5, -0.5, -0.5), (-0.5, -0.5,  0.5), (-0.5,  0.5, -0.5), (-0.5,  0.5,  0.5),
             (0.5, -0.5, -0.5),  (0.5, -0.5,  0.5),  (0.5,  0.5, -0.5),  (0.5,  0.5,  0.5)
        ]
        
        # Definiujemy indeksy określające, które wierzchołki tworzą trójkąty
        self.triangles = [
            0, 1, 3, 0, 3, 2,  # Tył
            4, 5, 7, 4, 7, 6,  # Front
            0, 1, 5, 0, 5, 4,  # Lewa
            2, 3, 7, 2, 7, 6,  # Prawa
            1, 5, 7, 1, 3, 7,  # Góra
            0, 4, 6, 0, 2, 6   # Dół
        ]
        
        # Współrzędne UV dla każdej ściany
        self.uvs = [
            (1.0, 0.0), (1.0, 1.0), (0.0, 1.0), (1.0, 0.0), (0.0, 1.0), (0.0, 0.0),
            (0.0, 0.0), (0.0, 1.0), (1.0, 1.0), (0.0, 0.0), (1.0, 1.0), (1.0, 0.0),
            (0.0, 0.0), (1.0, 0.0), (0.0, 1.0), (0.0, 1.0), (1.0, 0.0), (1.0, 1.0),
            (1.0, 0.0), (1.0, 1.0), (0.0, 0.0), (1.0, 1.0), (0.0, 0.0), (0.0, 1.0),
            (1.0, 0.0), (0.0, 0.0), (0.0, 1.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0),
            (1.0, 1.0), (0.0, 1.0), (0.0, 0.0), (1.0, 1.0), (1.0, 0.0), (0.0, 0.0)
        ]
        
        self.draw_type = draw_type
        self.texture = pygame.image.load(filename)
        self.init_texture()
        
    def init_texture(self):
        self.texID = glGenTextures(1)
        textureData = pygame.image.tobytes(self.texture, 'RGB', 1)
        width, height = self.texture.get_size()
        
        glBindTexture(GL_TEXTURE_2D, self.texID)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, textureData)
    
    def draw(self):
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.texID)
        
        glBegin(GL_TRIANGLES)
        for t in range(0, len(self.triangles), 3):
            glTexCoord2fv(self.uvs[t])
            glVertex3fv(self.vertices[self.triangles[t]])

            glTexCoord2fv(self.uvs[t+1])
            glVertex3fv(self.vertices[self.triangles[t+1]])

            glTexCoord2fv(self.uvs[t+2])
            glVertex3fv(self.vertices[self.triangles[t+2]])
        
        glEnd()
        glDisable(GL_TEXTURE_2D)
