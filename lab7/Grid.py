from OpenGL.GL import *

class Grid():
    def __init__(self, interval, halfsize, colour):
        self.interval = interval
        self.halfsize = halfsize
        self.colour = colour
        # Normalize color if needed
        if any(c > 1.0 for c in self.colour):
            self.normalized_color = (
                self.colour[0]/255.0, 
                self.colour[1]/255.0, 
                self.colour[2]/255.0
            )
        else:
            self.normalized_color = self.colour

    def draw(self):
        glColor3fv(self.normalized_color)  # Use normalized color
        glBegin(GL_LINES)
#        for x in range(-self.halfsize, self.halfsize):
#            for z in range(-self.halfsize, self.halfsize):
#                # Draw horizontal lines (along X axis)
#                glVertex3fv((x * self.interval, 0, z * self.interval))
#                glVertex3fv(((x+1) * self.interval, 0, z * self.interval))
#                
#                # Draw vertical lines (along Z axis)
#                glVertex3fv((x * self.interval, 0, z * self.interval))
#                glVertex3fv((x * self.interval, 0, (z+1) * self.interval))
        # Loop variables x and y now correspond directly to X and Y axes
        for x in range(-self.halfsize, self.halfsize):
            for y in range(-self.halfsize, self.halfsize):
                # Draw horizontal lines (along X axis) at Z=0
                glVertex3fv((x * self.interval, y * self.interval, 0)) # Z is 0
                glVertex3fv(((x+1) * self.interval, y * self.interval, 0)) # Z is 0

                # Draw vertical lines (along Y axis) at Z=0
                glVertex3fv((x * self.interval, y * self.interval, 0)) # Z is 0
                glVertex3fv((x * self.interval, (y+1) * self.interval, 0)) # Z is 0
        glEnd()

        
        # Reset color to white after drawing
        glColor3f(1.0, 1.0, 1.0)