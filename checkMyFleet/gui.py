__author__ = 'gabriel'

import sys
import pygame
import obd_parameters
import obd_reader
import obd_recorder

white = (255, 255, 255)
black = (0, 0, 0)
size = width, height = 800, 600
space = 20
rec_width = (width - (4 * space)) / 3
rec_height = (height - (3 * space)) / 2


class Pane(object):
    def __init__(self):
        pygame.init()
        self.LABEL = 1
        self.PARAMETER = 2
        self.font1 = pygame.font.SysFont('Arial', 25)
        self.font2 = pygame.font.SysFont('Arial', 35)
        pygame.display.set_caption('OBD GUI')
        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        self.xpos = 0
        self.ypos = 0
        self.parameters = obd_parameters.ObdParameters()
        self.reader = obd_reader.ObdReader()
        self.recorder = obd_recorder.OBDRecorder()

    def add_rec(self, x, y):
        pygame.draw.rect(self.screen, white, [x, y, rec_width, rec_height], 2)

    def add_text(self, text, x, y, font_type):
        if font_type == 1:
            self.screen.blit(self.font1.render(text, True, (255, 255, 255)), (x, y))
        if font_type == 2:
            self.screen.blit(self.font2.render(text, True, (255, 255, 255)), (x, y))


    def draw_interface(self):
        self.screen.fill(black)
        self.xpos = 0
        data = [('RPM:', str(self.parameters.rpm.value)),
                ('Km/h:', str(self.parameters.speed.value)),
                ('Economia:', str(self.parameters.econometer)),
                ('Acelerador:', str(self.parameters.throttle.value)),
                ('Distancia:', str(self.parameters.distance.value)),
                ('', '')]

        for count in range(0, 3):
            self.xpos += space
            self.ypos = space
            self.add_rec(self.xpos, self.ypos)
            self.add_text(data[count*2][0], self.xpos + 10, self.ypos + 10, self.LABEL)
            self.add_text(data[count*2][1], self.xpos + 70, self.ypos + (rec_height / 2 - 10),
                          self.PARAMETER)
            self.ypos += (rec_height + space)
            self.add_rec(self.xpos, self.ypos)
            self.add_text(data[count*2+1][0], self.xpos + 10, self.ypos + 10, self.LABEL)
            self.add_text(data[count*2+1][1], self.xpos + 70, self.ypos + (rec_height / 2 - 10),
                          self.PARAMETER)
            self.xpos += rec_width


if __name__ == '__main__':
    pan = Pane()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

        pan.reader.read_obd()
        pan.recorder.record_data()
        pan.draw_interface()
        pygame.display.flip()
