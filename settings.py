# Game options/settings
TITLE = "Snake"
GRID_SIZE = 30
BLANK_SIZE = 40
ROWS = 10
COLS = 10
FPS = 20
FONT_NAME = 'arial'
MOVE_GAP = 320
PRESS_GAP = 100

# Define colors
WHITE = (255, 255, 255)
WHITE1 = (220, 220, 220)
WHITE2 = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
BGCOLOR = BLACK
LINE_COLOR = BLUE1


# AI settings
N_INPUT = 32
N_HIDDEN1 = 12 
N_HIDDEN2 = 12
N_OUTPUT = 4
NET_STRUCT = [N_INPUT, N_HIDDEN1, N_HIDDEN2, N_OUTPUT]
GENES_LEN = N_INPUT * N_HIDDEN1 + N_HIDDEN1 * N_HIDDEN2 + N_HIDDEN2 * N_OUTPUT + N_HIDDEN1 + N_HIDDEN2 + N_OUTPUT 

N_INPUT = 32
N_HIDDEN = 20 
N_OUTPUT = 4
NET_STRUCT = [N_INPUT, N_HIDDEN, N_OUTPUT]
GENES_LEN = N_INPUT * N_HIDDEN + N_HIDDEN * N_OUTPUT + N_HIDDEN + N_OUTPUT 
P_SIZE = 50
C_SIZE = 450

DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

MUTATE_RATE = 0.1
CROSS_RATE = 0.5
ETA = 100
SCALE = 0.2

GAME_LOOP = ROWS * COLS
