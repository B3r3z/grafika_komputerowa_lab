from OpenGL.GL import *
from mesh3D import Mesh3D
class cube(Mesh3D):
   def __init__(self):
       super().__init__()
       
       # Definiujemy listę wierzchołków (x, y, z)
       self.vertices = [
            (-0.5, -0.5, -0.5),
            (-0.5, -0.5,  0.5),
            (-0.5,  0.5, -0.5),
            (-0.5,  0.5,  0.5),
             (0.5, -0.5, -0.5),
             (0.5, -0.5,  0.5),
             (0.5,  0.5, -0.5),
             (0.5,  0.5,  0.5)
            ]
       # Definiujemy indeksy określające, które wierzchołki tworzą trójkąty
       #self.triangles = [0, 2, 3, 0, 3, 1, 4,6,7,4,7,5 ]
       self.triangles = [
    0, 1, 3, 0, 3, 2,  # tył
    4, 5, 7, 4, 7, 6,  # front
    0, 1, 5, 0, 5, 4,  # lewa
    2, 3, 7, 2, 7, 6,  # prawa
    2, 3, 7, 2, 6, 7,  # góra (poprawione)
    0, 1, 5, 0, 5, 4   # dół (poprawione)
]
   def draw(self):
       # Rysujemy trójkąty w pętli, po 3 indeksy na każdy trójkąt
       for t in range(0, len(self.triangles), 3):
           glBegin(GL_LINE_LOOP)  # Rozpoczynamy rysowanie obwiedni trójkąta

           # Przekazujemy do OpenGL współrzędne każdego z wierzchołków
           glVertex3fv(self.vertices[self.triangles[t]])
           glVertex3fv(self.vertices[self.triangles[t + 1]])
           glVertex3fv(self.vertices[self.triangles[t + 2]]
                       )

           glEnd()  # Kończymy rysowanie aktualnego trójkąta