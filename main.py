import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from cof import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.show()
        self.con = sqlite3.connect("coffee.sqlite")
        cur = self.con.cursor()
        self.pushButton.clicked.connect(self.run)

    def run(self):
        cur = self.con.cursor()
        if self.lineEdit.text():
            result = cur.execute(f'{self.lineEdit.text()}').fetchall()
        else:
            result = cur.execute('SELECT * FROM variants').fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
