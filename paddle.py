import pygame
BLACK = (0,0,0)

class Paddle(pygame.sprite.Sprite):

    def __init__(self, colour, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        
        #draw the paddle
        pygame.draw.rect(self.image, colour, [0,0,width,height])
        
        # fetch the rectangle object that has dimentions of the image
        self.rect = self.image.get_rect()
    

    def moveUp(self, pixels):
        self.rect.y -= pixels

        if self.rect.y < 0: # check that the sprite is not too far off the screen
            self.rect.y = 0

    def moveDown(self, pixels):
        self.rect.y += pixels
            # check the sprite has not moved off the screen 
        if self.rect.y > 400:
            self.rect.y = 400
    
