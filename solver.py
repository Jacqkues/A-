import heapq
from grille import Grille
from heuristic import Heuristic
class Solver:
    def __init__(self, grille:Grille , heuristic: Heuristic, goal):
        self.grille = grille
        self.heuristic = heuristic
        self.open = []
        self.close = set()
        self.grille_goal = goal # [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    def reconstruire_chemin(self, nœud):
        chemin = [nœud]
        list_coup = []
        while nœud.parent:
            chemin.insert(0, nœud.parent)
            nœud = nœud.parent

        print("Chemin de résolution :")
        for étape, grille in enumerate(chemin):
            print(f"\nÉtape {étape + 1}: ({grille.coup}))")
            list_coup.append(grille.coup)
            self.afficher_grille(grille)

        return list_coup
    
    def afficher_grille(self, grille):
        for row in grille.grille:
            print(row)
        print()
    def solve(self):
        debut = self.grille
        debut.g = 0
        debut.h = self.heuristic.calculer_heuristic(debut.grille,self.grille_goal)   
        debut.f = debut.g + debut.h

        heapq.heappush(self.open, debut) 

        while len(self.open) > 0:

            current = heapq.heappop(self.open)

            if current.is_finish(self.grille_goal):
                return self.reconstruire_chemin(current)
                
            
            self.close.add(tuple(map(tuple, current.grille)))

            for coup in current.coup_possible():
                new_grille = current.jouer_coup(coup)
                new_grille.h = self.heuristic.calculer_heuristic(new_grille.grille,self.grille_goal)
                new_grille.f = new_grille.g + new_grille.h

                if tuple(map(tuple, new_grille.grille)) not in self.close:
                    heapq.heappush(self.open, new_grille)
    

