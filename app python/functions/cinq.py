def cinq(carte_list):
    list_of_correct_followin_value = []
    for i in range(len(carte_list)-1):
        if carte_list[i].get_value() - carte_list[i + 1].get_value() == -1:
            list_of_correct_followin_value.append(True)

    if len(list_of_correct_followin_value) == 4:
        return True
    elif carte_list[0].get_value() == 1 and carte_list[1].get_value() == 10 and carte_list[2].get_value() == 11 and carte_list[3].get_value() == 12 and carte_list[4].get_value() == 13:
       return True
    else:
     return False