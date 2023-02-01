import pygame

class Button(object):
    def __init__(self, pos, size, color, font, text, textColor):
        self.pos = pos
        self.size = size
        self.color = color
        self.hovered = False
        self.description = font.render(text, True, textColor)

    def hover(self, pos):
        return (pos[0] > self.pos[0] and pos[0] < self.pos[0] + self.size[0]) and (pos[1] > self.pos[1] and pos[1] < self.pos[1] + self.size[1])
    
    def draw(self, WIN):
        pygame.draw.rect(WIN, self.color, pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1]))
        WIN.blit(self.description, (self.pos[0], self.pos[1]))
