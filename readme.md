# Algorithme A*

## Jeu du taquin

Ce code python sert à résoudre le jeu du taquin avec l'algorithme A*.

Vous pouvez utiliser deux heuristiques différentes :
- Manhattan
- Hamming

Pour configurer le jeu modifier le fichier taquin.py

Pour definir aléatoirement la grille de depart : 

```python
grille = Grille(createMixedGrille(3, 10),coup="start")
```


Pour Changer d'heuristique : 

```python
heuristic = Heuristic_Hamming()
#ou 
heuristic = Heuristic_Manhanthan()
```

Configurer le solver et le lancer :

```python
solver = Solver(grille, heuristic, createGrille(3))
solution = solver.solve()
```


Pour lancer la démo éxecuter simplement le script taquin.py à l'aide de python

```bash
python taquin.py
```


Vous pouvez également afficher la versions graphique
aprés avoir installer les dépendances suivantes :

```bash
pip install pygame
```


Puis Lancer le script taquin_ui.py
