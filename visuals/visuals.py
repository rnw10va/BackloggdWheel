import sys
from .mainWindow import MainWindow
from .ShapeGroups.triangles import Triangles
from .ShapeGroups.ellipses import Ellipses
from .ShapeGroups.texts import Texts
from PyQt6.QtWidgets import QApplication

class Visuals:
   """
   Initializes the visualas of the wheel and its' ability to spin.
   """
   def __init__(self):
      """Constructor for creating the wheel and its' ability to spin."""
      app=QApplication(sys.argv)
      size=500 # Size of window - This will be replaced to be adaptive to be the same size regardless of pixel count on the screen.
      wheelValuesCount=24 # The amount of values in the wheel - This will be replaced to be adaptive to the link placed in the wheel.
      window=MainWindow(size) # Creates the Main Window
      window.shapeGroups.append(Triangles(size,wheelValuesCount)) # Creates the group of Triangles that will be needed needed to create the jagged wheel.
      window.shapeGroups.append(Ellipses(size,wheelValuesCount)) # Creates the group of Ellipses that will be needed to round the wheel's edges.
      window.shapeGroups.append(Texts(size,wheelValuesCount))
      for shapeGroup in window.shapeGroups: # Loops through the groups to actually create each individual tringle and ellipse's object.
         shapeGroup.createShapesForGroup()
      window.show()
      app.exec()