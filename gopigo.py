import math
import random
import pygame


class WormBody:
    width = 1080
    height = 720

    py = height / 2
    px = width / 2
    direction = 0
    rot_speed = math.pi / 18
    speed = 10

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))  # , pygame.FULLSCREEN)
        pygame.display.set_caption('gopigo')

        background = pygame.Surface(self.screen.get_size())
        self.background = background.convert()
        self.background.fill((0, 0, 0))

    def render(self):
        self.px %= self.width
        self.py %= self.height

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                raise Exception()

        self.screen.blit(self.background, (0, 0))
        pygame.draw.circle(self.screen, (255, 255, 255), (int(self.px), int(self.py)), 10)

        lx = self.px + self.speed * math.sin(self.direction)
        ly = self.py + self.speed * math.cos(self.direction)
        pygame.draw.line(self.screen, (255, 255, 255), (int(self.px), int(self.py)), (int(lx), int(ly)))

        pygame.display.flip()

    def fwd(self):
        self.px += self.speed * math.sin(self.direction)
        self.py += self.speed * math.cos(self.direction)
        print("fwd")
        self.render()

    def bwd(self):
        self.px -= self.speed * math.sin(self.direction)
        self.py -= self.speed * math.cos(self.direction)
        print("bwd")
        self.render()

    def left_rot(self):
        self.direction -= self.rot_speed % math.pi * 2
        print("left_rot")
        self.render()

    def right_rot(self):
        self.direction += self.rot_speed % math.pi * 2
        print("right_rot")
        self.render()

    def stop(self):
        print("stop")
        self.render()

    def set_speed(self, n):
        self.speed = n
        print("set_speed: ", n)

    def us_dist(self, n):
        print("us_dist: ", n)
        return random.random()

    def volt(self):
        print("volt")
        return 0


worm = WormBody()

fwd = worm.fwd
bwd = worm.bwd
left_rot = worm.left_rot
right_rot = worm.right_rot
stop = worm.stop
set_speed = worm.set_speed
us_dist = worm.us_dist
volt = worm.volt
