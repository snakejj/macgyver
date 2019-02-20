# -*-coding:utf-8 -*

from random import randrange
from classes.mac import Mac

mac = Mac()

class Obj:
    """
    Docstring de la classe
    """

    
    def __init__(self,maze):
        self.obj1_x = int() 
        self.obj1_y = int() 
        self.obj2_x = int() 
        self.obj2_y = int() 
        self.obj3_x = int() 
        self.obj3_y = int() 
        self.maze = maze

    def random_obj(self):
        
        tempobj1_x = randrange(14)
        tempobj1_y = randrange(14)
        tempobj2_x = randrange(14)
        tempobj2_y = randrange(14)
        tempobj3_x = randrange(14)
        tempobj3_y = randrange(14)

        
        
        
        while self.maze[tempobj1_x][tempobj1_y] != "@"\
        or self.maze[tempobj2_x][tempobj2_y] != "@"\
        or self.maze[tempobj3_x][tempobj3_y] != "@"\
        or self.maze[tempobj1_x][tempobj1_y] != \
        self.maze[tempobj2_x][tempobj2_y]\
        or self.maze[tempobj1_x][tempobj1_y] != \
        self.maze[tempobj3_x][tempobj3_y]\
        or self.maze[tempobj2_x][tempobj2_y] != \
        self.maze[tempobj3_x][tempobj3_y]:
            tempobj1_x = randrange(14)
            tempobj1_y = randrange(14)
            tempobj2_x = randrange(14)
            tempobj2_y = randrange(14)
            tempobj3_x = randrange(14)
            tempobj3_y = randrange(14)
        
        self.obj1_x = tempobj1_x
        self.obj1_y = tempobj1_y
        self.obj2_x = tempobj2_x
        self.obj2_y = tempobj2_y
        self.obj3_x = tempobj3_x
        self.obj3_y = tempobj3_y                
        
        
        
        return self.obj1_x, self.obj1_y, self.obj2_x, self.obj2_y,\
               self.obj3_x, self.obj3_y
        
            
        

