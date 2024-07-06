import math
from .shape import Shape
from PyQt6 import QtCore
class Ellipse(Shape):
   """
   Class for a Ellipse object. Inherits from the Shape object to get the values the Ellipse needs.
   """
   def paint(self,painter,rotate):
      self.paintHelper(painter)
      painter.translate(self.halfOfSize,self.halfOfSize)
      painter.rotate(rotate)
      painter.translate(-self.halfOfSize,-self.halfOfSize)
      point=QtCore.QPointF(500/2+self.x,500/2+self.y)
      dist=math.floor(math.dist([self.x2,self.y2],[self.x,self.y]))
      painter.translate(point)
      painter.rotate(self.t2+self.degreesPerValue*(self.wheelValuesCount/2-1)/2)
      painter.drawEllipse(0,math.ceil(-72/self.wheelValuesCount),dist,math.floor(self.degreesPerValue/2))
      painter.restore()