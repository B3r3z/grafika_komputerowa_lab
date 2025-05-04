from OpenGL.GL import * 
import pygame

class Mesh3D:
    def __init__(self):
        # Definiujemy listę wierzchołków (x, y, z)
        self.vertices = [(0.5, -0.5, 0.5),
                        (-0.5, -0.5, 0.5),
                        (0.5, 0.5, 0.5),
                        (-0.5, 0.5, 0.5)]
        
        # Definiujemy indeksy określające, które wierzchołki tworzą trójkąty
        self.triangles = [0, 2, 3, 0, 3, 1]
        
        # Ustawienia domyślne dla rysowania i teksturowania
        self.draw_type = GL_LINE_LOOP
        self.texture = None
        self.texID = 0
    
    def draw(self):
     glEnable(GL_TEXTURE_2D)
     glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
     glBindTexture(GL_TEXTURE_2D, self.texID)

     for t in range(0, len(self.triangles), 3):
         glBegin(self.draw_type)

         glTexCoord2fv(self.uvs[t])
         glVertex3fv(self.vertices[self.triangles[t]])

         glTexCoord2fv(self.uvs[t+1])
         glVertex3fv(self.vertices[self.triangles[t+1]])

         glTexCoord2fv(self.uvs[t+2])
         glVertex3fv(self.vertices[self.triangles[t+2]])

         glEnd()
    
    def init_texture(self):
        self.texID = glGenTextures(1)
        
        textureData = pygame.image.tobytes(self.texture, 'RGB', 1)
        width = self.texture.get_width()
        height = self.texture.get_height()
        
        glBindTexture(GL_TEXTURE_2D, self.texID)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)  # mipmapping
        glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 0,
                     GL_RGB, GL_UNSIGNED_BYTE, textureData)
