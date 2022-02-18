import pygame
import sys
import user.player as player

main = True
size = [800, 800]
screen = pygame.display.set_mode(size)

player = player.Player()
s = 5

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
                player.control("left")
            if event.key == pygame.K_RIGHT or event.key == ord('a'):
                player.control(-step, 0)
            if event.key == pygame.K_LEFT or event.key == ord('s'):
                player.control(0, -step)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(step, 0)



