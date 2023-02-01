import pygame

class Increment(object):
    def __init__(self, pos, font, template, value, initial, color):
        self.max = initial
        self.font = font
        self.color = color
        self.pos = pos
        self.value = value
        self.template = template
        self.text = self.font.render(template + str(self.max), True, self.color)


    def increment(self):
        self.max += self.value
        self.set_text(self.max)


    def decrement(self):
        self.max -= self.value if self.max > self.value else 0
        self.set_text(self.max)


    def set_text(self, text):
        self.text = self.font.render(self.template + str(text), True, self.color)

    
    def draw(self, WIN):
        WIN.blit(self.text, (self.pos[0], self.pos[1]))