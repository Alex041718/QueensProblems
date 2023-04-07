
# définition de la taille de l'échiquier
N = 8

# définition des mouvements autorisés du cavalier
deplacements = [
    (-2, -1), (-2, 1), (-1, -2), (-1, 2),
    (1, -2), (1, 2), (2, -1), (2, 1)
]

# fonction qui génère le graphe représentant les cases accessibles depuis chaque case de l'échiquier
def generer_graphe():
    graphe = {}

    for i in range(N):
        for j in range(N):
            case_depart = (i, j)
            voisins = []
            for deplacement in deplacements:
                i_suivant, j_suivant = i + deplacement[0], j + deplacement[1]
                if 0 <= i_suivant < N and 0 <= j_suivant < N:
                    voisins.append((i_suivant, j_suivant))
            graphe[case_depart] = voisins

    return graphe


def parcours_cavalier(graphe, case_depart, visites, chemin_courant, data,i = 0):
    # on marque la case de départ comme visitée
    visites.add(case_depart)
    
    # on ajoute la case de départ au chemin courant
    chemin_courant.append(case_depart)

    # si le chemin courant contient toutes les cases, on a trouvé une solution
    if len(chemin_courant) == N*N:
        i = i + 1
        print(i)
        #print(chemin_courant)
        data.append(chemin_courant)
        return data
        

    # on explore les cases voisines non visitées
    for voisin in graphe[case_depart]:
        if voisin not in visites:
            parcours_cavalier(graphe, voisin, set(visites), list(chemin_courant),data,i)

    # si aucune solution n'a été trouvée, on retourne None
    return data
"""
def tracer_chemin_hamiltonien(chemin):
    # initialisation de la tortue
    tortue = turtle.Turtle()
    tortue.speed("fastest")
    tortue.pensize(3)
    tortue.pencolor("red")

    # déplacement à la première case du chemin
    case_courante = chemin[0]
    tortue.penup()
    tortue.goto(case_courante[1]*50, case_courante[0]*50)
    tortue.pendown()

    # dessin de la ligne droite entre chaque case
    for case_suivante in chemin[1:]:
        tortue.goto(case_suivante[1]*50, case_suivante[0]*50)

    # affichage de la fenêtre turtle
    turtle.done()
"""
# génération du graphe
graphe = generer_graphe()
case_depart = (0, 0)

data = []

data = parcours_cavalier(graphe, case_depart, set(), [], data)

print(data)