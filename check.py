#!/usr/bin/env python
# coding: utf-8


import json
import sys

from qt_gui import *

app = QApplication()
MainWindow = QMainWindow(None)
ui = Ui_MainWindow()
ui.setupUi(MainWindow)


class Check_Antivirus:  # 检测应用
    def __init__(self):
        with open('./antivirus.json', 'r') as f:
            data = json.loads(f.read())
            print(data)
            self.antivirus = data

    def process_info(self):
        res = []
        process_name = ui.textEdit.toPlainText().strip().split()
        if len(process_name) > 0 and process_name is not None:
            for i, j in self.antivirus.items():
                if i in process_name:
                    res.append({"process": i, "name": j})
            if len(res) > 0:
                ui.tableWidget.setRowCount(len(res))
                for s in range(len(res)):
                    for l in range(2):
                        key = list(res[s].keys())
                        data = QTableWidgetItem(res[s][key[l]])
                        ui.tableWidget.setItem(s, l, data)


def main():
    check = Check_Antivirus()
    ui.pushButton.clicked.connect(lambda: check.process_info())
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
