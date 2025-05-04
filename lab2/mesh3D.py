from OpenGL.GL import *  # Import funkcji z OpenGL (m.in. do rysowania)

class Mesh3D:
   def __init__(self):
       # Definiujemy listę wierzchołków (x, y, z)
       self.vertices = [(0.5, -0.5, 0.5),
                       (-0.5, -0.5, 0.5),
                       (0.5, 0.5, 0.5),
                       (-0.5, 0.5, 0.5)]
       # Definiujemy indeksy określające, które wierzchołki tworzą trójkąty
       self.triangles = [0, 2, 3, 0, 3, 1]

   def draw(self):
       # Rysujemy trójkąty w pętli, po 3 indeksy na każdy trójkąt
       for t in range(0, len(self.triangles), 3):
           glBegin(GL_LINE_LOOP)  # Rozpoczynamy rysowanie obwiedni trójkąta

           # Przekazujemy do OpenGL współrzędne każdego z wierzchołków
           glVertex3fv(self.vertices[self.triangles[t]])
           glVertex3fv(self.vertices[self.triangles[t + 1]])
           glVertex3fv(self.vertices[self.triangles[t + 2]])

           glEnd()  # Kończymy rysowanie aktualnego trójkąta