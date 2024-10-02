import pygame
import sys

pygame.init()


size = (300, 300)
screen = pygame.display.set_mode((300,300))  
pygame.display.set_caption("bopols")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


board = [['' for _ in range(3)] for _ in range(3)]
player = 'B'


font = pygame.font.Font(None, 74)


def draw_board():
    screen.fill(WHITE)
    for row in range(1, 3):
        pygame.draw.line(screen, BLACK, (0, row * 100), (300, row * 100), 2)
        pygame.draw.line(screen, BLACK, (row * 100, 0), (row * 100, 300), 2)


def draw_marks():
    for row in range(3):
        for col in range(3):
            mark = board[row][col]
            if mark:
                color = RED if mark == 'B' else BLUE
                text = font.render(mark, True, color)
                screen.blit(text, (col * 100 + 25, row * 100 + 15))


def check_winner():
    
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '':
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return board[0][2]

    return None


def check_draw():
    for row in board:
        if '' in row:
            return False
    return True


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row, col = y // 100, x // 100
            if board[row][col] == '':
                board[row][col] = player
                if check_winner():
                    print(f"Player {player} wins!")
                    pygame.quit()
                    sys.exit()
                if check_draw():
                    print("It's a draw!")
                    pygame.quit()
                    sys.exit()
                player = 'O' if player == 'B' else 'B'

  
    draw_board()
    draw_marks()

    pygame.display.update()
