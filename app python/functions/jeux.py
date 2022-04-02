from functions.result import *
import random
from models.cart import carte


def jeux(mise, joueur):
    Couleur_list = ["Trèfle", "Coeur", "Pique", "Carrau"]
    valeur_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    deck = []

    for value in valeur_liste:
        for color in Couleur_list:
            nouvelle_carte = carte(value, color)
            deck.append(nouvelle_carte)

    selection_cartes = random.sample(deck, 5)

    print("Vous avez tiré : \n")

    for selection_carte in selection_cartes:
        joueur.add_carte(selection_carte)
        deck.remove(selection_carte)
        print(selection_carte.get_nom())

    final_carte_list = []

    for carte_tmp in joueur.get_carte_list():
        choix = input("\nVoulez vous garder : " + carte_tmp.get_nom() + " | oui/non ")
        if choix == "oui":
            final_carte_list.append(carte_tmp)
            print("ok, la carte est conservé")
        elif choix == "non":
            new_selection_carte = random.sample(deck, 1)
            final_carte_list.append(new_selection_carte[0])
            deck.remove(new_selection_carte[0])
            print("vous avez tiré :" + new_selection_carte[0].get_nom())
        else:
            final_carte_list.append(carte_tmp)
            print("Veleur incorrecte, la carte est conservé par défaut")

    joueur.update_all_cartes(final_carte_list)

    print("_______________________________________\n")
    print("Votre tirage final est : \n")

    for carte_to_dispaly in joueur.get_carte_list():
        print(carte_to_dispaly.get_nom())

    result(mise, joueur)
