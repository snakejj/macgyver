# -*-coding:utf-8 -*

from random import randrange


class Obj:
    """
    Obj class Docstring
    """

    def __init__(self, maze):
        self.obj_x = int()
        self.obj_y = int()
        self.objcounter = 0
        self.maze = maze
        self.objpick = False

    def random_obj(self):
        self.obj_x = randrange(14)
        self.obj_y = randrange(14)

        while self.maze[self.obj_x][self.obj_y] != "@":
            self.obj_x = randrange(14)
            self.obj_y = randrange(14)

        return self.obj_x, self.obj_y
