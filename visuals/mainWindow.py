import time,random,math
from PyQt6.QtWidgets import QApplication,QMainWindow
from PyQt6.QtGui import QPainter,QColor
class MainWindow(QMainWindow):
   """Inherits from QMainWindow to create a window for the wheel."""
   def __init__(self,size,linkData):
      """Constructor for MainWindow to create a window for the wheel."""
      super().__init__()
      self.linkData=linkData
      self.resize(size,size) # Creates the size of the window.
      self.rotate=0 # Keeps track of the amount the wheel has rotated.
      self.shapeGroups=[] # List of lists of shapes.
   def paintEvent(self,event):
      """Outputs the current wheel piece by piece."""
      super().paintEvent(event)
      painter=QPainter(self)
      painter.setRenderHint(QPainter.RenderHint.Antialiasing)
      for shapeGroup in self.shapeGroups: # Loops through the shape lists in order to output the entire wheel onto the screen.
         for shape in shapeGroup.shapeGroup:
            shape.paint(painter,self.rotate)
   def mousePressEvent(self,event):
      """If the mouse is clicked then spin the wheel a random amount."""
      spinAmount=random.randrange(1000,3000,1) # Randomize the amount to spin.
      for i in range(spinAmount): # Spin based on the randomized amount.
         time.sleep(.004) # Sleep a certain amount depending on how much the wheel has left to spin
         self.spin(spinAmount/(7*i+1))
      print(self.linkData[11-math.floor((self.rotate%360)/(360/len(self.linkData)))])
   def spin(self,degreesToSpin):
      """Updates the wheel to the current amount of rotation."""
      self.rotate+=degreesToSpin
      self.update()
      QApplication.processEvents()
