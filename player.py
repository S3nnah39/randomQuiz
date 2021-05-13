
class player:
     def __init__(self,name):
          self.__name = name
          self.__wins = 0
          self.__loses = 0
          
     def get_name(self):
          return self.__name

     def get_wins(self):
          return self.__wins
     
     def get_loses(self):
          return self.__loses
    

     def set_wins(self):
          self.__wins = self.__wins + 1

     def set_loses(self):
          self.__loses = self.__loses + 1


