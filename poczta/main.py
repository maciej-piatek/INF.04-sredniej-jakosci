from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("menu.ui",self)
        self.setWindowTitle("Nadaj przesyłkę 2137")
        self.but.clicked.connect(self.poleradio)
        self.but2.clicked.connect(self.zatwierdz)

    def poleradio(self):
        if (self.rbut1.isChecked()):
            self.wyswietlcene.setText("1 zł")
            obraz1 = QPixmap("pocztowka.png")
            self.obraz.setPixmap(obraz1)
        elif (self.rbut2.isChecked()):
            self.wyswietlcene.setText("1,5 zł")
            obraz2 = QPixmap("list.png")
            self.obraz.setPixmap(obraz2)
        elif (self.rbut3.isChecked()):
            self.wyswietlcene.setText("10 zł")
            obraz3 = QPixmap("paczka.png")
            self.obraz.setPixmap(obraz3)

    def zatwierdz(self):
        msg = QMessageBox()
        uwu = self.le_3.text()
        if (len(uwu) == 5):
            msg.setText("dobry kod pocztowy")
        else:
            msg.setText("ma być 5 liczb w kodzie pocztowym")



        msg.exec_()


app = QApplication([])
okno = MainWindow()
okno.show()
app.exec_()
