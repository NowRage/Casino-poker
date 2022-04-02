def full(carte_list):
    valeur_liste = []
    for val in carte_list:
        valeur_liste.append(str(val.value))

    filtered_valeur_liste = []
    for value in set(valeur_liste):
        filtered_valeur_liste.append(valeur_liste.count(value))

    sorted_list = sorted(filtered_valeur_liste, reverse=True)
    if sorted_list[0] == 3 and sorted_list[1] == 2:
        return True
    else:
        return False
