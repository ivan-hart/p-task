import pygame


class Car(object):

    def __init__(self, pos, dir, image):
        self.posX = int(pos[0])
        self.posY = int(pos[1])
        self.dir = dir
        self.image = image

    def move(self):
        match self.dir:
            case 'l':
                self.posX -= 10
            case 'u':
                self.posY -= 10
            case 'r':
                self.posX += 10
            case 'd':
                self.posY += 10

    def draw(self, win):
        car = pygame.transform.scale(self.image, (100, 100))
        match self.dir:
            case 'l':
                car = pygame.transform.rotate(car, -90)
            case 'r':
                car = pygame.transform.rotate(car, 90)
            case 'd':
                car = pygame.transform.rotate(car, 180)

        win.blit(car, (self.posX, self.posY))
