import pygame
from grille import Grille
from utils import *
from heuristic_manhanthan import Heuristic_Manhanthan
from solver import Solver
pygame.init()


print("grille de depart")
grille = Grille(createMixedGrille(3, 100),coup="start")
afficher_grille(grille)

heuristic_manhattan = Heuristic_Manhanthan()
solver = Solver(grille, heuristic_manhattan, createGrille(3))
solution = solver.solve()


# Set up window
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Taquin Game")

# Set up game variables
grid_size = 3
tile_size = width // grid_size
running = True


def draw_grid():
    for i in range(grid_size):
        for j in range(grid_size):
            value = grille.grille[i][j]
            pygame.draw.rect(screen, (255, 255, 255), (j * tile_size, i * tile_size, tile_size, tile_size))
            if value != 0:
                # Draw the value on the tile
                font = pygame.font.Font(None, 36)
                text = font.render(str(value), True, (0, 0, 0))
                screen.blit(text, (j * tile_size + tile_size // 3, i * tile_size + tile_size // 3))

draw_grid()
pygame.display.flip()



for coup in solution:
    grille = grille.jouer_coup(coup)
    draw_grid()
    pygame.display.flip()
    pygame.time.wait(750)



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            # Handle mouse click events
            # Update the state of the game accordingly

    # Redraw the grid
    draw_grid()
    pygame.display.flip()