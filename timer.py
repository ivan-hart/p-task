import pygame

class Timer(object):
    def __init__(self, font, color):
        self.max_time = 500
        self.font = font
        self.color = color
        self.time_text = self.font.render("Light timer: " + str(self.max_time), True, self.color)

    def increment_timer(self):
        self.max_time += 100
        self.set_time_text(self.max_time)


    def decrement_timer(self):
        self.max_time -= 100 if self.max_time >= 100 else 0
        self.set_time_text(self.max_time)

    def set_time_text(self, text):
        self.time_text = self.font.render("Light timer: " + str(text), True, self.color)

    
    def draw(self, WIN):
        WIN.blit(self.time_text, (520, 50))