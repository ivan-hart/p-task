import pygame


class Car(object):

    def __init__(self, pos, dir, max_speed, image):
        self.posX = int(pos[0])
        self.posY = int(pos[1])
        self.dir = dir
        self.max_speed = max_speed
        self.accel = max_speed * 0.1
        self.speed = 0
        self.image = image
        self.car = pygame.transform.scale(self.image, (100, 50))
        match self.dir:
            case 'u':
                self.car = pygame.transform.rotate(self.car, -90)
            case 'r':
                self.car = pygame.transform.rotate(self.car, 180)
            case 'd':
                self.car = pygame.transform.rotate(self.car, 90)


    def move(self):
        match self.dir:
            case 'l':
                self.posX -= self.speed
            case 'u':
                self.posY -= self.speed
            case 'r':
                self.posX += self.speed
            case 'd':
                self.posY += self.speed

    def speed_up(self):
        self.speed += self.accel
        if self.speed > self.max_speed:
            self.speed = self.max_speed


    def slow(self):
        self.speed -= self.accel
        if self.speed < 0:
            self.speed = 0


    def collide(self, pos):
        return (pos[0] > self.posX and pos[0] < self.posX + self.car.get_size()[1]) and (pos[1] > self.posY and pos[1] < self.posY +self. self.car.get_size()[1])


    def draw(self, win):
        win.blit(self.car, (self.posX, self.posY))
