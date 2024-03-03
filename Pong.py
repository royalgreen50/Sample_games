import pygame
import random
import sys
import time



pygame.init()

# Set up some constants
pygame.display.set_caption("Pong")  # Change the title here
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BALL_RADIUS = 10
ball = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed = [2, 2]
paddle_height = 100
paddle_width = 25
brick_height = paddle_height
brick_width = paddle_width
paddle_speed = 3
paddle1_pos = [5, SCREEN_HEIGHT // 2 - paddle_height // 2]
paddle2_pos = [SCREEN_WIDTH - 5 - 2 * paddle_width, SCREEN_HEIGHT // 2 - paddle_height // 2]
WIDTH = SCREEN_WIDTH
HEIGHT = SCREEN_HEIGHT
player1_score = 0
player2_score = 0
font = pygame.font.Font(None, 36)
paddle1_move = 0
paddle2_move = 0
ball_speed_increment = 1
max_ball_speed = 3

# Create the bricks
bricks = []
for i in range(5):  # Create 50 bricks
    brick_x = random.randint(0, SCREEN_WIDTH - brick_width)
    brick_y = random.randint(0, SCREEN_HEIGHT // 2)
    bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))

def reset_ball():
    global ball_speed, ball
    ball.x, ball.y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
    ball_speed[0] = random.choice([-3, 3])
    ball_speed[1] = -3

# Create the paddles
paddle1_color = (255, 0, 0)
paddle2_color = (0, 0, 255)

# Initialize clock
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                paddle1_move = -paddle_speed
            elif event.key == pygame.K_s:
                paddle1_move = paddle_speed
            elif event.key == pygame.K_RIGHT:
                paddle2_move = -paddle_speed
            elif event.key == pygame.K_LEFT:
                paddle2_move = paddle_speed
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_a, pygame.K_s):
                paddle1_move = 0
            elif event.key in (pygame.K_RIGHT, pygame.K_LEFT):
                paddle2_move = 0

    # Move the paddles
    paddle1_pos[1] += paddle1_move
    paddle2_pos[1] += paddle2_move

    # Move the ball
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Check for ball collision with top and bottom
    if ball.top < 0 or ball.bottom > SCREEN_HEIGHT:
        ball_speed[1] *= -1

    # Check for ball collision with bricks
    for brick in bricks:
        if ball.colliderect(brick):
            ball_speed[1] *= -1
            ball_speed[0] += random.choice([-1, 1]) * ball_speed_increment
            if ball_speed[0] > max_ball_speed:
                ball_speed[0] = max_ball_speed
            elif ball_speed[0] < -max_ball_speed:
                ball_speed[0] = -max_ball_speed
            if ball_speed[1] > max_ball_speed:
                ball_speed[1] = max_ball_speed
            elif ball_speed[1] < -max_ball_speed:
                ball_speed[1] = -max_ball_speed
            bricks.remove(brick)
            reset_ball()
            break  # Break the loop to prevent further collisions

    # Check for ball collision with paddles
    if ball.colliderect(pygame.Rect(paddle1_pos[0], paddle1_pos[1], paddle_width, paddle_height)):
        ball_speed[0] *= -1
    elif ball.colliderect(pygame.Rect(paddle2_pos[0], paddle2_pos[1], paddle_width, paddle_height)):
        ball_speed[0] *= -1

    # Check for ball leaving the screen on the left or right side
    if ball.left < 0 or ball.right > SCREEN_WIDTH:
        pygame.time.wait(3000)  # Pause for 3 seconds
        if ball.left < 0:
            player2_score += 1
        else:
            player1_score += 1
        
        reset_ball()
        pygame.display.flip()  # Update the display before pausing

    # Draw everything
    screen.fill((0, 0, 0))  # Black background color
    pygame.draw.circle(screen, (128, 128 , 0), ball.center, BALL_RADIUS)
    pygame.draw.rect(screen, paddle1_color, pygame.Rect(paddle1_pos[0], paddle1_pos[1], paddle_width, paddle_height))
    pygame.draw.rect(screen, paddle2_color, pygame.Rect(paddle2_pos[0], paddle2_pos[1], paddle_width, paddle_height))

    # Draw the score board
    score_text = font.render(f"Player 1: {player1_score} Player 2: {player2_score}", True, (0, 0, 0))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 5))

    # Draw the bricks
    brick_color = (255, 0, 0)  # Choose a color for the bricks
    for brick in bricks:
        pygame.draw.rect(screen, brick_color, brick)

    # Flip the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
    pygame.draw.circle(screen, (128, 128 , 0), ball.center, BALL_RADIUS)
    pygame.draw.rect(screen, paddle1_color, pygame.Rect(paddle1_pos[0], paddle1_pos[1], paddle_width, paddle_height))
    pygame.draw.rect(screen, paddle2_color, pygame.Rect(paddle2_pos[0], paddle2_pos[1], paddle_width, paddle_height))

    # Draw the score board
    score_text = font.render(f"Player 1: {player1_score} Player 2: {player2_score}", True, (0, 0, 0))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 5))

    # Draw the bricks
    brick_color = (255, 0, 0)  # Choose a color for the bricks
    for brick in bricks:
        pygame.draw.rect(screen, brick_color, brick)
import pygame

# Initialize Pygame
pygame.init()


pygame.quit()

    # Flip the display
pygame.display.flip()

    # Cap the frame rate
clock.tick(60)
