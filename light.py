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
                return car.posX + 100 < 166 and car.posX + 100 > 166 - 20
            case 'd':
                return car.posY < 166 and car.posY > 166 - 120


    def draw(self, WIN):
        pygame.draw.circle(WIN, self.color, self.pos, 18)
