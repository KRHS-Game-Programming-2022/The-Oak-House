import pygame,sys

clock=pygame.time.Clock()

size = [700, 900]
screen=pygame.display.set_mode(size)

pacImage=pygame.image.load("pacman.png")
pacRect=pacImage.get_rect(center=[700/2,900/2])
pacSpeed=[8,8]

orangeImage=pygame.image.load("orangeghost.png")
orangeRect=orangeImage.get_rect(center=[700/3,900/4])
orangeSpeed=[7,9]

goombsImage=pygame.image.load("goomba.png")
goombsRect=goombsImage.get_rect(center=[700/4,900/2])
goombsSpeed=[5,8]

cornholioImage=pygame.image.load("cornholio.png")
cornholioRect=cornholioImage.get_rect(center=[700/5,900/3])
cornholioSpeed=[6,9]

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            
    pacRect=pacRect.move(pacSpeed)
    if pacRect.right > size[0]:
        pacSpeed[0] = -pacSpeed[0]
    if pacRect.bottom > size[1]:
        pacSpeed[1] = -pacSpeed[1]
    if pacRect.left < 0:
        pacSpeed[0] = -pacSpeed[0]
    if pacRect.top < 0:
        pacSpeed[1] = -pacSpeed[1]
        
    orangeRect=orangeRect.move(orangeSpeed)
    if orangeRect.right > size[0]:
        orangeSpeed[0] = -orangeSpeed[0]
    if orangeRect.bottom > size[1]:
        orangeSpeed[1] = -orangeSpeed[1]
    if orangeRect.left < 0:
        orangeSpeed[0] = -orangeSpeed[0]
    if orangeRect.top < 0:
        orangeSpeed[1] = -orangeSpeed[1]
        
    goombsRect=goombsRect.move(goombsSpeed)
    if goombsRect.right > size[0]:
        goombsSpeed[0] = -goombsSpeed[0]
    if goombsRect.bottom > size[1]:
        goombsSpeed[1] = -goombsSpeed[1]
    if goombsRect.left < 0:
        goombsSpeed[0] = -goombsSpeed[0]
    if goombsRect.top < 0:
        goombsSpeed[1] = -goombsSpeed[1]
    
    cornholioRect=cornholioRect.move(cornholioSpeed)
    if cornholioRect.right > size[0]:
        cornholioSpeed[0] = -cornholioSpeed[0]
    if cornholioRect.bottom > size[1]:
        cornholioSpeed[1] = -cornholioSpeed[1]
    if cornholioRect.left < 0:
        cornholioSpeed[0] = -cornholioSpeed[0]
    if cornholioRect.top < 0:
        cornholioSpeed[1] = -cornholioSpeed[1]
        
    if pacRect.right > orangeRect.left:
        if pacRect.left < orangeRect.right:
            if pacRect.bottom > orangeRect.top:
                if pacRect.top < orangeRect.bottom:
                    pacSpeed[0] = -pacSpeed[0]
                    pacSpeed[1] = -pacSpeed[1]
                    orangeSpeed[0] = -orangeSpeed[0]
                    orangeSpeed[1] = -orangeSpeed[1]
                    
    if pacRect.right > goombsRect.left:
        if pacRect.left < goombsRect.right:
            if pacRect.bottom > goombsRect.top:
                if pacRect.top < goombsRect.bottom:
                    pacSpeed[0] = -pacSpeed[0]
                    pacSpeed[1] = -pacSpeed[1]
                    goombsSpeed[0] = -goombsSpeed[0]
                    goombsSpeed[1] = -goombsSpeed[1]
                    
    if goombsRect.right > orangeRect.left:
        if goombsRect.left < orangeRect.right:
            if goombsRect.bottom > orangeRect.top:
                if goombsRect.top < orangeRect.bottom:
                    goombsSpeed[0] = -goombsSpeed[0]
                    goombsSpeed[1] = -goombsSpeed[1]
                    orangeSpeed[0] = -orangeSpeed[0]
                    orangeSpeed[1] = -orangeSpeed[1]
                    
    if cornholioRect.right > goombsRect.left:
        if cornholioRect.left < goombsRect.right:
            if cornholioRect.bottom > goombsRect.top:
                if cornholioRect.top < goombsRect.bottom:
                    cornholioSpeed[0] = -cornholioSpeed[0]
                    cornholioSpeed[1] = -cornholioSpeed[1]
                    goombsSpeed[0] = -goombsSpeed[0]
                    goombsSpeed[1] = -goombsSpeed[1]
                    
    if cornholioRect.right > orangeRect.left:
        if cornholioRect.left < orangeRect.right:
            if cornholioRect.bottom > orangeRect.top:
                if cornholioRect.top < orangeRect.bottom:
                    cornholioSpeed[0] = -cornholioSpeed[0]
                    cornholioSpeed[1] = -cornholioSpeed[1]
                    orangeSpeed[0] = -orangeSpeed[0]
                    orangeSpeed[1] = -orangeSpeed[1]
            
    if cornholioRect.right > pacRect.left:
        if cornholioRect.left < pacRect.right:
            if cornholioRect.bottom > pacRect.top:
                if cornholioRect.top < pacRect.bottom:
                    cornholioSpeed[0] = -cornholioSpeed[0]
                    cornholioSpeed[1] = -cornholioSpeed[1]
                    pacSpeed[0] = -pacSpeed[0]
                    pacSpeed[1] = -pacSpeed[1]
                    
    
                    
    screen.fill((38,116,42))
    screen.blit(pacImage,pacRect)
    screen.blit(orangeImage,orangeRect)
    screen.blit(goombsImage,goombsRect)
    screen.blit(cornholioImage,cornholioRect)
    pygame.display.flip()
    clock.tick(60)

