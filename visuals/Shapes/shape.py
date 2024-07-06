import math
from PyQt6.QtGui import QColor
class Shape():
   """
   Parent class for all shape objects. A lot of the data needed is the same across the different shapes.
   """
   def __init__(self,wheelCountValue,halfOfSize,degreesPerValue,wheelValuesCount,parent=None):
      """Constructor for the parent class of shapes."""
      self.halfOfSize=halfOfSize
      self.wheelValuesCount=wheelValuesCount
      self.degreesPerValue=degreesPerValue
      self.brushColor=self.getBrushColor(wheelCountValue)
      self.penColor=QColor(0,0,0,0)
      self.math(wheelCountValue)
   def paint(self,painter,rotate):
      """Default paint method."""
      pass
   def paintHelper(self,painter):
      """Helps finish painting any shape."""
      if not painter.isActive():
         return
      painter.save()
      painter.setBrush(self.brushColor)
      painter.setPen(self.penColor)

   def getBrushColor(self,wheelCountValue):
      """Gets the next brush color that is needed in the circle."""
      r,g,b=0,0,0
      match wheelCountValue%6:
         case 0:
            r=255
         case 1:
            g=255
         case 2:
            b=255
         case 3:
            r=255
            g=255
         case 4:
            r=255
            b=255
         case _:
            g=255
            b=255
      return QColor(r,g,b)
   
   def math(self,wheelCountValue):
      """Does the math needed to know where every shape should be in the circle."""
      self.t=self.degreesPerValue*wheelCountValue # Finds the degrees needed for the x and y axis values of the first of the two non-middle triangle points.
      self.t2=self.degreesPerValue*((wheelCountValue+1)%self.wheelValuesCount) # Finds the degrees needed for the x and y axis values of the first of the two non-middle triangle points.
      self.x=self.halfOfSize*math.cos(math.radians(self.t)) # x-axis of the first of the two non-middle triangle points.
      self.y=self.halfOfSize*math.sin(math.radians(self.t)) # y-axis of the first of the two non-middle triangle points.
      self.x2=self.halfOfSize*math.cos(math.radians(self.t2)) # x-axis of the second of the two non-middle triangle points.
      self.y2=self.halfOfSize*math.sin(math.radians(self.t2)) # y-axis of the second of the two non-middle triangle points.

