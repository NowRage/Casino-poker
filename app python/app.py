from models.joueur import Joueur
from functions.jeux import *


def main():
    print("\n_________________________________________________")
    print('\nBienvenu sur mon jeux')
    print("\n_________________________________________________")
    nom = input("\nQuel est votre pseudo ? ")
    print("\n_________________________________________________")
    argent = int(input("\nBonjour " + nom + ". Combien de crédit voulez-vous acheter ? "))
    print("\n_________________________________________________")
    print("\nTrès bien, commençons la partie. Bonne Chance " + nom + "!!")
    print("\n_________________________________________________")

    joueur = Joueur(nom, argent, [])

    while joueur.get_argent() > 0:
        mise = int(input("\nCombien Voulez-vous miser ? "))
        print("\n_________________________________________________")
        if mise <= joueur.get_argent():
            jeux(mise, joueur)
        else:
            print("\nJe suis désolé mais vous n'avez pas assez de crédit ")
            print("\n_________________________________________________")

    if joueur.get_argent() < 1:
        print("\nJe suis désolé mais vous avez perdu tout vos crédits.\nVous aurez plus de chance la prochaine fois.")
        print("\n_________________________________________________")
        encours = input("\nVoulez-vous recommencer la partie ? oui/non ")
        if encours == "oui":
            main()
        else:
            print("\n_________________________________________________")
            print("Au revoir " + joueur.get_nom())


main()