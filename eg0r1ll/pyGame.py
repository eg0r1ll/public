import pygame
import random

pygame.init() # начало игры
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("test_game")

running = True
screen.fill((100,100,100))
while running:
    pygame.display.update()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif i.type == pygame.KEYDOWN: 
            if i.key == pygame.K_w:
                screen.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

