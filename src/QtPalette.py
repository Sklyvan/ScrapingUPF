from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor

Color1 = QColor(46, 52, 64)
Color2 = QColor(59, 66, 82)
Color3 = QColor(67, 76, 94)
Color4 = QColor(76, 86, 106)

darkPalette = QPalette()
darkPalette.setColor(QPalette.Window, Color2) # Application background
darkPalette.setColor(QPalette.WindowText, Qt.white) # Application text
darkPalette.setColor(QPalette.Base, Color4) # Text box background
darkPalette.setColor(QPalette.AlternateBase, QColor(53, 53, 53)) # I don't know what this is
darkPalette.setColor(QPalette.ToolTipBase, Qt.white) # Tooltip background
darkPalette.setColor(QPalette.ToolTipText, Qt.white) # Tooltip text
darkPalette.setColor(QPalette.Text, Qt.white) # User input text
darkPalette.setColor(QPalette.Button, Color1)
darkPalette.setColor(QPalette.ButtonText, Qt.white)
darkPalette.setColor(QPalette.BrightText, Qt.red)
darkPalette.setColor(QPalette.Link, QColor(42, 130, 218))
darkPalette.setColor(QPalette.Highlight, QColor(42, 130, 218))
darkPalette.setColor(QPalette.HighlightedText, Qt.black)
