import sys
import os
from pathlib import Path
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt


def get_apps():
    paths = [
        Path(os.getenv("PROGRAMDATA")) / "Microsoft/Windows/Start Menu/Programs",
        Path(os.getenv("APPDATA")) / "Microsoft/Windows/Start Menu/Programs"
    ]

    BLACKLIST = [
        "uninstall", "install", "update", "helper",
        "apphost", "runtime", "service", "crash",
        "debug", "setup", "maintenance", "feedback"
    ]

    apps = []

    for base in paths:
        if base.exists():
            for file in base.rglob("*.lnk"):
                name = file.name.lower()

                if any(word in name for word in BLACKLIST):
                    continue

                apps.append(file)

    apps = list(set(apps))
    apps.sort(key=lambda x: x.name.lower())
    return apps



def open_app(path):
    try:
        os.startfile(path)
    except Exception as e:
        print("Er:", e)


app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Приложение")
window.resize(1000, 500)


main_widget = QWidget()
layout = QHBoxLayout(main_widget)
window.setCentralWidget(main_widget)




app_table = QTableWidget()
app_table.setColumnCount(1)
app_table.setHorizontalHeaderLabels(["Приложения"])


layout.addWidget(app_table)

apps = get_apps()

def show_apps(app_list):
    app_table.setRowCount(len(app_list))
    for row, app_path in enumerate(app_list):
        item = QTableWidgetItem(app_path.stem)
        item.setData(1000, str(app_path))
        app_table.setItem(row, 0, item)

    app_table.setColumnWidth(0, 700)


show_apps(apps)


def launch_app(row, column):
    item = app_table.item(row, 0)
    path = item.data(1000)
    open_app(path)

app_table.cellClicked.connect(launch_app)

window.show()
sys.exit(app.exec())
