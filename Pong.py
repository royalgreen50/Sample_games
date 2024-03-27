import pygame
import random
import sys

# Initialize pygame and mixer
pygame.init()
pygame.mixer.init()

# Set up colors and constants
WHITE, RED, GREEN, BLUE = (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255)
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BALL_RADIUS, PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_SPEED = 10, 100, 25, 3
PLAYER1_SCORE, PLAYER2_SCORE = 0, 0
BALL_SPEED = [random.choice((-2, 2)), random.choice((-2, 2))]

# Paths to sound files
music_path = 'C:/Users/Royal Green/Funky pong/Sample_games/sounds.wav/2020-04-24_-_Too_Much_Funk_-_FesliyanStudios_-_Steve_Oaks.mp3'
bounce_sound_path = 'C:/Users/Royal Green/Funky pong/Sample_games/sounds.wav/4371__noisecollector__pongblipc4.wav'
score_sound_path = 'C:/Users/Royal Green/Funky pong/Sample_games/sounds.wav/mixkit-fast-small-sweep-transition-166.wav'

# Load and play background music
pygame.mixer.music.load(music_path)
pygame.mixer.music.play(-1)

# Load sound effects
bounce_sound = pygame.mixer.Sound(bounce_sound_path)
score_sound = pygame.mixer.Sound(score_sound_path)

# Custom event
CHANGE_COLOR_BACK_EVENT = pygame.USEREVENT + 1

# Display setup
pygame.display.set_caption("Pong")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def reset_ball():
    global ball, BALL_SPEED
    ball.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    BALL_SPEED = [random.choice((-2, 2)), random.choice((-2, 2))]

paddle1 = pygame.Rect(50, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(SCREEN_WIDTH - PADDLE_WIDTH - 50, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(0, 0, BALL_RADIUS * 2, BALL_RADIUS * 2)

while True:
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT), 1)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]: paddle2.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN]: paddle2.y += PADDLE_SPEED
    if keys[pygame.K_w]: paddle1.y -= PADDLE_SPEED
    if keys[pygame.K_s]: paddle1.y += PADDLE_SPEED

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    paddle1.clamp_ip(screen.get_rect())
    paddle2.clamp_ip(screen.get_rect())
    ball.move_ip(BALL_SPEED)

    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        BALL_SPEED[0] *= -1
        bounce_sound.play()

    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        BALL_SPEED[1] *= -1
        bounce_sound.play()

    if ball.left < 0:
        PLAYER2_SCORE += 1
        score_sound.play()
        reset_ball()
    elif ball.right > SCREEN_WIDTH:
        PLAYER1_SCORE += 1
        score_sound.play()
        reset_ball()

    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)

    score_text = f"Player 1: {PLAYER1_SCORE}   Player 2: {PLAYER2_SCORE}"
    score_surface = pygame.font.Font(None, 32).render(score_text, True, WHITE)
    screen.blit(score_surface, (SCREEN_WIDTH // 2 - score_surface.get_width() // 2, 10))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

