import re

#Catalogue de fonctions pour aider à l'étude d'un trajet routier

#fonction qui calcule la distance
#restant à parcourir

def distanceRestante(parcourue,totale):
    """
    > Cette fonction calcule la distance restant à parcourir
    
    :param parcourue: la distance parcourue
    :param totale: la distance totale à parcourir
    :return: La distance restant à parcourir.
    """
    return totale - parcourue


#fonction qui calcule la vitesse
#en km/h

def vitesseMoyenne(distance_parcourue, temps_du_trajet):
    """
    > Cette fonction calcule la vitesse moyenne en km/h
    
    :param distance_parcourue: la distance parcourue en kilomètres
    :param temps_du_trajet: durée du trajet en heures
    :return: the distance_parcourue divided by the temps_du_trajet.
    """
    return distance_parcourue / temps_du_trajet


#fonction qui calcule le temps restant
#pour un trajet en heures

def tempsRestant(distance_restante, vitesse_moyenne):
    """
    Cette fonction calcule le temps restant sur un trajet, en heures.
    
    :param distance_restante: la distance restant à parcourir, en kilomètres
    :param vitesse_moyenne: vitesse moyenne du véhicule
    :return: le temps restant sur un trajet, en heures.
    """
    return distance_restante / vitesse_moyenne


#fonction qui calcule le coût
#du trajet

def coutTrajet(distance, consommation_de_la_voiture, prix_du_carburant):
    """
    > Cette fonction calcule le coût d'un trajet
    
    :param distance: la distance du trajet
    :param consommation_de_la_voiture: la consommation de carburant de la voiture en litres aux 100 km
    :param prix_du_carburant: le prix du carburant dans votre pays
    :return: Le coût du voyage
    """
    return distance * (consommation_de_la_voiture / 100) * prix_du_carburant


#fonction qui convertie les heures
#en heures et en minutes

def afficheTemps(nombre_heure):
    """
    Elle convertit une durée donnée en heures, en heures et minutes et renvoie une chaîne de type ..
    heure(s) ... minute(s)
    
    :param nombre_heure: le nombre d'heures
    """
    return f"{int(nombre_heure * 60 // 60)} heure⋅s {int(nombre_heure * 60 % 60)}"

def completCoutTrajet(distance, vehicule):
    """
    Il prend une distance et un nom de véhicule, et renvoie le coût du trajet
    
    :param distance: la distance du trajet
    :param vehicule: le nom du véhicule
    :return: Le résultat de la fonction `coutTrajet`
    """

    # Recherche de la ligne du véhicule dans le fichier vehicule.txt
    contentVehicule = vehiculeParser()
    for i in range(1, len(contentVehicule)):
        if contentVehicule[i][0] == vehicule:
            line = i

    # Obtenir le type de carburant, la consommation
    typeCarburant = contentVehicule[line][2]
    consommation = contentVehicule[line][1]

    # Recherche du prix du type de carburant dans le fichier carburant.txt.
    contentCarburant = carburantParser()
    prixCarburant = None
    for i in range(1, len(contentCarburant)):
        if contentCarburant[i][0] == typeCarburant:
            prixCarburant = contentCarburant[i][1]
    if prixCarburant != None:
        # Renvoyer le résultat de la fonction `coutTrajet`
        return coutTrajet(float(distance), float(consommation), float(prixCarburant))
    else:
        raise ValueError("Le carburant de ce véhicule n'existe pas")
    

def vehiculeParser():
    """fonction qui récupère les données de vehicule.txt"""
    content = []
    with open('vehicule.txt', 'r') as file:
        for ligne in file:
            s = ligne.strip("\n\r")       # on enlève les caractères de fin de ligne
            l = s.split(",")           # on découpe en colonnes
            content.append(l)         #on ajoute à l'array les colonnes
    return content

def carburantParser():
    """fonction qui récupère les données de carburant.txt"""
    content = []
    with open('carburant.txt', 'r') as file:
        for ligne in file:
            s = ligne.strip("\n\r")       # on enlève les caractères de fin de ligne
            l = s.split(",")           # on découpe en colonnes
            content.append(l)         #on ajoute à l'array les colonnes
    return content

def vehiculeWriter(nom, conso, typeCarbu):
    """fonction qui ajoute un véhicule"""
    with open("vehicule.txt", "a") as file:
        file.write(nom+","+conso+","+typeCarbu+"\n")

def vehiculeWriterReplace(ancienNom, nouveauNom, conso, typeCarbu):
    """
    Il ouvre le fichier, le lit, remplace la ligne avec l'ancien nom par les nouvelles valeurs et écrit le
    nouveau contenu dans le fichier
    
    :param ancienNom: le nom du véhicule à remplacer
    :param nouveauNom: le nouveau nom du véhicule
    :param conso: consommation
    :param typeCarbu: « essence » ou « diesel »
    """

    with open("vehicule.txt", 'r') as file:
        content = file.read()
    content = re.sub(rf"{ancienNom}.+\n", f"{nouveauNom},{str(conso)},{typeCarbu}\n", content)
    with open("vehicule.txt", 'w') as file:
        file.write(content)

def vehiculeDeleter(nom):
    """
    Il ouvre le fichier, le lit, supprime la ligne qui contient le nom, puis écrit une ligne vide
    dans le fichier
    
    :param nom: le nom du véhicule à supprimer
    """

    with open("vehicule.txt", "r") as file:
        content = file.read()
    content = re.sub(rf"{nom}.+\n", "", content)
    with open("vehicule.txt" , "w") as file:
        file.write(content)

def vehiculeIsFind(nom):
    """
    Il ouvre le fichier, lit le contenu, puis recherche la chaîne que vous transmettez
    pour voir si celle-ci existe
    
    :param nom: le nom du véhicule
    :return: le résultat de la recherche.
    """

    with open("vehicule.txt", 'r') as file:
        content = file.read()
    return re.search(nom, content)