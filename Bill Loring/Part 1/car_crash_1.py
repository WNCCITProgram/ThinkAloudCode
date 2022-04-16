"""
    Name: car_crash.py
    Author:
    Date:
    Purpose: Draw the player"s car
"""

# Import pygame and sys modules
import pygame
import sys
# Import player class
import player

# Create a Player object
player = player.Player()


class CarCrash:

    def __init__(self):
        """ Setup the object data fields """
        # Setup color and screen size constants
        self.WHITE = (255, 255, 255)
        self.SURFACE_WIDTH = 400
        self.SURFACE_HEIGHT = 600
        # Constant for Frames Per Second (FPS
        self.FPS = 60
        # Setup a computer clock object
        self.FramePerSec = pygame.time.Clock()
        # Initialize pygame for action
        pygame.init()

        # Create the game window, color and caption
        self.surface = pygame.display.set_mode(
            (self.SURFACE_WIDTH, self.SURFACE_HEIGHT)
        )
        self.surface.fill(self.WHITE)
        pygame.display.set_caption("Car Crash")

    def run_game(self):
        """ Start the infinite Game Loop """
        while True:
            # Closing the program by clicking the X
            # causes the QUIT event to be fired
            for event in pygame.event.get():

                # Exit game if window is closed
                if event.type == pygame.QUIT:
                    # Quit Pygame
                    pygame.quit()
                    # Exit Python
                    sys.exit()

            # Fill the surface with white to clear the screen
            self.surface.fill(self.WHITE)

            # Draw the player sprite on the surface
            player.draw(self.surface)

            # Redraw the surface
            pygame.display.update()

            # How often our game loop executes
            self.FramePerSec.tick(self.FPS)


def main():
    # Create game instance
    car_crash = CarCrash()
    # Start the game
    car_crash.run_game()


# Start the program
main()
