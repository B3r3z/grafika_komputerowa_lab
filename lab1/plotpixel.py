import pygame

pygame.init()

screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("B B z kwadratów")

done = False
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)


font = pygame.font.Font(None, 50)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(black)
    position1 = (100, 100)
    pygame.draw.rect(screen, white, (position1[0], position1[1], 50, 50))
    position2 = (170, 100)
    pygame.draw.rect(screen, white, (position2[0], position2[1], 50, 50))
    text_surface_b = font.render("B", True, black)
    screen.blit(text_surface_b, (position1[0] + 10, position1[1] + 5))
    screen.blit(text_surface_b, (position2[0] + 10, position2[1] + 5))
    pygame.display.update()

pygame.quit()
