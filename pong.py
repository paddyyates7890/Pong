# import the pygame libries 
import pygame
from paddle import Paddle # import paddle class
from ball import Ball
# initilise pygame
pygame.init()

# set some colour variables that are needed 
BLACK = (0,0,0)
WHITE = (225,225,22)

# set the size of the screen and display 
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

# initialisation of the paddles 
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200
 
paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(WHITE,  10, 10)
ball.rect.x = 670
ball.rect.y = 195

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

# set the loop to carry on until the user exits the game
carryOn = True

# the clock pygame uses for the screen updates
clock = pygame.time.Clock()

scoreA = 0
scoreB = 0

#-------- main loop -------
while carryOn:
    # event loop
    for event in pygame.event.get(): # user did something 
        if event.type == pygame.QUIT: # if the user clicked close
            carryOn = False # exit the loop end the game
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x:
                carryOn=False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)

    # game logic
    all_sprites_list.update()

    if ball.rect.x>=690:
        scoreA+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        scoreB+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1] 
 
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce() 

    # drawing sprites
    screen.fill(BLACK)
    # draw the net
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    
    all_sprites_list.draw(screen)
    
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250,10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420,10))

    pygame.display.flip()

    clock.tick(60) # limit to 60 frames per second


pygame.quit() # the game engine willl stop
