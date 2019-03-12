# -*-coding:utf-8 -*


class Map:
    """
    Map Class docstring
    """

    def __init__(self):
        self.mainmap = []

    def load_cart(self):
        # opening map.txt in mapo_file variable
        with open("map.txt", "r") as mapo_file:
            mapo = []
            for line in mapo_file:
                mapo_l = []
                for character in line:
                    if character != "\n":
                        mapo_l.append(character)

                if mapo_l:
                    mapo.append(mapo_l)
        self.mainmap = mapo
