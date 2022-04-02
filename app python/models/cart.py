class carte:
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def get_nom(self):
        nom = str(self.value) + " de " + self.color

        if self.value == 11:
            nom = "Valet de " + self.color
        elif self.value == 12:
            nom = "Dame de " + self.color
        elif self.value == 13:
            nom = "Roi de " + self.color
        elif self.value == 1:
            nom = "As de " + self.color

        return nom

    def get_value(self):
       return self.value

    def get_color(self):
        return self.color