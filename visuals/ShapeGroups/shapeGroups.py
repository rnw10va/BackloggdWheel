class ShapeGroups():
   """
   Parent class for groups of shapes objects. The data is the same in the groups.
   """
   def __init__(self,size,wheelValuesCount,parent=None):
      """Constructor for the parent class of the groups of shapes."""
      self.halfOfSize=size/2 # Half of screen size.
      self.wheelValuesCount=wheelValuesCount
      self.degreesPerValue=360/wheelValuesCount # Degrees needed for the size of each circle piece.
      self.shapeGroup=[] # List of shapes for whichever shape group is inheriting from this class.
