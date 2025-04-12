
#Pip install pygame

import pygame
import sys
import random

pygame.init()

CELL_SIZE = 20
FPS = 10
WIDTH = 28 * CELL_SIZE
HEIGHT = 31 * CELL_SIZE + 60

BLACK   = (0, 0, 0)
BLUE    = (33, 33, 222)
YELLOW  = (255, 255, 0)
RED     = (255, 0, 0)
PINK    = (255, 100, 150)
CYAN    = (0, 255, 255)
ORANGE  = (255, 165, 0)
WHITE   = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")
clock = pygame.time.Clock()

try:
    dot_sound = pygame.mixer.Sound("dot.wav")
    death_sound = pygame.mixer.Sound("dead_one.wav")
    finish_sound = pygame.mixer.Sound("dead.wav")
    background_music = pygame.mixer.Sound("music.mp3")
except Exception as e:
    dot_sound = None
    death_sound = None
    finish_sound = None
    background_music = None

# Start background music
if background_music:
    background_music.set_volume(0.2)
    background_music.play(loops=-1)

maze_raw = [
    "1111111111111111111111111111",
    "1000000000000000000000000001",
    "1011110111110111110111110101",
    "1011110111110111110111110101",
    "1000000000000000000000000001",
    "1011110111010111010111110101",
    "1000000100010001000100000001",
    "1111110111010111010111111111",
    "0000000000000000000000000000",
    "1111110111010111010111111111",
    "1000000100010001000100000001",
    "1011110111110111110111110101",
    "1000000000000000000000000001",
    "1011110111110111110111110101",
    "1011110111110111110111110101",
    "1000000000000000000000000001",
    "1111111111111111111111111111"
]

maze = []
for row in maze_raw:
    line = []
    for char in row:
        if char == "1":
            line.append(1)
        else:
            line.append(2)
    maze.append(line)

pacman_pos = [1, 1]
pacman_dir = [0, 0]
lives = 3
score = 0
level = 1

ghosts = [
    {"pos": [len(maze[0]) - 2, 1], "color": RED},
    {"pos": [1, len(maze) - 2], "color": PINK},
    {"pos": [len(maze[0]) - 2, len(maze) - 2], "color": CYAN},
    {"pos": [len(maze[0]) // 2, len(maze) // 2], "color": ORANGE},
]

def draw_maze():
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE + 60, CELL_SIZE, CELL_SIZE)
            if cell == 1:
                pygame.draw.rect(screen, BLUE, rect)
            elif cell == 2:
                pygame.draw.circle(screen, WHITE, rect.center, 3)

def move_pacman():
    global score
    new_x = pacman_pos[0] + pacman_dir[0]
    new_y = pacman_pos[1] + pacman_dir[1]
    if 0 <= new_y < len(maze) and 0 <= new_x < len(maze[0]):
        if maze[new_y][new_x] != 1:
            pacman_pos[0] = new_x
            pacman_pos[1] = new_y
            if maze[new_y][new_x] == 2:
                maze[new_y][new_x] = 0
                score += 10
                if dot_sound:
                    dot_sound.play()

def move_ghosts():
    for ghost in ghosts:
        options = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(options)
        for dx, dy in options:
            new_x = ghost["pos"][0] + dx
            new_y = ghost["pos"][1] + dy
            if 0 <= new_y < len(maze) and 0 <= new_x < len(maze[0]):
                if maze[new_y][new_x] != 1:
                    ghost["pos"][0] = new_x
                    ghost["pos"][1] = new_y
                    break

def check_collisions():
    global lives
    pac_rect = pygame.Rect(pacman_pos[0] * CELL_SIZE, pacman_pos[1] * CELL_SIZE + 60, CELL_SIZE, CELL_SIZE)
    for ghost in ghosts:
        ghost_rect = pygame.Rect(ghost["pos"][0] * CELL_SIZE, ghost["pos"][1] * CELL_SIZE + 60, CELL_SIZE, CELL_SIZE)
        if pac_rect.colliderect(ghost_rect):
            lives -= 1
            if death_sound:
                death_sound.play()
            reset_positions()
            break

def reset_positions():
    pacman_pos[0], pacman_pos[1] = 1, 1
    pacman_dir[0], pacman_dir[1] = 0, 0
    ghosts[0]["pos"] = [len(maze[0]) - 2, 1]
    ghosts[1]["pos"] = [1, len(maze) - 2]
    ghosts[2]["pos"] = [len(maze[0]) - 2, len(maze) - 2]
    ghosts[3]["pos"] = [len(maze[0]) // 2, len(maze) // 2]
    pygame.time.delay(500)

def check_level_complete():
    global level, FPS
    if not any(2 in row for row in maze):
        level += 1
        for y in range(len(maze)):
            for x in range(len(maze[0])):
                if maze[y][x] == 0:
                    maze[y][x] = 2
        reset_positions()
        FPS += 1

# Main game loop
running = True
while running:
    screen.fill(BLACK)
    font = pygame.font.SysFont("arial", 24)
    info_text = font.render(f"Score: {score}    Lives: {lives}    Level: {level}", True, WHITE)
    screen.blit(info_text, (10, 10))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pacman_dir = [0, -1]
            elif event.key == pygame.K_DOWN:
                pacman_dir = [0, 1]
            elif event.key == pygame.K_LEFT:
                pacman_dir = [-1, 0]
            elif event.key == pygame.K_RIGHT:
                pacman_dir = [1, 0]
    
    move_pacman()
    move_ghosts()
    check_collisions()
    check_level_complete()
    draw_maze()
    
    pac_rect = pygame.Rect(pacman_pos[0] * CELL_SIZE, pacman_pos[1] * CELL_SIZE + 60, CELL_SIZE, CELL_SIZE)
    pygame.draw.circle(screen, YELLOW, pac_rect.center, CELL_SIZE // 2 - 2)
    
    for ghost in ghosts:
        ghost_rect = pygame.Rect(ghost["pos"][0] * CELL_SIZE, ghost["pos"][1] * CELL_SIZE + 60, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, ghost["color"], ghost_rect)
    
    pygame.display.flip()
    clock.tick(FPS)
    
    if lives <= 0:
        if finish_sound:
            finish_sound.play()
            pygame.time.delay(2000)
        screen.fill(BLACK)
        go_text = font.render("Game Over", True, RED)
        final_score = font.render(f"Final Score: {score}", True, WHITE)
        screen.blit(go_text, (WIDTH // 2 - go_text.get_width() // 2, HEIGHT // 2 - 30))
        screen.blit(final_score, (WIDTH // 2 - final_score.get_width() // 2, HEIGHT // 2 + 10))
        pygame.display.flip()
        pygame.time.delay(3000)
        running = False
