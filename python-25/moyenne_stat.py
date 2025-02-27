#ma fonction va clculer la moyenne dune serie statistique qui prend en parametre une liste et me retourne 
#-la moyenne 

def calcul_moyenne(series_statistique):
    moyenne = 0
    for element in series_statistique:
        moyenne += element
    
    #je divise la somme par la taille de la liste pour calculer la moyenne
    moyenne = moyenne / len(series_statistique)
    
    #j'affiche la moyenne
    print("La moyenne de la série est :", moyenne)
    return moyenne