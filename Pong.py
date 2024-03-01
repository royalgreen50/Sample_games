import pygame
import sys

# General setup
pygame.init()
clock = pygame.time.Clock()
pygame.mixer.init()

# Setting up main window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

ball = pygame.Rect(screen_width // 2 - 15, screen_height // 2 - 15, 30, 30)
paddle_a = pygame.Rect(10, screen_height // 2 - 70, 10, 140)
paddle_b = pygame.Rect(screen_width - 20, screen_height // 2 - 70, 10, 14