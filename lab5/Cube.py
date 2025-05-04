from OpenGL.GL import *
from Mesh3D import Mesh3D
import pygame
import os

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
        
        # Współrzędne UV dla każdego wierzchołka trójkąta (36 wartości dla 36 indeksów wierzchołków)
        self.uvs = [
            (1.0, 0.0), (1.0, 1.0), (0.0, 1.0), (1.0, 0.0), (0.0, 1.0), (0.0, 0.0),
            (0.0, 0.0), (0.0, 1.0), (1.0, 1.0), (0.0, 0.0), (1.0, 1.0), (1.0, 0.0),
            (0.0, 0.0), (1.0, 0.0), (0.0, 1.0), (0.0, 1.0), (1.0, 0.0), (1.0, 1.0),
            (1.0, 0.0), (1.0, 1.0), (0.0, 0.0), (1.0, 1.0), (0.0, 0.0), (0.0, 1.0),
            (1.0, 0.0), (0.0, 0.0), (0.0, 1.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0),
            (1.0, 1.0), (0.0, 1.0), (0.0, 0.0), (1.0, 1.0), (1.0, 0.0), (0.0, 0.0)
        ]
        
        self.draw_type = draw_type
        self.load_texture(filename)
        
    def load_texture(self, filename):
        """Ładuje teksturę z pliku."""
        try:
            if os.path.exists(filename):
                self.texture = pygame.image.load(filename)
                self.init_texture()
            else:
                print(f"Plik tekstury nie istnieje: {filename}")
                self.texture = None
                self.texID = 0
        except Exception as e:
            print(f"Błąd ładowania tekstury: {e}")
            self.texture = None
            self.texID = 0
        
    def init_texture(self):
        """Inicjalizuje teksturę w OpenGL."""
        if not self.texture:
            return
            
        self.texID = glGenTextures(1)
        textureData = pygame.image.tobytes(self.texture, 'RGB', 1)
        width, height = self.texture.get_size()
        
        glBindTexture(GL_TEXTURE_2D, self.texID)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, textureData)
    
    def draw(self):
        """Rysuje kostkę z teksturą."""
        # Włączamy teksturowanie jeśli tekstura jest dostępna
        if self.texture and self.texID:
            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, self.texID)
        
        glBegin(GL_TRIANGLES)
        for i in range(0, len(self.triangles)):
            # Używamy prawidłowych indeksów UV dla każdego wierzchołka
            uv_index = i  # Każdy wierzchołek trójkąta ma swoją współrzędną UV
            vertex_index = self.triangles[i]  # Indeks wierzchołka
            
            if self.texture and self.texID:
                glTexCoord2fv(self.uvs[uv_index])
            glVertex3fv(self.vertices[vertex_index])
        
        glEnd()
        
        # Wyłączamy teksturowanie po zakończeniu rysowania
        if self.texture and self.texID:
            glDisable(GL_TEXTURE_2D)
