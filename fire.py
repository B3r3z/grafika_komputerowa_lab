import pygame
import random

# Ustawienia rozmiaru animacji.
SCALE = 4  # skalowanie pojedynczego "piksela ognia"
FIRE_WIDTH = 80   # szerokość siatki ognia
FIRE_HEIGHT = 60  # wysokość siatki ognia

# Definicja palety kolorów (w stylu 8-bit) – od ciemnego do jasnego
palette = [
    (7, 7, 7),
    (31, 7, 7),
    (47, 15, 7),
    (71, 15, 7),
    (87, 23, 7),
    (103, 31, 7),
    (119, 31, 7),
    (143, 39, 7),
    (159, 47, 7),
    (175, 63, 7),
    (191, 71, 7),
    (199, 71, 7),
    (223, 79, 7),
    (223, 87, 7),
    (223, 87, 7),
    (215, 95, 7),
    (215, 95, 7),
    (215, 103, 15),
    (207, 111, 15),
    (207, 119, 15),
    (207, 127, 15),
    (207, 135, 23),
    (199, 135, 23),
    (199, 143, 23),
    (199, 151, 31),
    (191, 159, 31),
    (191, 159, 31),
    (191, 167, 39),
    (191, 167, 39),
    (191, 175, 47),
    (183, 175, 47),
    (183, 183, 47),
    (183, 183, 55),
    (207, 207, 111),
    (223, 223, 159),
    (239, 239, 199),
    (255, 255, 255)
]
NUM_COLORS = len(palette)

# Inicjalizacja siatki ognia – każdy element to wartość intensywności od 0 do NUM_COLORS-1.
fire_pixels = [[0 for _ in range(FIRE_WIDTH)] for _ in range(FIRE_HEIGHT)]

def initialize_fire():
    """Ustawia dolny wiersz siatki na maksymalną intensywność (źródło ognia)."""
    for x in range(FIRE_WIDTH):
        fire_pixels[FIRE_HEIGHT - 1][x] = NUM_COLORS - 1

def update_fire():
    """
    Aktualizuje siatkę ognia:
    - Każdy piksel (poza dolnym wierszem) pobiera wartość od piksela znajdującego się niżej
      z pewnym, losowym osłabieniem (decay).
    - Wartość ta jest przypisywana do piksela powyżej, przesuniętego w lewo o losową wartość.
    """
    for y in range(1, FIRE_HEIGHT):
        for x in range(FIRE_WIDTH):
            decay = random.randint(0, 3)
            new_intensity = fire_pixels[y][x] - decay
            if new_intensity < 0:
                new_intensity = 0
            # Przenoszenie efektu ognia do piksela powyżej, z lekkim przesunięciem w lewo
            dst_x = x - decay
            if dst_x < 0:
                dst_x = 0
            fire_pixels[y - 1][dst_x] = new_intensity

def draw_fire(screen):
    """Rysuje siatkę ognia na ekranie, mapując wartości intensywności na kolory z palety."""
    for y in range(FIRE_HEIGHT):
        for x in range(FIRE_WIDTH):
            color = palette[fire_pixels[y][x]]
            rect = (x * SCALE, y * SCALE, SCALE, SCALE)
            pygame.draw.rect(screen, color, rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((FIRE_WIDTH * SCALE, FIRE_HEIGHT * SCALE))
    pygame.display.set_caption("8-bitowy efekt ognia")
    clock = pygame.time.Clock()
    
    initialize_fire()
    
    running = True
    while running:
        # Obsługa zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        update_fire()
        screen.fill((0, 0, 0))
        draw_fire(screen)
        pygame.display.flip()
        clock.tick(30)  # 30 FPS
    
    pygame.quit()

if __name__ == '__main__':
    main()
