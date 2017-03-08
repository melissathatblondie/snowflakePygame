"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
bg = pygame.image.load("gwcpic3.png")
pygame.display.set_caption("Snow")

color = WHITE
# Your SnowFlake class
class SnowFlake:
    
    def __init__(self, x_location, y_location, fall_Speed, flake_size):  
    # Attributes of the bouncing ball 
        self.x_location = x_location
        self.y_location = y_location  
        self.fall_Speed = fall_Speed 
        self.flake_size = flake_size
        
    
    	
   
    def fall(self, screen, color, width, height):
    	
    	self.fall_Speed = random.randint(1,2)
    	color = WHITE
    	self.y_location += self.fall_Speed
    	pygame.draw.circle(screen, WHITE, [self.x_location, self.y_location], self.flake_size)
    	
    	if self.y_location > 500:
    		self.y_location = random.randint(-40, -10)
    		self.x_location = random.randint(0,750)



        

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Speed
speed = 2

# Snow List
snow_list = []

for i in range(random.randint(500,700)):
	x = random.randint(0,700)
	y = random.randint(0, 500)
	rad = random.randint(3,6)
	snowball = SnowFlake(x, y, 2, rad)
	snow_list.append(snowball)
	

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.blit(bg, (0,0))

    # --- Drawing code should go here
    # Begin Snow
    for k in snow_list:
    	k.fall(screen, WHITE, 700, 500)

    
 

    # End Snow
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
