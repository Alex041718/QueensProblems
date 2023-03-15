import pygame
##isomorphisme des graphe

TAILLE_CASE = 80
TAILLE_ECRAN = 8 * TAILLE_CASE


    
def finish(tableau):
    nb_ones = 0
    for ligne in tableau:
        for element in ligne:
            if element == 1:
                nb_ones += 1
    if nb_ones == 8:
        return True
    else:
        return False

def next_case(i):
    if i == 7:
        return 0
    else:
        return i+1

def est_valide(tab, r, c):
    """
    Vérifie si une reine peut être placée en (r,c) sur l'échiquier.
    Retourne True si c'est le cas, False sinon.
    """
    # Vérifier la rangée et la colonne
    for i in range(8):
        if tab[r][i] == 1 or tab[i][c] == 1:
            return False
    # Vérifier les diagonales
    for i in range(8):
        for j in range(8):
            if (i + j == r + c) or (i - j == r - c):
                if tab[i][j] == 1:
                    return False
    return True

def placer_reine_temp(tab, col):
    """
    Place une reine sur la colonne 'col' de l'échiquier 'tab'.
    Retourne True si une solution a été trouvée, False sinon.
    """
    # Cas de base : toutes les reines ont été placées
    if col == 8:
        return True
    # Essayer de placer une reine sur chaque ligne de la colonne 'col'
    for i in range(8):
        if est_valide(tab, i, col):
            tab[i][col] = 1
            pygame.time.wait(1000)  # Attendre un peu pour l'affichage
            afficher_echiquier(tab)
            pygame.display.update()
            if placer_reine(tab, col + 1):
                return True
            tab[i][col] = 0
            pygame.time.wait(1000)  # Attendre un peu pour l'affichage
            afficher_echiquier(tab)
            pygame.display.update()
    return False

def placer_reine(tab, col, n):
    if finish(tab):
        print("---------- ",n," ---------")
        print(tab)
        return True
    c = 0
    lig = n
    
    while c < 8:
        
        c = c + 1
        if est_valide(tab, lig, col):
            tab[lig][col] = 1
            pygame.time.wait(10)  # Attendre un peu pour l'affichage
            afficher_echiquier(tab)
            pygame.display.update()
            if placer_reine(tab, next_case(col),lig):
                return True
            tab[lig][col] = 0
            pygame.time.wait(10)  # Attendre un peu pour l'affichage
            afficher_echiquier(tab)
            pygame.display.update()
        lig = next_case(lig)
    return False  
        

def afficher_echiquier(tab):
    """
    Affiche l'échiquier sur l'écran Pygame.
    """
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                couleur = (255, 255, 255)
            else:
                couleur = (0, 0, 0)
            pygame.draw.rect(ecran, couleur, (i * TAILLE_CASE, j * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))
            if tab[j][i] == 1:
                pygame.draw.circle(ecran, (255, 0, 0), (i * TAILLE_CASE + TAILLE_CASE // 2, j * TAILLE_CASE + TAILLE_CASE // 2), TAILLE_CASE // 3)

# Initialisation de Pygame
pygame.init()
ecran = pygame.display.set_mode((TAILLE_ECRAN, TAILLE_ECRAN))
pygame.display.set_caption("Problème des huit reines")

# Programme principal
echiquier = [[0 for j in range(8)] for i in range(8)]


placer_reine(echiquier, 0, 2)

# Boucle d'événements Pygame
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
