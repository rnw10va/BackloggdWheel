import math
from .shape import Shape
from PyQt6 import QtCore
from PyQt6.QtGui import QColor
class Text(Shape):
    """
    Class for a Triangle object. Inherits from the Shape object to get the values the Triangle needs.
    """
    def paint(self,painter,rotate):
        if not painter.isActive():
            return
        painter.save()
        painter.translate(self.halfOfSize,self.halfOfSize)
        painter.rotate(rotate)
        painter.translate((self.halfOfSize+self.x2-self.halfOfSize+self.x)//3,(self.halfOfSize+self.y2-self.halfOfSize+self.y)//3)
        #painter.rotate(self.t2+self.degreesPerValue*(self.wheelValuesCount/2-1)/2)
        painter.setPen(QColor(0,0,0))
        # ADD FONT ADJUSTMENT HERE
        painter.rotate(math.floor((self.t2+self.t)/2))
        #painter.translate((self.halfOfSize+self.x2-self.halfOfSize+self.x)//2,(self.halfOfSize+self.y2-self.halfOfSize+self.y)//2)
        painter.drawText(0,math.ceil(-72/self.wheelValuesCount),"textTEXTtext")
        painter.restore()
