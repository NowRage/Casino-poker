def flush(carte_list):
    hearts = []
    clubs = []
    diamonds = []
    spades = []

    for carte in carte_list:
        if carte.color == "Trèfle":
            clubs.append(carte)
        elif carte.color == "Coeur":
            hearts.append(carte)
        elif carte.color == "Carrau":
            diamonds.append(carte)
        elif carte.color == "Pique":
            spades.append(carte)

    if len(hearts) == 5:
        return True
    elif len(clubs) == 5:
        return True
    elif len(diamonds) == 5:
        return True
    elif len(spades) == 5:
        return True
    else:
        return False