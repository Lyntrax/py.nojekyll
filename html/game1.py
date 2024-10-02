import pygame
import sys
import random

pygame.init()

screen_width, screen_height = 400, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

black = (0, 0, 0)
white = (255, 255, 255)
bird_color = (255, 255, 0)
pipe_color = (0, 255, 0)

background_image = pygame.image.load('moon.jfif').convert()

bird_width, bird_height = 34, 24
bird_x, bird_y = 50, screen_height // 2
bird_velocity = 0
gravity = 0.5
bird_flap = -10

pipe_width = 80
pipe_height = 500
pipe_gap = 150
pipe_velocity = -5
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks() - pipe_frequency

pipes = []

font = pygame.font.Font(None, 36)

def draw_bird(x, y):
    pygame.draw.rect(screen, bird_color, [x, y, bird_width, bird_height])

def draw_pipes(pipes):
    for pipe in pipes:
        pygame.draw.rect(screen, pipe_color, pipe['rect'])

def draw_score(score):
    text = font.render(f'Score: {score}', True, white)
    screen.blit(text, (10, 10))

def game_loop():
    global bird_y, bird_velocity, last_pipe, pipes

    clock = pygame.time.Clock()
    score = 0
    game_over = False
    pipe_timer = pygame.time.get_ticks()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not game_over:
                bird_velocity = bird_flap
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r and game_over:
                return

        screen.blit(background_image, (0, 0))

        if not game_over:
            bird_velocity += gravity
            bird_y += bird_velocity
            if bird_y > screen_height - bird_height:
                bird_y = screen_height - bird_height
                bird_velocity = 0
            if bird_y < 0:
                bird_y = 0
                bird_velocity = 0

            current_time = pygame.time.get_ticks()
            if current_time - last_pipe > pipe_frequency:
                pipe_height = random.randint(100, screen_height - pipe_gap - 100)
                pipes.append({
                    'rect': pygame.Rect(screen_width, 0, pipe_width, pipe_height),
                    'passed': False
                })
                last_pipe = current_time

            for pipe in pipes:
                pipe['rect'].x += pipe_velocity
                if pipe['rect'].x < -pipe_width:
                    pipes.remove(pipe)
                if not pipe['passed'] and pipe['rect'].x + pipe_width < bird_x:
                    pipe['passed'] = True
                    score += 1

                if bird_x + bird_width > pipe['rect'].x and bird_x < pipe['rect'].x + pipe_width:
                    if bird_y < pipe['rect'].height or bird_y + bird_height > pipe['rect'].height + pipe_gap:
                        game_over = True

            draw_bird(bird_x, bird_y)
            draw_pipes(pipes)
            draw_score(score)

        pygame.display.flip()
        clock.tick(30)

if __name__ == "_main_":
    game_loop()