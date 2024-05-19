import pygame
import random
import math 

pygame.init()

screen_width = 800 
screen_height = 800 
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Hit the astroid game!")

clock = pygame.time.Clock()

# loading images
bg_img = pygame.image.load("images/starbg.png")
alien_img = pygame.image.load("images/alienShip.png")
player_rocket = pygame.image.load("images/spaceRocket.png")
star_img = pygame.image.load("images/star.png")
asteroid50 = pygame.image.load("images/asteroid50.png")
asteroid100 = pygame.image.load("images/asteroid100.png")
asteroid150 = pygame.image.load("images/asteroid150.png")

# loading sound
shoot_sound = pygame.mixer.Sound("sound/shoot.wav")
bangSmall_sound = pygame.mixer.Sound("sound/bangSmall.wav")
bangLarge_sound = pygame.mixer.Sound("sound/bangLarge.wav")

shoot_sound.set_volume(0.25)
bangSmall_sound.set_volume(0.25)
bangLarge_sound.set_volume(0.25)


game_over = False
lives = 5 
score = 0 
rapid_fire = False # cannot press fire button non stop
rf_start = -1
is_sound_on = True 
high_score = 0

class Player(object):
    def __init__(self):
        self.img = player_rocket
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.x = screen_width // 2
        self.y = screen_height // 2 
        self.angle = 0 
        self.rotated_surface = pygame.transform.rotate(self.img, self.angle)
        self.rotated_rect = self.rotated_surface.get_rect()
        self.rotated_rect.center = (self.x,self.y)


