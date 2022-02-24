import pygame, sys, math
from WallTile import *
from Spawner import *
import user.player as player
def loadLevel (lev):
    f = open(lev, 'r')
    lines = f.readlines()
    f.close()

    size = 50
    offset = size/1
    tiles = []
    newLines = []
    walls = []
    spawners = []

    for line in lines:
        newLine = ""
        for c in line:
            if c != "\n":
                newLine += c
        newLines += [newLine]

    lines = newLines

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                walls += [Wall([x*size+offset, y*size+offset])]
            if c == "X":
                spawners += [Spawner([x*size+offset, y*size+offset])]
    tiles = [walls,
            spawners]
    return tiles




#loadLevel("Levels/example.lvl")

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

