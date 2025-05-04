from OpenGL.GL import *
from Utils import map_value  # Import specific function
import pygame
from Settings import *  # Import settings

class Button:
    def __init__(self, screen, position, width, height, color, o_color, p_color, callback=None):  # Changed on_click to callback
        self.screen = screen
        self.position = position
        self.width = width
        self.height = height
        # Convert colors from 0-255 pygame.Color to 0.0-1.0 tuple if needed
        self.normal_color = self._normalize_color(color)
        self.over_color = self._normalize_color(o_color)
        self.pressed_color = self._normalize_color(p_color)
        self.callback = callback  # Store the callback function
        self.is_pressed = False  # Tracks if the mouse button is currently down *over this button*
        self.is_over = False  # Tracks if the mouse cursor is currently over this button

    def _normalize_color(self, color):
        """Converts pygame.Color or tuple(0-255) to tuple(0.0-1.0)."""
        if isinstance(color, pygame.Color):
            return (color.r / 255.0, color.g / 255.0, color.b / 255.0)
        elif isinstance(color, (list, tuple)) and len(color) == 3:
            # Assume 0-255 if any value > 1, else assume 0-1
            if any(c > 1 for c in color):
                return (color[0] / 255.0, color[1] / 255.0, color[2] / 255.0)
            else:
                return tuple(color)  # Already normalized
        return (0.0, 0.0, 0.0)  # Default black if invalid format

    def update(self, events):
        """Handles events and draws the button."""
        self.handle_events(events)
        self.draw()  # Draw no longer needs events directly

    def handle_events(self, events):
        """Processes mouse events to update button state."""
        mouse_pos = pygame.mouse.get_pos()
        # Map mouse coordinates from window space to GUI space
        mx = map_value(0, window_width, 0, gui_width, mouse_pos[0])
        my = map_value(0, window_height, gui_height, 0, mouse_pos[1])  # Invert Y for typical GUI coords

        # Check if mouse is over the button
        self.is_over = self.position[0] <= mx < (self.position[0] + self.width) and \
                       self.position[1] <= my < (self.position[1] + self.height)

        # Process relevant events
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.is_over:
                    self.is_pressed = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if self.is_pressed and self.is_over:
                    # --- Execute callback on click release ---
                    if self.callback:
                        self.callback()
                self.is_pressed = False  # Always release press state on mouse up

        # If mouse button was released *not* over the button, ensure is_pressed is False
        if not pygame.mouse.get_pressed()[0]:  # Check if left button is up globally
            self.is_pressed = False

    def draw(self):
        """Draws the button based on its current state."""
        glPushMatrix()
        glLoadIdentity()

        glDisable(GL_TEXTURE_2D)  # Ensure texturing is off before drawing the button

        # Wybór koloru w zależności od stanu przycisku
        current_color = self.normal_color
        if self.is_pressed and self.is_over:
            current_color = self.pressed_color
        elif self.is_over:
            current_color = self.over_color

        glColor3f(current_color[0], current_color[1], current_color[2])

        # Rysowanie przycisku
        glBegin(GL_POLYGON)
        glVertex2f(self.position[0], self.position[1])
        glVertex2f(self.position[0] + self.width, self.position[1])
        glVertex2f(self.position[0] + self.width, self.position[1] + self.height)
        glVertex2f(self.position[0], self.position[1] + self.height)
        glEnd()
        glPopMatrix()
