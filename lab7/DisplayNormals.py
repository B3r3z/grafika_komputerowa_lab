import pygame
from OpenGL.GL import *
from MathOGL import *  # importujemy naszą funkcję cross_product

class DisplayNormals:
    def __init__(self, vertices, triangles):
        self.vertices = vertices
        self.triangles = triangles
        self.normals = []
        # Obliczamy normalne dla każdej ściany (trójkąta) obiektu:
        for t in range(0, len(self.triangles), 3):
            vertex1 = self.vertices[self.triangles[t]]
            vertex2 = self.vertices[self.triangles[t + 1]]
            vertex3 = self.vertices[self.triangles[t + 2]]
            # Wektory krawędziowe p i q dla trójkąta (vertex1-vertex2, vertex2-vertex3):
            p = pygame.Vector3(
                vertex1[0] - vertex2[0],
                vertex1[1] - vertex2[1],
                vertex1[2] - vertex2[2]
            )
            q = pygame.Vector3(
                vertex2[0] - vertex3[0],
                vertex2[1] - vertex3[1],
                vertex2[2] - vertex3[2]
            )
            # Iloczyn wektorowy p x q daje normalną:
            norm = cross_product(p, q)
            # Punkt startowy dla rysowania normalnej (środek układu obiektu):
            nstart = (0, 0, 0)
            # Zapisujemy krotkę (punkt_start, punkt_start + wektor_normalny)
            self.normals.append((nstart, nstart + norm))

    def draw(self):
        glColor3fv((0, 1, 0))         # ustawiamy kolor rysowania na zielony
        glBegin(GL_LINES)             # zaczynamy rysowanie linii
        for start_point, end_point in self.normals:
            # Wstawiamy wierzchołek początkowy linii (normalna wychodzi z nstart)
            glVertex3fv((start_point[0], start_point[1], start_point[2]))
            # Wstawiamy wierzchołek końcowy linii (dokładamy wektor normalny)
            glVertex3fv((end_point[0], end_point[1], end_point[2]))
        glEnd()
