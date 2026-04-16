import sys
import os
import psutil
from pathlib import Path
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QSize, QFileInfo, QTimer
from PyQt6.QtWidgets import QFileIconProvider

icon_provider = QFileIconProvider()

# 💾 история запусков
launch_history = []
seen_processes = set()


# 🧠 иконка
def get_icon(path):
    return icon_provider.icon(QFileInfo(str(path)))


# 📦 недавно установленные
def get_recent_installed(limit=30):
    paths = [
        Path(os.getenv("PROGRAMDATA")) / "Microsoft/Windows/Start Menu/Programs",
        Path(os.getenv("APPDATA")) / "Microsoft/Windows/Start Menu/Programs"
    ]

    apps = []

    for base in paths:
        if base.exists():
            for file in base.rglob("*.lnk"):
                apps.append(file)

    apps.sort(key=lambda x: x.stat().st_mtime, reverse=True)
    return apps[:limit]


# 🚀 обновление истории процессов
def update_running_history():
    global launch_history, seen_processes

    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        try:
            pid = proc.info['pid']
            exe = proc.info['exe']

            if not exe:
                continue

            if pid not in seen_processes:
                seen_processes.add(pid)

                path = Path(exe)

                # добавляем в начало списка
                launch_history.insert(0, path)

                # убираем дубликаты по пути
                unique = []
                seen_paths = set()
                for p in launch_history:
                    if str(p) not in seen_paths:
                        unique.append(p)
                        seen_paths.add(str(p))

                launch_history = unique[:30]

        except:
            continue

    # если открыта вкладка "Недавно запущенные", обновляем таблицу
    if category_list.currentItem().text() == "Недавно запущенные":
        show_items(launch_history)


# 🚀 запуск
def open_item(path):
    try:
        os.startfile(path)
    except Exception as e:
        print("Ошибка:", e)


# 📋 показать элементы
def show_items(items):
    table.setRowCount(len(items))

    for row, path in enumerate(items):
        item = QTableWidgetItem(path.stem)
        item.setIcon(get_icon(path))
        item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)

        table.setItem(row, 0, item)

        btn = QPushButton("▶")
        btn.clicked.connect(lambda _, p=str(path): open_item(p))
        table.setCellWidget(row, 1, btn)

    table.setColumnWidth(0, 600)
    table.setColumnWidth(1, 100)


# 🖥️ GUI
app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Лаунчер")
window.resize(1000, 500)

main_widget = QWidget()
layout = QHBoxLayout(main_widget)
window.setCentralWidget(main_widget)

# категории
category_list = QListWidget()
category_list.addItems(["Недавно установленные", "Недавно запущенные"])
category_list.setFixedWidth(250)

# таблица
table = QTableWidget()
table.setColumnCount(2)
table.setHorizontalHeaderLabels(["Название", ""])
table.setIconSize(QSize(32, 32))

layout.addWidget(category_list)
layout.addWidget(table)


# переключение категорий
def on_category_changed():
    current = category_list.currentItem().text()

    if current == "Недавно установленные":
        show_items(get_recent_installed())
    elif current == "Недавно запущенные":
        show_items(launch_history)


category_list.currentItemChanged.connect(lambda: on_category_changed())

# старт
category_list.setCurrentRow(0)

# ⏱️ таймер обновления каждые 2 секунды
timer = QTimer()
timer.timeout.connect(update_running_history)
timer.start(2000)

window.show()
sys.exit(app.exec())
