import pygame
import pdb

from snake import Snake, Food, SnakeEatsItselfException

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

BLACK = (0, 0, 0)

pygame.init()
clock = pygame.time.Clock()

SCREEN_HEIGHT = 1200
SCREEN_WIDTH = 1600
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Create a snake
snake = Snake((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
food = Food(SCREEN_WIDTH, SCREEN_HEIGHT) 
direction = [1, 0]
# Run until the user asks to quit
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[K_UP]:
        direction = [0, -1]
    elif keys_pressed[K_DOWN]:
        direction = [0, 1]
    elif keys_pressed[K_LEFT]:
        direction = [-1, 0]
    elif keys_pressed[K_RIGHT]:
        direction = [1, 0]

    snake.change_direction(direction)

    try:
        if snake.get_head_pos() == food.get_pos():
            snake.grow()
            del food
            food = Food(SCREEN_WIDTH, SCREEN_HEIGHT)
        else:
            snake.update()
    except SnakeEatsItselfException:
        print("Snake ate itself!")
        running = False

    head_pos = snake.get_head_pos()
    if head_pos[0] == SCREEN_WIDTH or head_pos[0] == 0:
        running = False
    if head_pos[1] == SCREEN_HEIGHT or head_pos[1] == 0:
        running = False

    screen.fill(BLACK)
    snake.draw(screen)
    food.draw(screen)
    pygame.display.update()

    # Limit to 30 fps
    clock.tick(10)
# Done! Time to quit.
pygame.quit()
