"""
    Name: player.py
    Author:
    Date:
    Purpose: All logic for the player's car is in this class
"""

# Import pygame modules
import pygame
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    """
        Define the player class and methods
    """

#------------------------- INITIALIZE PLAYER OBJECT -----------------#
    def __init__(self):

        # Construct a player object from Sprite class
        super().__init__()

        # Load an image from file
        self.image = pygame.image.load("player.png")

        # Create a surface rectangle the same size as the image
        self.surf = pygame.Surface((50, 100))

        # Gets the rectangle area of the Surface
        # Starts at 0, 0 which is the upper left corner of the surface
        self.rect = self.surf.get_rect()

#------------------------- DRAW PLAYER ON SURFACE -----------------#
    # Draw the Player object on the surface
    def draw(self, surface):
        # blit takes the off stage buffered image and draws it on the screen
        surface.blit(self.image, self.rect)
