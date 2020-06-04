import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
print(sys.argv)

btn = QPushButton("Quit")
btn.show()

app.exec_()
