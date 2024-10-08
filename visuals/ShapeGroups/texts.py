from .shapeGroups import ShapeGroups
from ..Shapes.text import Text
class Texts(ShapeGroups):
    """
    Class for all of the ellipse objects that inherits from the ShapeGruops object to get the values each ellipse needs.
    """
    def setLinkData(self,linkData):
        self.linkData=linkData

    def createShapesForGroup(self):
        """Paints all of the text objects needed and places them in the list of ellipses."""
        for i in range(self.wheelValuesCount): # Creates an ellipse for every value that should be in the wheel.
            self.shapeGroup.append(Text(i,self.halfOfSize,self.degreesPerValue,self.wheelValuesCount))
            self.shapeGroup[i].setLinkData(self.linkData)
            