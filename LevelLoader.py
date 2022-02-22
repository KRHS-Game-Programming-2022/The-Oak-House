import pygame, sys, math, random
from LevelLoader import *
from WallTile import*
from Hud import*
from Spawner import *
from SpriteSheet import*

pygame.init()

if not pygame.font:
    print("Warning, fonts disabled")

   
clock = pygame.time.Clock();

size = [1300, 960]
screen = pygame.display.set_mode(size)
