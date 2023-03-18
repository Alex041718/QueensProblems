import time

N = 8

def solve_queen_problem(N):
    solutions = []
    
    def is_valid(board, row, col):
        for r, c in board:
            if col == c or row + col == r + c or row - col == r - c:
                return False
        return True
    
    def backtrack(board, row):
        nonlocal solutions
        if row == N:
            solutions.append(board[:])
            return
        for col in range(N):
            if is_valid(board, row, col):
                board.append((row, col))
                backtrack(board, row + 1)
                board.pop()
    
    backtrack([], 0)
    return solutions

start = time.time()
solutions = solve_queen_problem(N)

    
def afficher_echiquier(tab,N,num):
    """
    Affiche l'échiquier sur l'écran Pygame.
    """
    print("-------- ",num+1," ---------")
    for i in range(N):
        
        for j in range(N):
            if tab[i][j] == 1:
                print("♛"," ",end='')
            else:
                print("."," ",end='')
        print("")





def initEchi():
    return [[0 for j in range(N)] for i in range(N)]

tab = []

for i in range(len(solutions)):
    tab.append(initEchi())
    for j in range(N):
        
        tab[i][solutions[i][j][0]][solutions[i][j][1]] = 1
    afficher_echiquier(tab[i],N,i)
    
bool = False

"""
#pas de paire
for g in range(len(tab)):
    for f in range(len(tab)):
        if g != f:
            if tab[g] == tab[f]:
                bool = True
            
print(bool)
"""

print(time.time() - start)