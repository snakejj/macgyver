# -*-coding:utf-8 -*


from classes.map import Map

map = Map()

class Mac:
    """
    Docstring de la classe
    """

    
    

    def __init__(self,maze):
        self.mac_x = int() 
        self.mac_y = int()
        self.maze = maze
        self.front_g = False

    def mac_down(self):
        
        if self.mac_y < 280 and self.maze[int(self.mac_y /20+1)]\
        [int(self.mac_x / 20)] == "G" :
            self.front_g = True    
        elif self.mac_y < 280 and self.maze[int(self.mac_y /20+1)]\
        [int(self.mac_x / 20)] == "@" :
            self.mac_y += 20
            print("mac_y =",self.mac_y)
            return self.mac_x, self.mac_y       
        else:
            print("mac_y =",self.mac_y)
            return self.mac_x, self.mac_y

    def mac_up(self):

        if self.mac_y > 0 and self.maze[int(self.mac_y /20-1)]\
        [int(self.mac_x / 20)] == "G":
            self.front_g = True
        elif self.mac_y > 0 and self.maze[int(self.mac_y /20-1)]\
        [int(self.mac_x / 20)] == "@" or self.maze[int(self.mac_y /20-1)]\
        [int(self.mac_x / 20)] == "M" :
            self.mac_y -= 20
            print("mac_y =", self.mac_y)
            return self.mac_x, self.mac_y
        else:
            print("mac_y =",self.mac_y)
            return self.mac_x, self.mac_y

    def mac_right(self):
        


        if self.mac_x < 280 and self.maze[int(self.mac_y /20)]\
        [int(self.mac_x / 20 + 1)] == "G" :
            self.front_g = True

        elif self.mac_x < 280 and self.maze[int(self.mac_y /20)]\
        [int(self.mac_x / 20 + 1)] == "@" :
            self.mac_x += 20
            print("mac_x =",self.mac_x)
            return self.mac_x, self.mac_y
        
        else:
            print("mac_x =",self.mac_x)
            return self.mac_x, self.mac_y

    def mac_left(self):


        if self.mac_x > 0 and self.maze[int(self.mac_y /20)]\
           [int(self.mac_x / 20 - 1)] == "G" :
            self.front_g = True
        elif self.mac_x > 0 and self.maze[int(self.mac_y /20)]\
        [int(self.mac_x / 20 - 1)] == "@" or self.maze[int(self.mac_y /20-1)]\
        [int(self.mac_x / 20 - 1)] == "M" :
            self.mac_x -= 20
            print("mac_x =",self.mac_x)
            return self.mac_x, self.mac_y
        else:
            print("mac_x =",self.mac_x)
            return self.mac_x, self.mac_y

