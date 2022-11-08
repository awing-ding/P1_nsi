import trajet as t

def choix1():
    """
    Il demande à l'utilisateur un véhicule, vérifie s'il est dans la liste des véhicules, demande la
    durée du trajet, puis imprime le coût du trajet
    """
    vehicule = input('quel est votre véhicule ? ')
    if t.vehiculeIsFind(vehicule) != None: 
        longueurTrajet = input("quelle est la longueur de votre trajet ? ")
        try:
            longueurTrajet = int(longueurTrajet)
        except ValueError:
            print("une longueur doit être un nombre !")
        print(f"ce trajet coutera {t.completCoutTrajet(longueurTrajet, vehicule)}")
    else:
        print("Véhicule inconnu")

def choix2():
    """
    Il demande à l'utilisateur la distance restante et la vitesse moyenne, puis imprime le temps restant
    """
    distanceRestante = input("Quel distance reste-t-il à parcourir ? ")
    vitesse_moyenne = input("Quel est votre vitesse moyenne ? ")
    print(t.afficheTemps(t.tempsRestant(distanceRestante, vitesse_moyenne)))

def choix3():
    """
    Cette fonction permet à l'utilisateur de saisir le nom du véhicule, la consommation du véhicule et
    le type de carburant utilisé par le véhicule
    """
    inLoop = True
    while inLoop:
        nom = input("Entrez le nom du véhicule (0 pour annuler) ")
        if nom != "0":
            print(t.vehiculeIsFind(nom))
            if t.vehiculeIsFind(nom) == None:             
                consommationCarburant = input("Quel est la consommation au 100 de votre véhicule ? ")
                typeCarburant = input("Quel carburant votre véhicule consomme-t-il ? ")
                t.vehiculeWriter(nom, consommationCarburant, typeCarburant)
            else: 
                print("le vehicule existe déjà")
        else:
            inLoop = False

def choix4():
    """
    Il demande un nom à l'utilisateur, si le nom n'est pas 0, il demande le nouveau nom, une nouvelle
    consommation et un nouveau type de carburant. Puis il appelle la fonction vehiculeWriterReplace de
    la classe Trajet pour modifier l'entrée
    """
    nom = input("Entrez le nom du véhicule (0 pour annuler) ")
    if nom != "0":
        if t.vehiculeIsFind(nom) != None:
            newName = input("Entrez le nouveau nom ")
            newConso = input("Entrez la nouvelle conso ")
            newType = input("Entrez le nouveau type de carburant ")
            t.vehiculeWriterReplace(nom, newName, newConso, newType)
        else: 
            print("le vehicule n'a pas été trouvé")

def choix5():
    """
    Il demande à l'utilisateur d'entrer le nom du véhicule à supprimer, et si le véhicule est trouvé, il
    le supprime
    """
    nom = input("Entrez le nom du véhicule (0 pour annuler) ")
    if nom != "0":
        if t.vehiculeIsFind(nom) != None:
            t.vehiculeDeleter(nom)
        else: 
            print("le vehicule n'a pas été trouvé")

def main():
    """
    La fonction principale du programme. C'est la fonction qui sera appelée au lancement du programme.
    """

    while True :

        # C'est un menu.
        choix = input("             0-quitter \n \
            1-calculer le coût d'un trajet \n \
            2-calculer le temps restant sur un trajet en .. heure(s) ... minute(s) \n \
            3-ajouter un véhicule \n \
            4-modifier un véhicule \n \
            5-supprimer un véhicule \n \
            ")

        # C'est une façon de quitter le programme.
        if choix == "0":
            return 

        # C'est une fonction qui calcule le coût d'un voyage.
        elif choix == "1":
            choix1()

        # C'est une fonction qui calcule le temps restant sur un trajet.
        elif choix == "2":
            choix2()
    
        # C'est une fonction qui permet d'ajouter un véhicule.
        elif choix == "3":
            choix3()
        
        # C'est une fonction qui permet de modifier un véhicule.
        elif choix == "4":
            choix4()
        
        # C'est une fonction qui permet de supprimer un véhicule.
        elif choix == "5":
            choix5()

                

main()