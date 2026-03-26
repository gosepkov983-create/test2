import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTableWidget, 
                             QTableWidgetItem, QPushButton, QVBoxLayout, 
                             QWidget, QHeaderView)
from PyQt6.QtCore import Qt

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Таблица с кнопками")
window.resize(800, 500)

# Центральный виджет
central = QWidget()
window.setCentralWidget(central)

# Layout
layout = QVBoxLayout()
central.setLayout(layout)

# Таблица
table = QTableWidget()
layout.addWidget(table)

# Настройка таблицы: 5 строк, 4 столбца
rows = 5
cols = 4

table.setRowCount(rows)
table.setColumnCount(cols)

# Заголовки столбцов
table.setHorizontalHeaderLabels(["Название", "1", "2", "3"])

# Заполняем левый столбец (названия строк, можно редактировать)
names = ["Строка 1", "Строка 2", "Строка 3", "Строка 4", "Строка 5"]

for i in range(rows):
    item = QTableWidgetItem(names[i])
    item.setFlags(item.flags() | Qt.ItemFlag.ItemIsEditable)
    table.setItem(i, 0, item)

# Заполняем остальные столбцы кнопками с цифрами
for row in range(rows):
    for col in range(1, cols):
        button = QPushButton(str(col))
        button.setEnabled(False)  # кнопка неактивна, не нажимается
        table.setCellWidget(row, col, button)

# Настройка размеров
table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
for i in range(1, cols):
    table.setColumnWidth(i, 100)

table.verticalHeader().setDefaultSectionSize(60)

window.show()
sys.exit(app.exec())
