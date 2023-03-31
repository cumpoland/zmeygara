import pygame
import random

# initialize pygame
pygame.init()

# define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# set up the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# set up the clock
clock = pygame.time.Clock()

# set up the snake
snake_block_size = 10
snake_speed = 15
snake_list = []
snake_length = 1
snake_x = SCREEN_WIDTH // 2
snake_y = SCREEN_HEIGHT // 2

# set up the food
food_block_size = 10
food_x = round(random.randrange(0, SCREEN_WIDTH - food_block_size) / 10.0) * 10.0
food_y = round(random.randrange(0, SCREEN_HEIGHT - food_block_size) / 10.0) * 10.0

# define a function to draw the snake
def draw_snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, BLACK, [x[0], x[1], snake_block_size, snake_block_size])

# define a function to display the score
def display_score(score):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: " + str(score), True, RED)
    screen.blit(text, [0, 0])

# set up the game loop
game_over = False
score = 0

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # get the current state of the arrow keys
    keys = pygame.key.get_pressed()

    # move the snake
    if keys[pygame.K_LEFT]:
        snake_x -= snake_block_size
    if keys[pygame.K_RIGHT]:
        snake_x += snake_block_size
    if keys[pygame.K_UP]:
        snake_y -= snake_block_size
    if keys[pygame.K_DOWN]:
        snake_y += snake_block_size

    # check for collisions with the walls
    if snake_x < 0 or snake_x >= SCREEN_WIDTH or snake_y < 0 or snake_y >= SCREEN_HEIGHT:
        game_over = True

    # check for collisions with the food
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, SCREEN_WIDTH - food_block_size) / 10.0) * 10.0
        food_y = round(random.randrange(0, SCREEN_HEIGHT - food_block_size) / 10.0) * 10.0
        snake_length += 1
        score += 10

    # move the snake
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    # check for collisions with the snake's own body
    for x in snake_list[:-1]:
        if x == snake_head:
            game_over = True

    # draw the screen
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, [food_x, food_y, food_block_size, food_block_size])
    draw_snake(snake_block_size, snake_list)
    display_score(score)
    pygame.display.update()

    # set the game
