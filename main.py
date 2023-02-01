"""
author @Ivan Hart
Name - Traffic Simulator
"""

import os
import pygame
from color import Color
from car import Car
from light import Light
from lane import Lane
from button import Button
from timer import Timer

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Traffic Simulator")

delta = pygame.time.Clock()
time = 0
max_time = 500
FPS = 60
run = True

backdrop = pygame.image.load(os.path.join("backdrop.png"))
image = pygame.image.load(os.path.join("car.png"))

cars = []
lights = []

font = pygame.font.Font(pygame.font.get_default_font(), 18)
timerPos = (535, 50)
timer = Timer(timerPos, font, Color.black)

button_font = pygame.font.Font(pygame.font.get_default_font(), 50)

incrementButton = Button((530, timerPos[1] + 30), (50, 50), Color.green, button_font, "+", Color.black, (540, timerPos[1] + 30))
decrementButton = Button((620, timerPos[1] + 30), (50, 50), Color.blue, button_font, "-", Color.black, (640, timerPos[1] + 30))

def build_object(index):
    return Car(Lane.car_pos[index], Lane.dir[index], 1, image)


def build_object_lists():
    for i in range(4):
        light = Light(Lane.light_pos[i], Lane.dir[i], Color.red if i % 2 == 0 else Color.green)
        lights.append(light)
        cars.append(build_object(i))


def check_off_screen(car):
    return car.posX < -100 or car.posX > 600 or car.posY < -100 or car.posY > 600


def check_time():
    return True if time > timer.max_time else False


def handle_key_input(event):
    global max_time
    global run
    match event.key:
        case pygame.K_DOWN:
            timer.increment_timer
        case pygame.K_UP:
            timer.decrement_timer()
        case pygame.K_ESCAPE:
            run = False


def mouse_click():
    global max_time
    if incrementButton.hovered:
        timer.increment_timer()
    elif decrementButton.hovered:
        timer.decrement_timer()


def mouse_hover(pos):
    if incrementButton.hover(pos):
        incrementButton.hovered = True
        incrementButton.color = Color.light_green
    elif decrementButton.hover(pos):
        decrementButton.hovered = True
        decrementButton.color = Color.light_green
    else:
        decrementButton.hovered = False
        decrementButton.color = Color.green
        incrementButton.hovered = False
        incrementButton.color = Color.green


def render():
    WIN.fill(Color.white)
    WIN.blit(backdrop, (0, 0))
    for i in range(4):
        cars[i].draw(WIN)
        lights[i].draw(WIN)
    pygame.draw.rect(WIN, Color.white, pygame.Rect(500, 0, 200, 500))
    timer.draw(WIN)
    incrementButton.draw(WIN)
    decrementButton.draw(WIN)


def update():
    global time
    for i in range(4):
        if check_time():
            for l in lights:
                l.change()
            time = 0
        
        if (lights[i].check(cars[i]) and lights[i].color == Color.red):
            cars[i].slow()
        else:
            cars[i].speed_up()

        if check_off_screen(cars[i]):
            cars[i] = build_object(i)

        cars[i].move()


def main():
    global time
    global run
    build_object_lists()
    while run:
        delta.tick(FPS)
        for event in pygame.event.get():
            match event.type:
                case pygame.KEYDOWN:
                    handle_key_input(event)
                case pygame.MOUSEBUTTONUP:
                    mouse_click()
                case pygame.QUIT:
                    run = False
        mouse_hover(pygame.mouse.get_pos())
        render()
        update()
        pygame.display.update()
        time += 1


if __name__ == "__main__":
    main()
