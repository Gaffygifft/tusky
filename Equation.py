

Welcome to Gafaru Python Class
from math import sqrt

class Quadratic:
  def __init__(self):
#     self.a = a
#     self.b = b
#     self.c = c
    
#  def insert_values(self):
    self.a = int(input(">>"))
    self.b = int(input(">>"))
    self.c = int(input(">>"))
    
#   def calc_xs(self):
#     self.x1 = (-(self.b) + sqt((self.b**2) - 4 * self.a * self.c))/ 2 * self.a
#     self.x2 = (-(self.b) - sqt((self.b**2) - 4 * self.a * self.c))/ 2 * self.a
#     
#     print(self.x1 , self.x2)
#     
#   def total_y(self):
#     self.y1 = (self.x1)**2 * self.a + (self.x1) * self * b + self.c
#     self.y2 = (self.x2)**2 * self.a + (self.x2) * self * b + self.c
#     
#     print(self.y1 , self.y2)
#   
  def ask_question(self):
    
     while True:
        self.quest = int(input("Choose 1 or 2"))
        if self.quest == 1:
            self.x1 = (-(self.b) + sqrt((self.b**2) - 4 * self.a * self.c))/ 2 * self.a
            self.x2 = (-(self.b) - sqrt((self.b**2) - 4 * self.a * self.c))/ 2 * self.a
            print('you want to solve for x1 and x2')
            print(self.x1 , self.x2)
            
          
        elif self.quest == 2:
            self.y1 = (self.x1)**2 * self.a + (self.x1) * self.b + self.c
            self.y2 = (self.x2)**2 * self.a + (self.x2) * self.b + self.c
            print('You want to solve for the total value of y')
            print(self.y1 , self.y2)
            
          
        else:
          print('we can only solve for x and y')
        
    
    
formular = Quadratic()

formular.ask_question()




print('Done')

print('thank you')

    

