import pygame, sys, math
from user.player import Player
from Button import*

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
        bigfont = pygame.font.Font("assets/fonts/Chiken Skratch.ttf", 55)
        title = bigfont.render("The Oak House", True, (192, 26, 26))
        titleRect=title.get_rect(midtop=[400, 50])
        
        playButton = Button("play", [400, 700-30])
        
    while mode == "MainMenu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    main = False
            if event.type == pygame.MOUSEMOTION:
                playButton.hover(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:           #BUTTONS!!!
                playButton.clickDown(event.pos)

            if event.type == pygame.MOUSEBUTTONUP:
                if playButton.clickUp(event.pos):
                    mode = "PlayGame"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mode="PlayGame"


        screen.fill((0, 0, 0))
        screen.blit(title,titleRect)
        screen.blit(playButton.image, playButton.rect)
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
