import pygame, math, random, sys

pygame.init()

clock = pygame.time.Clock()

size = [1000,900]
screen = pygame.display.set_mode(size)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
                
    
    
    screen.fill((0,0,0))
    pygame.display.flip()
    clock.tick(60)
