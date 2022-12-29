# tetris game

# the board and the x y axis looks like this
# 4
# 3
# 2
# 1
# 0
#    0  1  2  3  4

import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((750, 750))
pygame.display.set_caption('Tetris')

# Fill background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

# Blit everything to the screen
screen.blit(background, (0, 0))
pygame.display.flip()


class OPiece:
    center = (0.5, 0.5)
    color = (255, 255, 0)
    origin = (0, 0)
    body = [(0, 1), (1, 0), (1, 1)]


class IPiece:
    center = (0.5, 1.5)
    color = (0, 255, 255)
    origin = (0, 0)
    body = [(0, 1), (0, 2), (0, 3)]


class LPiece:
    center = (1, 1)
    color = (255, 127, 0)
    origin = (0, 0)
    body = [(1, 0), (1, 1), (1, 2)]


class JPiece:
    center = (0, 1)
    color = (0, 0, 255)
    origin = (0, 0)
    body = [(1, 0), (0, 1), (0, 2)]


class SPiece:
    center = (1, 1)
    color = (0, 255, 0)
    origin = (0, 1)
    body = [(1, 1), (1, 0), (2, 0)]


class ZPiece:
    center = (1, 1)
    color = (255, 0, 0)
    origin = (0, 0)
    body = [(1, 0), (1, 1), (2, 1)]


class TPiece:
    center = (1, 0)
    color = (128, 0, 128)
    origin = (0, 0)
    body = [(1, 0), (1, 1), (2, 0)]


class Box:
    def __init__(self, coordinate, piece=None):
        self.coordinate = coordinate
        self.piece = piece
        if piece is None:
            self.color = (127, 127, 127)
        else:
            self.color = piece.color


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = []
        # generate a tetris board with given width and height
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(Box((i, j)))
            self.grid.append(row)

    # print the generated board out
    def print_board(self):
        size = 35
        for row in self.grid:
            for box in row:
                pygame.draw.rect(screen, box.color,
                                 pygame.Rect(row.index(box) * (size + 2), self.grid.index(row) * (size + 2), size,
                                             size))

    # fetch information on a box on the board with given x and y coordinate
    def fetch_location(self, x, y):
        return self.grid[y][x]

    # insert piece with given origin
    def insert_piece(self, piece, x_origin, y_origin):
        if piece == SPiece:
            y_origin += 1
        self.grid[y_origin][x_origin] = Box((x_origin, y_origin), piece)  # place the origin
        for x, y in piece.body:
            dx = x - piece.origin[0]
            dy = y - piece.origin[1]
            self.grid[y_origin + dy][x_origin + dx] = Box((dx, dy), piece)
        self.print_board()


# idk but they say this is important
if __name__ == '__main__':
    board = Board(10, 20)
    board.insert_piece(random.choice([OPiece, IPiece, TPiece, ZPiece, SPiece, LPiece, JPiece]), 4, 0)
    board.print_board()
    screen.blit(background, (0, 0))

    change_piece_event = pygame.USEREVENT + 1
    change_piece = 1000
    pygame.time.set_timer(change_piece_event, change_piece)

    done = False

    # Event loop
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        for e in pygame.event.get():
            if e.type == change_piece_event:
                board.insert_piece(random.choice([OPiece, IPiece, TPiece, ZPiece, SPiece, LPiece, JPiece]), 4, 0)
        pygame.display.flip()
