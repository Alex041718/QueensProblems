### Projet: Problème des N reines
## Auteur: Alexandre Le Marec - Duncan Cadoret

# On import le module time pour calculer le temps d'exécution du programme
import time

# la variable N contient la taille de l'échiquier ainsi que le nombre de reines
N = 8


def solve_queen_problem(N):
    """La fonction solve_queen_problem() permet de résoudre le problème des N reines avec une fonction récursive pour le backtracking et une autre fonction pour vérifier si une reine peut être placée sur une case.

    Args:
        N (int): Le nombre de reines à placer sur l'échiquier aisni que la taille de l'échiquier.

    Returns:
        solutions: Une liste de listes contenant les coordonnées des reines sur l'échiquier.
    """
    solutions = []
    
    def is_valid(board, row, col):
        """La fonction is_valid() vérifie si une reine peut être placée sur une case.
        (si une reine est déjà présente sur la même colonne, diagonale ou antidiagonale que la case spécifiée)

        Args:
            board (list): Une liste de tuples contenant les coordonnées des reines déjà placées sur l'échiquier.
            row (int): L'index de la ligne à vérifier.
            col (int): L'index de la colonne à vérifier.

        Returns:
            bool: True si une reine peut être placée sur la case, False sinon.
        """
        for r, c in board:
            if col == c or row + col == r + c or row - col == r - c:
                return False
        return True
    
    def backtrack(board, row):
        """La fonction backtrack() est une fonction récursive pour le backtracking. Elle utilise la fonction is_valid() pour vérifier si une reine peut être placée sur une case.

        Args:
            board (list): Une liste de tuples contenant les coordonnées des reines déjà placées sur l'échiquier.
            row (int): L'index de la ligne à vérifier.

        Returns:
            None
        """
        nonlocal solutions
        if row == N:
            solutions.append(board[:])
            #L'utilisation de la notation de tranche "board[:]" crée une nouvelle liste contenant les mêmes éléments que "board", plutôt que de simplement ajouter une référence à la liste originale. Cela permet d'éviter les problèmes liés à la modification de la liste originale.
            return
        for col in range(N):
            if is_valid(board, row, col):
                board.append((row, col))
                backtrack(board, row + 1) # Appel récursif
                board.pop()
    
    backtrack([], 0) #Appel initial
    return solutions

##On lance le programme et on calcule le temps d'exécution
start = time.time() # On mets en amrche le timer
solutions = solve_queen_problem(N) # On lance la fonction solve_queen_problem() qui nous renverra la liste des coordonnées des reines sur l'échiquier pour chaque solution.

    
def afficher_echiquier(tab,N,num):
    """
    La fonction afficher_echiquier() affiche l'échiquier sur l'écran Pygame.

    Args:
        tab (list): La liste de listes représentant l'échiquier à afficher.
        N (int): La taille de l'échiquier.
        num (int): Le numéro de l'échiquier à afficher.

    Returns:
        None
    """
    print("")
    print("-------- ",num+1," ---------") # On affiche le numéro de l'échiquier
    for i in range(N):
        
        for j in range(N):
            if tab[i][j] == 1: # Si la case vaut 1 alors elle contient une reine, alors on affiche un ♛
                print("♛"," ",end='')
            else:
                print("."," ",end='') # Sinon on affiche un point
        print("")
    print("")





def initEchi():
    """La fonction initEchi() initialise un échiquier de taille N*N.

    Returns:
        Une liste de listes de taille N*N.
        Un échiquier vide.
    """
    return [[0 for j in range(N)] for i in range(N)]

## Affichage des solutions
# Initialisation de la liste des échiquiers, tab contiendra tout les échiquiers
tab = []

# On parcourt la liste des solutions
for i in range(len(solutions)):
    
    tab.append(initEchi()) # On rajoute un échiquier vide à la liste des échiquiers qui contienne les solutions.
    
    for j in range(N):
        
        tab[i][solutions[i][j][0]][solutions[i][j][1]] = 1 # On place les reines sur l'échiquier. Grâce au tuple de cooordonnée des reines dans "solutions", on sait où placer les reines. Elles sont représentées par un 1.
        
    afficher_echiquier(tab[i],N,i) # On affiche l'échiquier pour chaque solution.
    




print(time.time() - start) # On affiche le temps d'exécution du programme