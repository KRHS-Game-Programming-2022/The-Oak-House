from map.spawner import Spawner
from map.wall import Wall


def loadLevel(lev):
    f = open(lev, 'r')
    lines = f.readlines()
    f.close()

    size = 20
    offset = size / 2
    walls = []
    spawners = []

    newLines = []
    for line in lines:
        newline = ""
        for c in line:
            if c != "\n":
                newline += c
        newLines += [newline]

    lines = newLines

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                walls += [Wall([x * size + offset, y * size + offset])]
            elif c == "X":
                spawners += [Spawner([x * size + offset, y * size + offset])]
    tiles = {"walls": walls, "spawners":
             spawners}

    return tiles
