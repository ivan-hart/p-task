import pygame
from color import Color

class Light(object):

    def __init__(self, pos, dir, color):
        self.pos = pos
        self.dir = dir
        self.color = color


    def change(self):
        self.color = Color.red if self.color == Color.green else Color.green


    def check(self, car):
        match car.dir:
            case 'l':
                return car.posX > 336 and car.posX < 336 + 20
            case 'u':
                return car.posY > 336 and car.posY < 336 + 20
            case 'r':
                return car.posX + 120 < 166 and car.posX > 166 - 120
            case 'd':
                return car.posY + 120 < 166 and car.posY > 166
        return RuntimeError


    def draw(self, WIN):
        pygame.draw.circle(WIN, self.color, self.pos, 18)
