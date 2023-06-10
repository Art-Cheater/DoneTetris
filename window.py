import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDesktopWidget, QMessageBox
from engine2 import Board2
from engine1 import Board
from engine3 import TetrisGame

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        self.main_window = MainWindow 
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 760)
        self.setStyleSheet("background-color: rgb(245,255,250);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.rules_dialog = None  # Переменная окна правил игры
        
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(173, 216, 230);")
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        
        self.input_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(10)
        self.input_label.setFont(font)
        self.input_label.setAlignment(QtCore.Qt.AlignCenter)
        self.input_label.setText("Введите ник:")
        self.gridLayout.addWidget(self.input_label, 1, 1)
        
        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.setStyleSheet("background-color: rgb(245,255,250);")
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 2, 1)

        self.btn_new = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(10)
        self.btn_new.setFont(font)
        self.btn_new.setObjectName("btn_new")
        self.gridLayout.addWidget(self.btn_new, 3, 1)

        self.btn_new_p = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(10)
        self.btn_new_p.setFont(font)
        self.btn_new_p.setObjectName("btn_new_p")
        self.gridLayout.addWidget(self.btn_new_p, 4, 1)

        self.btn_rules = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(10)
        self.btn_rules.setFont(font)
        self.btn_rules.setObjectName("btn_rules")
        self.btn_rules.setText("Правила")
        self.btn_rules.clicked.connect(self.pravila_game)
        self.gridLayout.addWidget(self.btn_rules, 5, 1)

        self.btn_record = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btn_record.setFont(font)
        self.btn_record.setObjectName("btn_record")
        self.gridLayout.addWidget(self.btn_record, 6, 1)

        self.btn_close = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(10)
        self.btn_close.setFont(font)
        self.btn_close.setObjectName("btn_close")
        self.gridLayout.addWidget(self.btn_close, 7, 1)


        
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(7, 1)
        self.gridLayout.setColumnStretch(0, 1)

        # Установка минимальных размеров элементов
        self.label.setMinimumSize(QtCore.QSize(200, 50))
        self.input_label.setMinimumSize(QtCore.QSize(200, 30))
        self.textEdit.setMinimumSize(QtCore.QSize(200, 30))
        self.btn_close.setMinimumSize(QtCore.QSize(200, 50))
        self.btn_new.setMinimumSize(QtCore.QSize(200, 50))
        self.btn_new_p.setMinimumSize(QtCore.QSize(200, 50))
        self.btn_record.setMinimumSize(QtCore.QSize(200, 50))
        self.btn_rules.setMinimumSize(QtCore.QSize(200, 50))
        
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.show()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    def pravila_game(self):
        if not self.rules_dialog:  # Проверяем, существует ли уже окно правил игры
            self.rules_dialog = QMessageBox(self.main_window)
            self.rules_dialog.setWindowTitle("Правила игры")
            self.rules_dialog.setText("Цель игры - удалить как можно больше линий и набрать очки\n\n"
                                "1. Двигать фигуры вправо и влево с помощью стрелочек влево и вправо\n"
                                "2. Фигуры можно переворачивать стрелочкой вверх\n"
                                "3. Фигуры можно ускорять стрелочкой вниз\n"
                                "4. Вы можете заменить фигуру нажав кнопку 'shift'.\n"
                                "5. Вы можете поставить игру на паузу буквой 'p' и при повторном нажатии игра продолжится\n"
                                "6. Вы можете нажать кнопку 'Escape' и появится окно с выбором дальнейшего действия\n"
                                "7. Игра закончится когда фигуры достигнут верхушки окна.\n"
                                "8. Ваш рекорд отобразится в главном меню.\n\n"
                                "Удачи!")
            self.rules_dialog.setStandardButtons(QMessageBox.Ok)
        self.rules_dialog.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tetris"))
        self.label.setText(_translate("MainWindow", "Тетрис"))
        self.input_label.setText(_translate("MainWindow", "Введите ник"))
        self.btn_new.setText(_translate("MainWindow", "Тетрис"))
        self.btn_new_p.setText(_translate("MainWindow", "Полимис"))
        self.btn_record.setText(_translate("MainWindow", "Рекорды"))
        self.btn_close.setText(_translate("MainWindow", "Выход из игры"))

    def add_functions(self):
        self.btn_new.clicked.connect(lambda: self.start_game())
        self.btn_new_p.clicked.connect(lambda: self.start_game_p())
        self.btn_record.clicked.connect(lambda: self.start_records())
        self.btn_new.clicked.connect(lambda: self.save_records())
        self.btn_close.clicked.connect(lambda: self.close_game())

    def close_game(self):
        reply = QMessageBox.question(
        self.main_window, "Выход", "Вы уверены, что хотите выйти из игры?", QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            self.main_window.close()
        else:
            self.main_window.show()
        
    def start_records(self):
        self.main_window.hide()
        self.record_window = RecordsWindow(self.main_window)
        self.record_window.show()

    def save_records(self):
        text = self.textEdit.text()
        with open("records.txt", "a") as file:
            file.write(text + ":" + ' ')

    def start_game(self):
        self.main_window.hide()
        self.tetris = Tetris()
        self.tetris.main_window = self.main_window
        self.tetris.show()

    def start_game_p(self):
        self.main_window.hide()
        self.tetris2 = Tetris2()
        self.tetris2.main_window = self.main_window
        self.tetris2.show()

    def write_number(self, number):
        if self.label.text() == "0": 
            self.label.setText(number)
        else:
            self.label.setText(self.label.text()+number)

class Tetris(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.tboard = Board(self)
        self.main_window = MainWindow
        self.setCentralWidget(self.tboard)
        self.resize(360, 760)
        self.setStyleSheet("background-color: rgb(245,255,250);")

        self.statusbar = self.statusBar()
        self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)
        self.tboard.game_over_signal.connect(self.game_over)
        self.tboard.keyPressevent.connect(self.pause_esc)

        self.tboard.start()
        self.center()
        self.setWindowTitle('Tetris')

        self.show()

    def end_game(self, score):
        with open("records.txt", "a") as file:
            print('sdv')
            file.write(str(score) + "\n")

    def game_over(self):
        game_over = QMessageBox()
        game_over.setWindowTitle("Конец игры")
        game_over.setText("Игра окончена. Выберите дальнейшее действие")
        game_over.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        game_over.setDefaultButton(QMessageBox.Yes)

        new_game_button = game_over.button(QMessageBox.Yes)
        new_game_button.setText("Новая игра")

        main_menu_button = game_over.button(QMessageBox.No)
        main_menu_button.setText("Главное меню")

        reply = game_over.exec()

        if reply == QMessageBox.Yes:
            self.start_game()
        elif reply == QMessageBox.No:
            self.menu()

    def pause_esc(self):
        escape = QMessageBox()
        escape.setWindowTitle("Игра приостановлена")
        escape.setText("Выберите дальнейшее действие")
        escape.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Reset)

        new_button = escape.button(QMessageBox.Yes)
        new_button.setText("Новая игра")

        main_button = escape.button(QMessageBox.No)
        main_button.setText("Главное меню")

        resume_button = escape.button(QMessageBox.Reset)
        resume_button.setText("Продолжить")

        escape.exec()

        clicked_button = escape.clickedButton()

        if clicked_button == new_button:
            self.start_game()
        elif clicked_button == main_button:
            self.menu()
        elif clicked_button == resume_button:
            self.tboard.resume()

    def menu(self):
        self.tboard.close()
        self.close()  # Закрыть окно игры
        self.main_window.show()  # Показать главное меню
        self.end_game(self.tboard.numLinesRemoved)

    def start_game(self):
        self.tboard.close()
        self.close()
        self.tetris = Tetris()
        self.tetris.show()

    def resizeEvent(self, event):
        self.center()
        return super().resizeEvent(event)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class Tetris2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.tboard = Board2(self) 
        self.main_window = MainWindow
        self.setCentralWidget(self.tboard)
        self.resize(360, 760)
        self.setStyleSheet("background-color: rgb(245,255,250);")

        self.statusbar = self.statusBar()
        self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)
        self.tboard.game_over_signal.connect(self.game_over)
        self.tboard.keyPressevent.connect(self.pause_esc)
        self.tboard.start()
        self.center()
        self.setWindowTitle('Tetris')

        self.show()

    def end_game(self, score):
        with open("records.txt", "a") as file:
            print('sdv')
            file.write(str(score) + "\n")

    def game_over(self):
        game_over = QMessageBox()
        game_over.setWindowTitle("Конец игры")
        game_over.setText("Игра окончена. Выберите дальнейшее действие")
        game_over.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        game_over.setDefaultButton(QMessageBox.Yes)

        new_game_button = game_over.button(QMessageBox.Yes)
        new_game_button.setText("Новая игра")

        main_menu_button = game_over.button(QMessageBox.No)
        main_menu_button.setText("Главное меню")

        reply = game_over.exec()

        if reply == QMessageBox.Yes:
            self.start_game()
        elif reply == QMessageBox.No:
            self.menu()

    def pause_esc(self):
        escape = QMessageBox()
        escape.setWindowTitle("Игра приостановлена")
        escape.setText("Выберите дальнейшее действие")
        escape.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Reset)

        new_button = escape.button(QMessageBox.Yes)
        new_button.setText("Новая игра")

        main_button = escape.button(QMessageBox.No)
        main_button.setText("Главное меню")

        resume_button = escape.button(QMessageBox.Reset)
        resume_button.setText("Продолжить")

        escape.exec()

        clicked_button = escape.clickedButton()

        if clicked_button == new_button:
            self.start_game()
        elif clicked_button == main_button:
            self.menu()
        elif clicked_button == resume_button:
            self.tboard.resume()

    def menu(self):
        self.tboard.close()
        self.close()  # Закрыть окно игры
        self.main_window.show()  # Показать главное меню
        self.end_game(self.tboard.numLinesRemoved)

    def start_game(self):
        self.tboard.close()
        self.close()
        self.tetris = Tetris2()
        self.tetris.show()

    def resizeEvent(self, event):
        self.center()
        return super().resizeEvent(event)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class RecordsWindow(QtWidgets.QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.initUI()

    def initUI(self):
        self.setObjectName("MainWindow")
        self.resize(360, 760)
        self.setStyleSheet("background-color: rgb(245,255,250);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 1, 0, 1, 1)

        self.btn_record = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(10)
        self.btn_record.setFont(font)
        self.btn_record.setStyleSheet("\nbackground-color: rgb(220, 220, 220);")
        self.btn_record.setObjectName("pushButton2")
        self.btn_record.clicked.connect(self.load_records)
        self.gridLayout.addWidget(self.btn_record, 2, 0, 1, 1)

        self.btn_menu2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(10)
        self.btn_menu2.setFont(font)
        self.btn_menu2.setStyleSheet("\nbackground-color: rgb(220, 220, 220);")
        self.btn_menu2.setObjectName("pushButton")
        self.btn_menu2.clicked.connect(self.menu)
        self.gridLayout.addWidget(self.btn_menu2, 3, 0, 1, 1)

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)


    def load_records(self):
        if os.path.exists("records.txt"):
            with open("records.txt", "r") as file:
                records = file.read()

            font = QtGui.QFont()
            font.setFamily("Comfortaa")
            font.setPointSize(12)
            self.plainTextEdit.setFont(font)

            option = QtGui.QTextOption(QtCore.Qt.AlignTop)  # Исправленная строка
            self.plainTextEdit.document().setDefaultTextOption(option)

            self.plainTextEdit.setPlainText(records)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Records"))
        self.label.setText(_translate("MainWindow", "Рекорды"))
        self.btn_menu2.setText(_translate("MainWindow", "Главное меню"))
        self.btn_menu2.setObjectName("btn_menu2")
        self.btn_record.setText(_translate("MainWindow", "Показать рекорды"))
        self.btn_record.setObjectName("btn_record")


    def menu(self):
        self.close()  # Закрыть окно рекордов
        self.main_window.show()  # Показать главное меню

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())