from .shapeGroups import ShapeGroups
from ..Shapes.triangle import Triangle
class Triangles(ShapeGroups):
   """
   Class for all of the Triangle objects. Inherits from the ShapeGroups object to get the values each triangle needs.
   """
   def createShapesForGroup(self):
      """Paints all of the triangles needed and places them in the list of triangles."""
      for i in range(self.wheelValuesCount): # Creates a triangle for every value that should be in the wheel.
         self.shapeGroup.append(Triangle(i,self.halfOfSize,self.degreesPerValue,self.wheelValuesCount)) 
