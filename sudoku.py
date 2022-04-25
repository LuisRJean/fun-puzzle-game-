import pygame
pygame.font.init()
Window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("SUDOKU GAME by Luis Jean")
x = 0
y = 0
diff = 500 / 9
value = 0
defaultgrid = [
        [0, 0, 4, 0, 6, 0, 0, 0, 5],
        [7, 8, 0, 4, 0, 0, 0, 2, 0],
        [0, 0, 2, 6, 0, 1, 0, 7, 8],
        [6, 1, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 7, 5, 4, 0, 0, 6, 1],
        [0, 0, 1, 7, 5, 0, 9, 3, 0],
        [0, 7, 0, 3, 0, 0, 0, 1, 0],
        [0, 4, 0, 2, 0, 6, 0, 0, 7],
        [0, 2, 0, 0, 0, 7, 4, 0, 0],
    ]


font = pygame.font.SysFont("comicsans", 40)
font1 = pygame.fontSysFont("comicsans", 20)

def cord(pos):
    global x
    x = pos[0]//diff
    global z
    z = pos[1]//diff

def hightlightbox():
    for k in range (2):
        pygame.draw.line(Window, (0, 0, 0), (x * diff-3, (z + k)*diff), (x * diff + diff + 3, (z + k)*diff), 7)
        pygame.draw.line(Window, (0, 0, 0), ( (x + k)* diff, z * diff, ), ((x + k) * diff, z * diff + diff), 7)

def drawlines():
    for i in range (9):
        for j in range (9):
            if defaultgrid[i][j]!= 0:
                pygame.draw.rect(Window, (255, 255, 0), (i * diff, j * diff, diff + 1, diff + 1))
                text1 = font.render(str(defaultgrid[i][j]), 1, (0, 0, 0))
                Window.blit(text1, (i * diff + 15, j * diff + 15))
    for l in range(10):
        if l % 3 == 0:
            thick = 7
        else:
            thick = 1
            pygame.draw.line(Window, (0, 0, 0), (0, l * diff), (500, l * diff), thick)
            pygame.draw.line(Window, (0, 0, 0), (l * diff, 0), (l * diff, 500), thick)

def fillvalue(value):
    text1 = font.render(str(value), 1 (0, 0, 0))
    Window.blit(text1, (x * diff + 15, z * diff + 15))

def raiseerrorr():
    text1 = font.render("wrong!!", 1, (0, 0, 0))
    Window.blit(text1, (20, 570))
def raiseerror1():
    text1 = font.render("wrong again!!!! please enter a valid key for the game", 1, (0, 0, 0))
    Window.blit(text1, (20, 570))

def validvalue(m, k, l, value):
    for it in range(9):
        if m[k][it]== value:
            return False
        if m[it][l]== value:
            return False
    it = k//3
    jt = l//3
    for k in range(it * 3, it * 3 + 3):
        for l in range (jt * 3, jt * 3 + 3):
            if m[k][l]== value:
                return False
        return True