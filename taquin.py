from grille import Grille
from heuristic_manhanthan import Heuristic_Manhanthan
from heuristic_hamming import Heuristic_Hamming
from solver import Solver
from utils import *

print("grille de depart")
grille = Grille(createMixedGrille(3, 10),coup="start")
afficher_grille(grille)


heuristic = Heuristic_Hamming()
#heuristic = Heuristic_Manhanthan()
solver = Solver(grille, heuristic, createGrille(3))
solution = solver.solve()