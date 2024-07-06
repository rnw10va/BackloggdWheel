from .shapeGroups import ShapeGroups
from ..Shapes.ellipse import Ellipse
class Ellipses(ShapeGroups):
   """
   Class for all of the ellipse objects that inherits from the ShapeGruops object to get the values each ellipse needs.
   """
   def createShapesForGroup(self):
      """Paints all of the ellipses needed and places them in the list of ellipses."""
      for i in range(self.wheelValuesCount): # Creates an ellipse for every value that should be in the wheel.
         self.shapeGroup.append(Ellipse(i,self.halfOfSize,self.degreesPerValue,self.wheelValuesCount))