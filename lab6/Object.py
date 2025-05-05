from Mesh3D import *
from Transform import *
from Button import *
from OpenGL.GL import * # Added for glPushMatrix/PopMatrix
from Grid import *
class Object:
    def __init__(self, obj_name):
        self.name = obj_name
        self.components = []

    def add_component(self, component):
        if isinstance(component, Transform):
            self.components.insert(0,component)
        else:
            self.components.append(component)

    def update(self, events = None): # Renamed parameter from event to events
        glPushMatrix()
        transform_applied = False # Track if transform was applied in this update
        obj_transform = self.get_component(Transform) # Get transform component once

        if obj_transform:
            obj_transform.apply_transform()
            transform_applied = True

        for c in self.components:
            # Skip Transform component as it's handled above
            if isinstance(c, Transform):
                continue

            # Call specific methods for other components
            if isinstance(c, Mesh3D):
                c.draw()
            elif isinstance(c, Button):
                # Buttons manage their own matrix stack if needed
                c.update(events) # Pass the events list
            elif isinstance(c, Grid):
                c.draw()

        glPopMatrix()

    def get_component(self, class_type):
       """Gets the first component of the specified type."""
       for c in self.components:
           if isinstance(c, class_type): # Use isinstance for inheritance checks
               return c
       return None