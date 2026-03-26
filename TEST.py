import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Таблица")
window.resize(800, 500)

table = QTableWidget(5, 4)
window.setCentralWidget(table)

table.setHorizontalHeaderLabels(["Название", "1", "2", "3"])

# Строка 1
table.setItem(0, 0, QTableWidgetItem("Строка 1"))
table.item(0, 0).setFlags(table.item(0, 0).flags() | Qt.ItemFlag.ItemIsEditable)

btn1 = QPushButton("1")
table.setCellWidget(0, 1, btn1)

btn2 = QPushButton("2")
table.setCellWidget(0, 2, btn2)

btn3 = QPushButton("3")
table.setCellWidget(0, 3, btn3)

# Строка 2
table.setItem(1, 0, QTableWidgetItem("Строка 2"))
table.item(1, 0).setFlags(table.item(1, 0).flags() | Qt.ItemFlag.ItemIsEditable)

btn1 = QPushButton("1")
table.setCellWidget(1, 1, btn1)

btn2 = QPushButton("2")
table.setCellWidget(1, 2, btn2)

btn3 = QPushButton("3")
table.setCellWidget(1, 3, btn3)

# Строка 3
table.setItem(2, 0, QTableWidgetItem("Строка 3"))
table.item(2, 0).setFlags(table.item(2, 0).flags() | Qt.ItemFlag.ItemIsEditable)

btn1 = QPushButton("1")
table.setCellWidget(2, 1, btn1)

btn2 = QPushButton("2")
table.setCellWidget(2, 2, btn2)

btn3 = QPushButton("3")
table.setCellWidget(2, 3, btn3)

# Строка 4
table.setItem(3, 0, QTableWidgetItem("Строка 4"))
table.item(3, 0).setFlags(table.item(3, 0).flags() | Qt.ItemFlag.ItemIsEditable)

btn1 = QPushButton("1")
table.setCellWidget(3, 1, btn1)

btn2 = QPushButton("2")
table.setCellWidget(3, 2, btn2)

btn3 = QPushButton("3")
table.setCellWidget(3, 3, btn3)

# Строка 5
table.setItem(4, 0, QTableWidgetItem("Строка 5"))
table.item(4, 0).setFlags(table.item(4, 0).flags() | Qt.ItemFlag.ItemIsEditable)

btn1 = QPushButton("1")
table.setCellWidget(4, 1, btn1)

btn2 = QPushButton("2")
table.setCellWidget(4, 2, btn2)

btn3 = QPushButton("3")
table.setCellWidget(4, 3, btn3)

table.setColumnWidth(0, 200)
table.setColumnWidth(1, 100)
table.setColumnWidth(2, 100)
table.setColumnWidth(3, 100)

window.show()
sys.exit(app.exec())
