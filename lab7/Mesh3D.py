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
        
        # Definiujemy współrzędne tekstury (UV) dla każdego wierzchołka
        self.uvs = [(1, 0), (0, 0), (1, 1), (0, 1)]
        
        # Dodajemy kolor normalny, którego brakowało
        self.normal_color = (1, 1, 1)
        
        # Ustawienia domyślne dla rysowania i teksturowania
        self.draw_type = GL_LINE_LOOP
        self.texture = None
        self.texID = 0
    
    def draw(self):
        # Enable texturing before drawing the textured mesh
        if self.texture and self.texID:
            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, self.texID)
            glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        
        glColor3f(self.normal_color[0], self.normal_color[1], self.normal_color[2])
        
        for t in range(0, len(self.triangles), 3):
            glBegin(self.draw_type)
            
            # Indeksy wierzchołków dla bieżącego trójkąta
            idx1 = self.triangles[t]
            idx2 = self.triangles[t+1]
            idx3 = self.triangles[t+2]
            
            # Ustawiamy współrzędne tekstury i wierzchołki
            glTexCoord2fv(self.uvs[idx1])
            glVertex3fv(self.vertices[idx1])
            
            glTexCoord2fv(self.uvs[idx2])
            glVertex3fv(self.vertices[idx2])
            
            glTexCoord2fv(self.uvs[idx3])
            glVertex3fv(self.vertices[idx3])
            
            glEnd()
        
        # Disable texturing after drawing the textured mesh
        if self.texture and self.texID:
            glDisable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, 0) # Unbind texture
    
    def init_texture(self):
        if not self.texture:
            return
            
        self.texID = glGenTextures(1)
        
        textureData = pygame.image.tobytes(self.texture, 'RGB', 1)
        width = self.texture.get_width()
        height = self.texture.get_height()
        
        glBindTexture(GL_TEXTURE_2D, self.texID)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 0,
                     GL_RGB, GL_UNSIGNED_BYTE, textureData)
