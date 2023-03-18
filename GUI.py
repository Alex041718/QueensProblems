import pygame



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



def placer_reine(tab, col, lig, n):
    if finish(tab):
        #print()
        #print("-------- ",n+1," ---------")
        #afficher_echiquier(echiquier)
        return True
    c = 0
    
    
    while c < 8:
        
        c = c + 1
        if est_valide(tab, lig, col):
            tab[lig][col] = 1
            
            
            
            if placer_reine(tab, next_case(col),lig,n):
                return True
            tab[lig][col] = 0
            
            
            
        lig = next_case(lig)
    return False  

def init_echiquier():
    return [[0 for j in range(8)] for i in range(8)]

# Programme principal
echiquier = init_echiquier()

tab = []

for i in range(8):
    placer_reine(echiquier, 0, i, i)
    tab.append(echiquier)
    echiquier = init_echiquier()







### PYGAME
TAILLE_CASE = 40
TAILLE_CADRE = 8 * TAILLE_CASE
DECALAGE = TAILLE_CASE
NB_CADRE = 8


pygame.init()
ecran = pygame.display.set_mode(((TAILLE_CADRE+DECALAGE)*NB_CADRE // 2, (TAILLE_CADRE+DECALAGE)*2))
#ecran = pygame.display.set_mode((10000,10000))
pygame.display.set_caption("Problème des huit reines")


                
def afficher_echiquier_bis(tab, nb_echiquiers):
    """
    Affiche plusieurs échiquiers côte à côte sur l'écran Pygame.
    """
    


    for n in range(nb_echiquiers):  # Boucle sur chaque échiquier
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    couleur = (255, 255, 255)
                else:
                    couleur = (0, 0, 0)
                if n>3:
                    
                    pygame.draw.rect(ecran, couleur, (((i * TAILLE_CASE) + (n-4)*(TAILLE_CADRE + DECALAGE)), ((j * TAILLE_CASE)+ (1)*(TAILLE_CADRE + DECALAGE)), TAILLE_CASE, TAILLE_CASE))
                else:
                    pygame.draw.rect(ecran, couleur, (((i * TAILLE_CASE) + n*(TAILLE_CADRE + DECALAGE)), j * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))
                    
                if tab[n][j][i] == 1:
                    if n>3:
                        pygame.draw.circle(ecran, (255, 0, 0), (((i * TAILLE_CASE + TAILLE_CASE // 2) + (n-4)*(TAILLE_CADRE + DECALAGE)), ((j * TAILLE_CASE + TAILLE_CASE // 2)+ (1)*(TAILLE_CADRE + DECALAGE))), TAILLE_CASE // 3)
                    else:
                        pygame.draw.circle(ecran, (255, 0, 0), (((i * TAILLE_CASE + TAILLE_CASE // 2) + n*(TAILLE_CADRE + DECALAGE)), j * TAILLE_CASE + TAILLE_CASE // 2), TAILLE_CASE // 3)
                        




 
        
afficher_echiquier_bis(tab,NB_CADRE)#
pygame.display.update()


# Boucle d'événements Pygame
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
