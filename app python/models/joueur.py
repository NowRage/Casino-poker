class Joueur:
    def __init__(self, nom, argent, carte_list):
        self.nom = nom
        self.argent = argent
        self.carte_list = carte_list

    def get_nom(self):
     return self.nom

    def get_argent(self):
     return self.argent

    def get_carte_list(self):
        return self.carte_list

    def update_all_cartes(self, new_carte_list):
        self.carte_list = new_carte_list

    def add_carte(self, carte):
        self.carte_list.append(carte)

    def remove_carte(self, carte):
        self.carte_list.remove(carte)

    def reset_cartes(self):
        self.carte_list = []

    def win_argent(self, value):
        self.argent = self.argent + value

    def argent_perdu(self, value):
        self.argent = self.argent - value

    def sort_carte_by_value(self):
        self.carte_list = sorted(self.carte_list, key=lambda carte: carte.value)
        return  self.carte_list