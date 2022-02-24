import pygame, sys, math
from user.player import Player

pygame.init()
clock = pygame.time.Clock()

main = True
size = [800, 800]
screen = pygame.display.set_mode(size)

player = Player()
step = 5

while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player.control("up")
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.control("left")
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.control("right")
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.control("down")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player.control("stop up")
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.control("stop left")
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.control("stop right")
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.control("stop down")

    player.update()

    screen.fill((0, 0, 0))
    screen.blit(player.image, player.rect)
    pygame.display.flip()
    clock.tick(60)
