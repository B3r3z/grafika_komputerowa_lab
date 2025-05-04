from mesh3D import *
from transform import *
class Object:
    def __init__(self, obj_name):
        self.name = obj_name
        self.components = []
        #self.transform = Transform()


    def add_component(self, component):
        if isinstance(component, Transform):
            self.components.insert(0,component)
        else:
            self.components.append(component)

    #def update(self):
    #    for c in self.components:
    #        if isinstance(c, Mesh3D):
    #            c.draw()
    def update(self):
        glPushMatrix()
        for c in self.components:
            if isinstance(c, Transform):
             #   pos = c.get_position()
             #   glTranslatef(pos.x, pos.y, pos.z)
                c.apply_transform()
            if isinstance(c, Mesh3D):
                c.draw()
        glPopMatrix()