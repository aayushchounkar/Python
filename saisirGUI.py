# hello.py
"""Simple Hello, World example with PyQt6."""
import sys

# 1. Import QApplication and all the required widgets
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

# 2. Create an instance of QApplication
app = QApplication([])

# 3. Create your application's GUI
window = QWidget()
window.setWindowTitle("*-CHONKYY-*")#NAME OF TITLE 
window.setGeometry(100, 100, 580,500 )#SIZE OF WINDOW
helloMsg = QLabel("<h1>HEYY,GUYSS CHONKYY HERE !!🚀👻</h1>", parent=window)
helloMsg.move(60, 15)

# 4. Show your application's GUI
window.show()

# 5. Run your application's event loop
sys.exit(app.exec())