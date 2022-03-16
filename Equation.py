

Welcome to Gafaru Python Class
import math
class Quadratic:
  def __init__(self,a,b,c):
    self.a = a
    self.b = b
    self.c = c
    
  def insert_values(self):
    self.a = int(input(>>))
    self.b = int(input(>>))
    self.c = int(input(>>))
    
  def calc_xs(self):
    self.x1 = (-(self.b) + sqt((self.b**2) - 4 * self.a * self.c))/ 2 * self.a
    self.x2 = (-(self.b) - sqt((self.b**2) - 4 * self.a * self.c))/ 2 * self.a
    
    rerurn self.x1 , self.x2
    
  def total_y(self):
    self.y1 = (self.x1)**2 * self.a + (self.x1) * self * b + self.c
    self.y2 = (self.x2)**2 * self.a + (self.x2) * self * b + self.c
    
    return self.y1 , self.y2
  
  def ask_question(self):
    
     while True:
        self.quest = int(input("Choose 1 or 2"))
        if self.quest == 1:
          print('you want to solve for x1 and x2')
          print('x1 = ',self.x1, 'x2 =', self.x2)
          
        elif self.quest == 2:
          print('You want to solve for the total value of y')
          printprint('y1 = ',self.y1, 'y2 =', self.y2)
          
        else:
          print('we can only solve for x and y')
        
    
    
formular = Quadratic()

print(formular.insert_values())
print(formular.calc_xs())
print(formular.total_y())



print('Done')
