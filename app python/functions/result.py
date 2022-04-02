from functions.full import *
from functions.flush import *
from functions.pair import *
from functions.carré import *
from functions.main import *
from functions.cinq import *
from functions.triple import *
from functions.pairs import *


def result(mise, joueur):
    joueur.argent_perdu(mise)
    print("_________________________________________________")
    if main(joueur.sort_carte_by_value()) == True and flush(joueur.sort_carte_by_value()) == True:
        gain = mise * 250
        joueur.win_argent(gain)
        print("Félicitation vous avez une Quinte Flush Royale!! vous remportez " + str(gain) + " €")
    elif flush(joueur.sort_carte_by_value()) == True and cinq(joueur.sort_carte_by_value()) == True:
        gain = mise * 50
        joueur.win_argent(gain)
        print("Félicitation vous avez une Quinte Flush !! vous remportez " + str(gain) + " €")
    elif carré(joueur.sort_carte_by_value()) == True:
        gain = mise * 25
        joueur.win_argent(gain)
        print("Félicitation vous avez un Carré !! vous remportez " + str(gain) + " €")
    elif full(joueur.sort_carte_by_value()) == True:
        gain = mise * 9
        joueur.win_argent(gain)
        print("Félicitation vous avez un full !! vous remportez " + str(gain) + " €")
    elif flush(joueur.sort_carte_by_value()) == True:
        gain = mise * 6
        joueur.win_argent(gain)
        print("Félicitation vous avez une couleur !! vous remportez " + str(gain) + " €")
    elif cinq(joueur.sort_carte_by_value()) == True:
        gain = mise * 4
        joueur.win_argent(gain)
        print("Félicitation vous avez une suite !! vous remportez " + str(gain) + " €")
    elif triple(joueur.sort_carte_by_value()) == True:
        gain = mise * 3
        joueur.win_argent(gain)
        print("Félicitation vous avez un brelan !! vous remportez " + str(gain) + " €")
    elif pairs(joueur.sort_carte_by_value()) == True:
        gain = mise * 2
        joueur.win_argent(gain)
        print("Félicitation vous avez deux paires !! vous remportez " + str(gain) + " €")
    elif pair(joueur.sort_carte_by_value()) == True:
        joueur.win_argent(mise)
        print("Vous avez une paire !! vous remportez " + str(mise) + " €")
    else:
        print("Dommage !! vous perdez " + str(mise) + " €")

    joueur.reset_cartes()
    print("Vous avez un crédit de " + str(joueur.get_argent()) + " €")
    print("_________________________________________________")
