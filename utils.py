def createGrille(n):
    if n <= 0:
        raise ValueError("Grid size must be greater than 0")

    total_cells = n * n
    values = list(range(1, total_cells))
    values.append(0)
    grid = [values[i:i+n] for i in range(0, total_cells, n)]

    return grid


from grille import Grille
import random
def createMixedGrille(n , nb_coup):
    if n <= 0:
        raise ValueError("Grid size must be greater than 0")

   
    total_cells = n * n
    values = list(range(1, total_cells))
    values.append(0)
    grid = [values[i:i+n] for i in range(0, total_cells, n)]

    grille = Grille(grid)


    for i in range(nb_coup):
        coups = grille.coup_possible()
        coup = coups[random.randint(0, len(coups) - 1)]
        grille = grille.jouer_coup(coup)
    return grille.grille





def afficher_grille(grille):
    for row in grille.grille:
        print(row)
    print()