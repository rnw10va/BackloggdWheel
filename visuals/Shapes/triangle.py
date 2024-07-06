import math
from .shape import Shape
from PyQt6 import QtGui,QtCore
from PyQt6.QtGui import QColor
class Triangle(Shape):
   """
   Class for a Triangle object. Inherits from the Shape object to get the values the Triangle needs.
   """
   def paint(self,painter,rotate):
      self.paintHelper(painter)
      painter.translate(self.halfOfSize,self.halfOfSize)
      painter.rotate(rotate)
      painter.translate(-self.halfOfSize,-self.halfOfSize)
      polygon=QtGui.QPolygonF()
      polygon.append(QtCore.QPointF(self.halfOfSize,self.halfOfSize))
      polygon.append(QtCore.QPointF(math.floor(self.halfOfSize+self.x),math.floor(self.halfOfSize+self.y)))
      polygon.append(QtCore.QPointF(math.floor(self.halfOfSize+self.x2),math.floor(self.halfOfSize+self.y2)))
      painter.drawPolygon(polygon)
      painter.restore()
