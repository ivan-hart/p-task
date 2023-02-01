"""
author @Ivan Hart
Name - Traffic Simulator
"""

import os
import pygame
import Color
from car import Car

WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Traffic Simulator")

delta = pygame.time.Clock()

FPS = 60

image = pygame.image.load(os.path.join("car.png"))

cars = []
lights = []


def buildObjects():
    #for i in range(4):
    car = Car((200, 200), 'r', image)
    cars.append(car)


def render():
    WIN.fill(Color.White)
    for i in cars:
        i.draw(WIN)


def update():
    for i in cars:
        i.move()


def main():
    buildObjects()
    run = True
    while run:
        delta.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        render()
        update()
        pygame.display.update()


if __name__ == "__main__":
    main()
