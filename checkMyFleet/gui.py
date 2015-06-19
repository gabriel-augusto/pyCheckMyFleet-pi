__author__ = 'gabriel'

import sys
import pygame
from threading import Thread

white = (255, 255, 255)
black = (0, 0, 0)
size = width, height = 800, 600
space = 20
rec_width = (width - (4 * space)) / 3
rec_height = (height - (3 * space)) / 2


def is_float(value):
    try:
        value = float(value)
        return True
    except:
        return False


class Pane(object):
    def __init__(self, parameters):
        pygame.init()
        self.LABEL = 1
        self.PARAMETER = 2
        self.font1 = pygame.font.SysFont('Arial', 25)
        self.font2 = pygame.font.SysFont('Arial', 30)
        pygame.display.set_caption('OBD GUI')
        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        self.xpos = 0
        self.ypos = 0
        self.parameters = parameters

    def add_rec(self, x, y):
        pygame.draw.rect(self.screen, white, [x, y, rec_width, rec_height], 2)

    def add_text(self, text, x, y, font_type):
        if font_type == 1:
            self.screen.blit(self.font1.render(text, True, (255, 255, 255)), (x, y))
        if font_type == 2:
            self.screen.blit(self.font2.render(text, True, (255, 255, 255)), (x, y))

    def draw_interface(self):
        data_list = [('Velocidade:', self.parameters.speed), ('RPM:', self.parameters.rpm),
                     ('Consumo:', self.parameters.fuel), ('Combustivel:', self.parameters.level),
                     ('Ethanol', self.parameters.ethanol)]
        self.screen.fill(black)
        self.xpos = 0
        count = 0
        for data in data_list:
            if count % 2:
                self.ypos += (rec_height + space)
            else:
                self.ypos = space
                self.xpos += space

            self.add_rec(self.xpos, self.ypos)

            if is_float(data[1].value):
                data[1].value = round(data[1].value, 2)

            self.add_text(str(data[0]), self.xpos + 10, self.ypos + 10, self.LABEL)
            self.add_text(data[1].__str__(), self.xpos + 10, self.ypos + (rec_height / 2 - 10), self.PARAMETER)

            if count % 2:
                self.xpos += rec_width
            count += 1


class Render(Thread):
    def __init__(self, parameters):
        Thread.__init__(self)
        self.pan = Pane(parameters)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
            self.pan.draw_interface()
            pygame.display.flip()