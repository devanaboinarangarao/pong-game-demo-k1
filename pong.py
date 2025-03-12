import pygame

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong')

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Define ball properties
ball_pos = [width // 2, height // 2]
ball_radius = 15
ball_speed = [3, 3]

# Define paddle properties
paddle_width, paddle_height = 10, 100
paddle_speed = 5
left_paddle = pygame.Rect(50, height // 2 - paddle_height // 2, paddle_width, paddle_height)
right_paddle = pygame.Rect(width - 50 - paddle_width, height // 2 - paddle_height // 2, paddle_width, paddle_height)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move ball
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Ball collision with top and bottom
    if ball_pos[1] - ball_radius <= 0 or ball_pos[1] + ball_radius >= height:
        ball_speed[1] = -ball_speed[1]

    # Ball collision with paddles
    if left_paddle.collidepoint(ball_pos) or right_paddle.collidepoint(ball_pos):
        ball_speed[0] = -ball_speed[0]

    # Clear screen
    window.fill(black)

    # Draw ball
    pygame.draw.circle(window, white, ball_pos, ball_radius)

    # Draw paddles
    pygame.draw.rect(window, white, left_paddle)
    pygame.draw.rect(window, white, right_paddle)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()