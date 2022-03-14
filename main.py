import pygame, sys, math
from user.player import Player

pygame.init()
clock = pygame.time.Clock()

main = True
size = [800, 800]
screen = pygame.display.set_mode(size)

player = Player()
step = 5

mode = "MainMenu"

while main:
    if mode == "MainMenu":
        bigfont = pygame.font.Font("assets/fonts/Chiken Skratch.ttf", 60)
        title = bigfont.render("The Oak House", True, (192, 26, 26))
        titleRect=title.get_rect(midtop=[400, 50])
        
        smallfont = pygame.font.Font("assets/fonts/Chiken Skratch.ttf", 30)
        start = smallfont.render("Press Enter to Start", True, (192, 26, 26))
        startRect=start.get_rect(midbottom=[400, 700])
    while mode == "MainMenu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    main = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mode="PlayGame"
        screen.fill((0, 0, 0))
        screen.blit(title,titleRect)
        screen.blit(start,startRect)
        pygame.display.flip()
        clock.tick(60)
    if mode == "PlayGame":
        player = Player()
        step = 5
    while mode == "PlayGame":
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
