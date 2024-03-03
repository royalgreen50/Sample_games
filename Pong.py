import pygame
import sys
import time

# General setup
pygame.init()
clock = pygame.time.Clock()
pygame.mixer.init()

# Create a window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

# Game objects
ball = pygame.Rect(width // 2 - 15, height // 2 - 15, 30, 30)
paddle_a = pygame.Rect(10, height // 2 - 70, 10, 140)
paddle_b = pygame.Rect(width - 20, height // 2 - 70, 10, 140)

# Sound
paddle_sound = pygame.mixer.Sound(r"path\to\paddle_sound.wav")
bounce_sound = pygame.mixer.Sound(r"path\to\bounce_sound.wav")
score_sound = pygame.mixer.Sound(r"path\to\score_sound.wav")

# Game variables
font = pygame.font.Font(None, 36)
ball_speed = [2, 2]
ball_speed_increase = 2.0
ball_init_speed = [2, 2]
paddle_speed = 2
score_a = 0
score_b = 0
game_over = False

def draw_objects():
    """Draw all the game objects on the screen."""
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), paddle_a)
    pygame.draw.rect(screen, (255, 255, 255), paddle_b)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)

def draw_score():
    """Display the score on the screen."""
    score_text = font.render(f"Score: {score_a} - {score_b}", True, (255, 255, 255))
    screen.blit(score_text, (width // 2 - score_text.get_width() // 2, 10))

def paddle_movement(keys, paddle):
    """Move the paddle based on the provided keys."""
    if keys[pygame.K_w] and paddle.y > 0:
        paddle.move_ip(0, -paddle_speed)
    if keys[pygame.K_s] and paddle.y + paddle.height < height:
        paddle.move_ip(0, paddle_speed)

def ball_movement():
    """Move the ball and check for collisions."""
    global score_a, score_b, game_over

    ball.move_ip(ball_speed)

    if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
        ball_speed[0] *= -1
        ball_speed[0] += ball_speed_increase
        paddle_sound.play()

    if ball.top <= 0 or ball.bottom >= height:
        ball_speed[1] *= -1
        ball_speed[1] += ball_speed_increase
        bounce_sound.play()

    if ball.left < 0:
        score_b += 1 
        ball.center = (width // 2, 
                        height // 2) 
        ball_speed[0] *= -1 
        ball_speed = ball_init_speed.copy() 
        # reset speed to initial speed 
        score_sound.play() 
        import pygame
import sys
import time

# General setup
pygame.init()
clock = pygame.time.Clock()
pygame.mixer.init()

# Create a window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

# Game objects
ball = pygame.Rect(width // 2 - 15, height // 2 - 15, 30, 30)
paddle_a = pygame.Rect(10, height // 2 - 70, 10, 140)
paddle_b = pygame.Rect(width - 20, height // 2 - 70, 10, 140)

# Sound
paddle_sound = pygame.mixer.Sound(r"path\to\paddle_sound.wav")
bounce_sound = pygame.mixer.Sound(r"path\to\bounce_sound.wav")
score_sound = pygame.mixer.Sound(r"path\to\score_sound.wav")

# Game variables
font = pygame.font.Font(None, 36)
ball_speed = [2, 2]
ball_speed_increase = 2.0
ball_init_speed = [2, 2]
paddle_speed = 2
score_a = 0
score_b = 0
game_over = False
ball_reset=False
max_score=10

def draw_objects():
    """Draw all the game objects on the screen."""
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), paddle_a)
    pygame.draw.rect(screen, (255, 255, 255), paddle_b)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)

def draw_score():
    """Display the score on the screen."""
    score_text = font.render(f"Score: {score_a} - {score_b}", True, (255, 255, 255))
    screen.blit(score_text, (width // 2 - score_text.get_width() // 2, 10))

def paddle_movement(keys, paddle):
    """Move the paddle based on the provided keys."""
    if keys[pygame.K_w] and paddle.y > 0:
        paddle.move_ip(0, -paddle_speed)
    if keys[pygame.K_s] and paddle.y + paddle.height < height:
        paddle.move_ip(0, paddle_speed)

def ball_movement():
    """Move the ball and check for collisions."""
    global score_a, score_b, game_over

    ball.move_ip(ball_speed)

    if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
        ball_speed[0] *= -1
        ball_speed[0] += ball_speed_increase
        paddle_sound.play()

    if ball.top <= 0 or ball.bottom >= height:
        ball_speed[1] *= -1
        ball_speed[1] += ball_speed_increase
        bounce_sound.play()

    if ball.left < 0:
        score_b += 1
        ball_reset()
    """Check for game over condition."""
if score_b == max_score:
   game_over = True
   #game_over_sound.play()