import pygame as pg

# Constants
WIDTH, HEIGHT = 800, 700
FPS = 60

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Create the game window
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Maze Game")


# Maze layout using a 2D array
maze = [
    '|||||||||||||||||||||||||||',
    '|............|............|',
    '|.||||.|||||.|.|||||.||||.|',
    '|.||||.|||||.|.|||||.||||.|',
    '|.........................|',
    '|.||||.||.|||||||.||.||||.|',
    '|......||....|....||......|',
    '|.||||.||||| | |||||.||||.|',
    '|.||||.||         ||.||||.|',
    '|.||||.||  |||||  ||.||||.|',
    '      .    |EEE|    .      ',
    '|.||||.||  |||||  ||.||||.|',
    '|.||||.||         ||.||||.|',
    '|.||||.||.|||||||.||.||||.|',
    '|............|............|',
    '|.||||.|||||.|.|||||.||||.|',
    '|....|.......P.......|....|',
    '|||..|.||.|||||||.||.|..|||',
    '|......||....|....||......|',
    '|.||||||||||.|.||||||||||.|',
    '|.........................|',
    '|||||||||||||||||||||||||||'
]

# Maze cell size
cell_size = int(WIDTH / 27)

# Pac-Man properties
pacman_size = cell_size / 2
pacman_args = pg.Rect(cell_size, cell_size, pacman_size, pacman_size)
pacman_pos = pg.Vector2(16, 13)
pacman_speed = 5

def draw_maze(maze):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            rect = pg.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
            if cell == '|':
                pg.draw.rect(screen, WHITE, rect)
            elif cell == '-':
                pg.draw.rect(screen, BLACK, rect)
            elif cell == '.':
                dot_rect = pg.Rect(rect.centerx - 2, rect.centery - 2, 5, 5)
                pg.draw.rect(screen, WHITE, dot_rect)
            elif cell == 'P':
                pacman_args.x = x * cell_size + pacman_size / 2
                pacman_args.y = y * cell_size + pacman_size / 2
                pacman_pos.x = x
                pacman_pos.y = y
                pg.draw.circle(screen, YELLOW, pacman_args.center, pacman_size)

# Game loop
running = True
clock = pg.time.Clock()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()

    # Update Pac-Man position based on direction
    pacman_direction = pg.Vector2(0, 0)

    if keys[pg.K_RIGHT]:
        pacman_direction.x = 1
    elif keys[pg.K_DOWN]:
        pacman_direction.y = 1
    elif keys[pg.K_LEFT]:
        pacman_direction.x = -1
    elif keys[pg.K_UP]:
        pacman_direction.y = -1

    # Check boundaries before updating Pac-Man position
    new_x = int(pacman_pos.x + pacman_direction.x)
    new_y = int(pacman_pos.y + pacman_direction.y)
    if 0 <= new_x < len(maze[0]) and 0 <= new_y < len(maze):
        # Change the position of 'P' to ' '
        maze_row = list(maze[int(pacman_pos.y)])
        maze_row[int(pacman_pos.x)] = ' '
        maze[int(pacman_pos.y)] = ''.join(maze_row)
        pacman_pos += pacman_direction
        maze_row = list(maze[int(pacman_pos.y)])
        maze_row[int(pacman_pos.x)] = 'P'
        maze[int(pacman_pos.y)] = ''.join(maze_row)

    # Fill the screen with a background color
    screen.fill(BLACK)

    # Draw the maze
    draw_maze(maze)

    # Update the display
    pg.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

pg.quit()
