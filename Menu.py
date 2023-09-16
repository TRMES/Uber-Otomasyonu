from PyQt5.QtWidgets import QApplication
from welcomeScreen_python import Menu

app = QApplication([])
window = Menu()
window.show()
app.exec_()

