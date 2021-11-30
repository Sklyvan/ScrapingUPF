from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor

darkPalette = QPalette()
darkPalette.setColor(QPalette.Window, QColor(48, 54, 67)) # Application background
darkPalette.setColor(QPalette.WindowText, Qt.white) # Application text
darkPalette.setColor(QPalette.Base, QColor(37, 42, 52)) # Text box background
darkPalette.setColor(QPalette.AlternateBase, QColor(53, 53, 53)) # I don't know what this is
darkPalette.setColor(QPalette.ToolTipBase, Qt.white) # Tooltip background
darkPalette.setColor(QPalette.ToolTipText, Qt.white) # Tooltip text
darkPalette.setColor(QPalette.Text, Qt.white) # User input text
darkPalette.setColor(QPalette.Button, QColor(42, 47, 58))
darkPalette.setColor(QPalette.ButtonText, Qt.white)
darkPalette.setColor(QPalette.BrightText, Qt.red)
darkPalette.setColor(QPalette.Link, QColor(42, 130, 218))
darkPalette.setColor(QPalette.Highlight, QColor(42, 130, 218))
darkPalette.setColor(QPalette.HighlightedText, Qt.black)
