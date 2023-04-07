import time
##isomorphisme des graphe


N = 8
    
def finish(tableau):
    nb_ones = 0
    for ligne in tableau:
        for element in ligne:
            if element == 1:
                nb_ones += 1
    if nb_ones == N:
        return True
    else:
        return False

def next_case(i):
    if i == N-1:
        return 0
    else:
        return i+1

def est_valide(tab, r, c):
    """
    Vérifie si une reine peut être placée en (r,c) sur l'échiquier.
    Retourne True si c'est le cas, False sinon.
    """
    # Vérifier la rangée et la colonne
    for i in range(N):
        if tab[r][i] == 1 or tab[i][c] == 1:
            return False
    # Vérifier les diagonales
    for i in range(N):
        for j in range(N):
            if (i + j == r + c) or (i - j == r - c):
                if tab[i][j] == 1:
                    return False
    return True



def placer_reine(tab, col, lig, n):
    if finish(tab):
        print()
        print("-------- ",n+1," ---------")
        afficher_echiquier(echiquier)
        return True
    c = 0
    
    
    while c < N:
        
        c = c + 1
        if est_valide(tab, lig, col):
            tab[lig][col] = 1
            
            
            
            if placer_reine(tab, next_case(col),lig,n):
                return True
            tab[lig][col] = 0
            
            
            
        lig = next_case(lig)
    return False  
        

def afficher_echiquier(tab):
    """
    Affiche l'échiquier sur l'écran Pygame.
    """
    for i in range(N):
        
        for j in range(N):
            if tab[i][j] == 1:
                print("♛"," ",end='')
            else:
                print("."," ",end='')
        print("")

def init_echiquier():
    return [[0 for j in range(N)] for i in range(N)]

# Programme principal
echiquier = init_echiquier()

tab = []

start = time.time()

for i in range(N):
    
    placer_reine(echiquier, 0, i, i)
    
    tab.append(echiquier)
    echiquier = init_echiquier()
    
print(time.time() - start)



