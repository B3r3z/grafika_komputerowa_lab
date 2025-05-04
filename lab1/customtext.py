import pygame

pygame.init()
screen_width = 1000
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
done = False
white = pygame.Color(255, 255, 255)
pygame.font.init()

# Użycie systemowej czcionki Comic Sans MS
font = pygame.font.SysFont('Comic Sans MS', 60, False, True)
text = font.render('graphic design is my passion', False, white)
# Przykład użycia niestandardowej czcionki:
font_custom = pygame.font.Font('fonts/KOMIKAX_.ttf', 100)
custom_text = font_custom.render('Inny tekst', False, white)
# W pętli głównej:
screen.blit(custom_text, (10, 120))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(text, (10, 10))
    pygame.display.update()
pygame.quit()