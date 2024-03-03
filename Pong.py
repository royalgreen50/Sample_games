import pygame
import sys
import random
import time

# Initialize pygame and mixer
pygame.init()
pygame.mixer.init()

# Set up colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up some constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_RADIUS = 10
PADDLE_HEIGHT = 100
PADDLE_WIDTH = 25
PADDLE_SPEED = 3
PLAYER1_SCORE = 0
PLAYER2_SCORE = 0
paddle1_color = BLUE
paddle2_color = GREEN

# Set up the ball and paddles
ball = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed = [random.choice((-2, 2)), random.choice((-2, 2))]
paddle1 = pygame.Rect(5, SCREEN_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(SCREEN_WIDTH - 5 - PADDLE_WIDTH, SCREEN_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle1_speed = [0, 0]
paddle2_speed = [0, 0]

# Load the music and sound effects
pygame.mixer.music.load('sounds.wav/2020-04-24_-_Too_Much_Funk_-_FesliyanStudios_-_Steve_Oaks.mp3')
bounce_sound = pygame.mixer.Sound('sounds.wav/4371__noisecollector__pongblipc4.wav')
score_sound = pygame.mixer.Sound('sounds.wav/mixkit-fast-small-sweep-transition-166.wav')

# Play the background music
pygame.mixer.music.play(-1)

# Create a custom event for changing the paddle color back
CHANGE_COLOR_BACK_EVENT = pygame.USEREVENT + 1

# Set up the display
pygame.display.set_caption("Pong")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def reset_ball():
    global ball, ball_speed
    ball.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    ball_speed = [random.choice((-2, 2)), random.choice((-2, 2))]

# Game loop
while True:
    screen.fill((0, 0, 0))  # Clear the screen by filling it with black

    # Draw the center line
    pygame.draw.line(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT), 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                paddle2_speed[1] = -PADDLE_SPEED
            elif event.key == pygame.K_DOWN:
                paddle2_speed[1] = PADDLE_SPEED
            elif event.key == pygame.K_w:
                paddle1_speed[1] = -PADDLE_SPEED
            elif event.key == pygame.K_s:
                paddle1_speed[1] = PADDLE_SPEED
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                paddle2_speed[1] = 0
            elif event.key in (pygame.K_w, pygame.K_s):
                paddle1_speed[1] = 0

    # Update paddle positions
    paddle1.move_ip(paddle1_speed)
    paddle2.move_ip(paddle2_speed)

    # Keep paddles inside the screen
    if paddle1.top < 0:
        paddle1.top = 0
    if paddle1.bottom > SCREEN_HEIGHT:
        paddle1.bottom = SCREEN_HEIGHT
    if paddle2.top < 0:
        paddle2.top = 0
    if paddle2.bottom > SCREEN_HEIGHT:
        paddle2.bottom = SCREEN_HEIGHT

    # Update ball position
    ball.move_ip(ball_speed)

    # Ball collision with paddles
    if ball.colliderect(paddle1):
        ball_speed[0] = abs(ball_speed[0])
        bounce_sound.play()
    elif ball.colliderect(paddle2):
        ball_speed[0] = -abs(ball_speed[0])
        bounce_sound.play()

    # Ball collision with top and bottom
    if ball.top < 0 or ball.bottom > SCREEN_HEIGHT:
        ball_speed[1] = -ball_speed[1]
        bounce_sound.play()

    # Ball goes off to the sides
    if ball.left < 0:
        PLAYER2_SCORE += 1
        score_sound.play()
        pygame.time.set_timer(CHANGE_COLOR_BACK_EVENT, 5000)  # Set a timer for 5 seconds
        reset_ball()
    elif ball.right > SCREEN_WIDTH:
        PLAYER1_SCORE += 1
        score_sound.play()
        
        reset_ball()

    # Draw the ball and paddles
    pygame.draw.rect(screen, WHITE, ball)
    pygame.draw.rect(screen, paddle1_color, paddle1)
    pygame.draw.rect(screen, paddle2_color, paddle2)

    # Draw the scores
    score_text = f"Player 1: {PLAYER1_SCORE}   Player 2: {PLAYER2_SCORE}"
    score_surface = pygame.font.Font(None, 32).render(score_text, True, WHITE)
    screen.blit(score_surface, (SCREEN_WIDTH // 2 - score_surface.get_width() // 2, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
