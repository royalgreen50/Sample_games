
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

# Game objects
ball = pygame.Rect(screen_width // 2 - 15, screen_height // 2 - 15, 30, 30)
paddle_a = pygame.Rect(10, screen_height // 2 - 70, 10, 140)
paddle_b = pygame.Rect(screen_width - 20, screen_height // 2 - 70, 10, 140)
#Sound
paddle_sound = pygame.mixer.Sound(r'C:\Users\Royal Green\Sample_games\sounds.wav\616541__josheb_policarpio__retro-video-game-sound-effect-short-pluck-version.wav')
bounce_sound = pygame.mixer.Sound(r'C:\Users\Royal Green\Sample_games\sounds.wav\4371__noisecollector__pongblipc4.wav')
score_sound = pygame.mixer.Sound( r'C:\Users\Royal Green\Sample_games\sounds.wav\mixkit-fast-small-sweep-transition-166.wav')
# Game variables
font = pygame.font.Font(None,36)
ball_speed = [2, 2]
ball_speed_increase = 2.0
ball_init_speed= [2,2]
paddle_speed = 2
score_a = 0
score_b = 0

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle_a.move_ip(0, -paddle_speed)
    if keys[pygame.K_s]:
        paddle_a.move_ip(0, paddle_speed)
    if keys[pygame.K_UP]:
        paddle_b.move_ip(0, -paddle_speed)
    if keys[pygame.K_DOWN]:
        paddle_b.move_ip(0, paddle_speed)

    # Ball movement
    ball.move_ip(ball_speed)

    # Collision checking
    if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
        ball_speed[0] *= -1 
        ball_speed_increase
        
        paddle_sound.play()
    
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed[1] *= -1
        ball_speed_increase
        bounce_sound.play()

    # Scoring
    
    
    if ball.left < 0:
        score_b += 1
        ball.center = (screen_width // 2, screen_height // 2)
        ball_speed[0] *= -1
        ball_init_speed
        score_sound.play()
    if ball.right > screen_width:
        score_a += 1
        ball.center = (screen_width // 2, screen_height // 2)
        ball_speed[0] *= -1
        ball_init_speed
        score_sound.play()
  

    # Drawing everything
    screen.fill(pygame.Color('purple'))
    
    # Render scores
    score_text_a = font.render('Player 1: ' + str(score_a), True, ('yellow'))
    score_text_b = font.render(' Player 2: ' + str(score_b), True, ('yellow'))
    screen.blit(score_text_a, (10,10))
    screen.blit(score_text_b, (405,10))

    #Add colors
    pygame.draw.rect(screen, pygame.Color('blue'), paddle_a)
    pygame.draw.rect(screen, pygame.Color('blue'), paddle_b)
    pygame.draw.ellipse(screen, pygame.Color('green'), ball)
    pygame.draw.aaline(screen, pygame.Color('yellow'), (screen_width // 2, 0), (screen_width // 2, screen_height))

    pygame.display.flip()
    clock.tick(60)
