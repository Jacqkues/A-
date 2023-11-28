
import heapq
import random


class Grille:
    def __init__(self, grille, parent=None, g=float('inf'), h=float('inf') , coup=None):
        self.grille = grille
        self.size = len(grille)
        self.parent = parent
        self.g = g  # coût du chemin depuis le début
        self.h = h  # estimation du coût restant pour atteindre l'objectif
        self.f = g + h  # coût total
        self.coup = coup
    def is_finish(self,goal):
        return self.grille == goal
    def case_vide(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grille[i][j] == 0:
                    return (i,j)
    def coup_possible(self):
        i,j = self.case_vide()
        coups = []
        if i > 0:
            coups.append('h')
        if i < self.size - 1:
            coups.append('b')
        if j > 0:
            coups.append('g')
        if j < self.size - 1:
            coups.append('d')
        return coups
    def jouer_coup(self, coup):
        i, j = self.case_vide()
        nouvelle_grille = [list(row) for row in self.grille]  # Créer une copie de la grille
        if coup == 'h':
            nouvelle_grille[i][j], nouvelle_grille[i-1][j] = nouvelle_grille[i-1][j], nouvelle_grille[i][j]
            
        elif coup == 'b':
            nouvelle_grille[i][j], nouvelle_grille[i+1][j] = nouvelle_grille[i+1][j], nouvelle_grille[i][j]
        elif coup == 'g':
            nouvelle_grille[i][j], nouvelle_grille[i][j-1] = nouvelle_grille[i][j-1], nouvelle_grille[i][j]
        elif coup == 'd':
            nouvelle_grille[i][j], nouvelle_grille[i][j+1] = nouvelle_grille[i][j+1], nouvelle_grille[i][j]
        return Grille(nouvelle_grille, parent=self, g=self.g+1, h=self.h , coup=coup)
    def __lt__(self, other):
        return self.f < other.f






