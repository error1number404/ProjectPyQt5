# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from ResultOfGame import Ui_ResultOfGameForm
from InstructionForm import Ui_InstructionForm
from StatisticForm import Ui_StatisticForm
from SelectPlayerForm import Ui_SelectPlayerForm
import random
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(680, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CurrentPlayer_LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.CurrentPlayer_LineEdit.setGeometry(QtCore.QRect(10, 20, 180, 20))
        self.CurrentPlayer_LineEdit.setObjectName("CurrentPlayer_LineEdit")
        self.CurrentPlayer_Label = QtWidgets.QLabel(self.centralwidget)
        self.CurrentPlayer_Label.setGeometry(QtCore.QRect(10, 0, 180, 16))
        self.CurrentPlayer_Label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CurrentPlayer_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentPlayer_Label.setObjectName("CurrentPlayer_Label")
        self.SelectCurrentPlayer_PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.SelectCurrentPlayer_PushButton.setGeometry(QtCore.QRect(10, 50, 180, 25))
        self.SelectCurrentPlayer_PushButton.setObjectName("SelectCurrentPlayer_PushButton")
        self.GetStatistic_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.GetStatistic_pushButton.setGeometry(QtCore.QRect(10, 80, 180, 25))
        self.GetStatistic_pushButton.setObjectName("GetStatistic_pushButton")
        self.GetInstruction_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.GetInstruction_pushButton.setGeometry(QtCore.QRect(10, 110, 180, 25))
        self.GetInstruction_pushButton.setObjectName("GetInstruction_pushButton")
        self.LeadersBoard_tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.LeadersBoard_tableWidget.setGeometry(QtCore.QRect(10, 190, 180, 360))
        self.LeadersBoard_tableWidget.setObjectName("LeadersBoard_tableWidget")
        self.LeadersBoard_tableWidget.setColumnCount(0)
        self.LeadersBoard_tableWidget.setRowCount(0)
        self.LeadersBoard_Label = QtWidgets.QLabel(self.centralwidget)
        self.LeadersBoard_Label.setGeometry(QtCore.QRect(10, 170, 180, 16))
        self.LeadersBoard_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.LeadersBoard_Label.setObjectName("LeadersBoard_Label")
        self.CurrentScore_LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.CurrentScore_LineEdit.setGeometry(QtCore.QRect(220, 20, 80, 20))
        self.CurrentScore_LineEdit.setObjectName("CurrentScore_LineEdit")
        self.BestScore_LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.BestScore_LineEdit.setGeometry(QtCore.QRect(590, 20, 80, 20))
        self.BestScore_LineEdit.setObjectName("BestScore_LineEdit")
        self.CurrentScore_Label = QtWidgets.QLabel(self.centralwidget)
        self.CurrentScore_Label.setGeometry(QtCore.QRect(220, 0, 80, 16))
        self.CurrentScore_Label.setObjectName("CurrentScore_Label")
        self.BestScore_Label = QtWidgets.QLabel(self.centralwidget)
        self.BestScore_Label.setGeometry(QtCore.QRect(590, 0, 80, 16))
        self.BestScore_Label.setObjectName("BestScore_Label")
        self.BackgroundForField_Label = QtWidgets.QLabel(self.centralwidget)
        self.BackgroundForField_Label.setGeometry(QtCore.QRect(220, 100, 450, 450))
        self.BackgroundForField_Label.setText("")
        self.BackgroundForField_Label.setObjectName("BackgroundForField_Label")
        self.StartNewGame_PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartNewGame_PushButton.setGeometry(QtCore.QRect(220, 60, 120, 25))
        self.StartNewGame_PushButton.setObjectName("StartNewGame_PushButton")
        self.SaveGame_PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveGame_PushButton.setGeometry(QtCore.QRect(385, 60, 120, 25))
        self.SaveGame_PushButton.setObjectName("SaveGame_PushButton")
        self.LoadGame_PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.LoadGame_PushButton.setGeometry(QtCore.QRect(550, 60, 120, 25))
        self.LoadGame_PushButton.setObjectName("LoadGame_PushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 680, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.DataBaseName = 'databases/Players_db.sqlite'
        self.CurrentPlayer_LineEdit.setReadOnly(True)
        self.CurrentScore_LineEdit.setReadOnly(True)
        self.BestScore_LineEdit.setReadOnly(True)
        self.BackgroundForField_Label.setPixmap(QPixmap("images/background.jpg"))
        self.StartNewGame_PushButton.clicked.connect(self.create_new_field)
        self.GetInstruction_pushButton.clicked.connect(self.get_instruction)
        self.GetStatistic_pushButton.clicked.connect(self.get_statistic)
        self.SelectCurrentPlayer_PushButton.clicked.connect(self.selectcurrentplayer)
        self.SaveGame_PushButton.clicked.connect(self.do_save)
        self.LoadGame_PushButton.clicked.connect(self.load_save)
        self.field = []
        self.ButtonsField = []
        self.currentPlayer = None
        self.blocked = False
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        for x_pos in range(4):
            self.ButtonsField.append([])
            for y_pos in range(4):
                self.ButtonsField[x_pos].append(QtWidgets.QPushButton(self.centralwidget))
                self.ButtonsField[x_pos][y_pos].setGeometry(QtCore.QRect(250 + x_pos * 100,
                                                                  130 + y_pos * 100,
                                                                  90, 90))
                self.ButtonsField[x_pos][y_pos].setEnabled(False)
                self.ButtonsField[x_pos][y_pos].setFont(font)
                self.ButtonsField[x_pos][y_pos].hide()
        self.load_leaders_board()
        self.load_mp3('sounds/swipe.mp3')

    def selectcurrentplayer(self):
        self.selectCurrentPlayer = Ui_SelectPlayerForm(self)

    def get_instruction(self):
        self.instruction = Ui_InstructionForm(self)

    def get_statistic(self):
        con = sqlite3.connect(self.DataBaseName)
        cur = con.cursor()
        if self.currentPlayer is None:
            message = QtWidgets.QMessageBox.warning(self, 'Внимание!', "Выберите пользователя")
        elif cur.execute('select all_results from players where id = ?', (self.currentPlayer,)).fetchone()[0] == '':
            message = QtWidgets.QMessageBox.warning(self, 'Внимание!', "Вы не сыграли ни одной игры")
        elif len(cur.execute('select all_results from players where id = ?',(self.currentPlayer,)).fetchone()[0].split(' ')) < 2:
            message = QtWidgets.QMessageBox.warning(self, 'Внимание!', "Вы сыграли лишь одну игру")
        else:
            self.statistic = Ui_StatisticForm(self)
        con.close()

    def create_new_field(self):
        if self.currentPlayer is None:
            message = QtWidgets.QMessageBox.warning(self, 'Внимание!', "Выберите пользователя")
        else:
            self.blocked = False
            self.field = [[0, 0, 0, 0] for i in range(4)]
            self.count_score()
            self.add_new_plate()
            self.setFocusPolicy(QtCore.Qt.StrongFocus)

    def add_new_plate(self):
        x_pos = random.randint(0, 3)
        y_pos = random.randint(0, 3)
        while self.field[x_pos][y_pos] != 0:
            x_pos = random.randint(0, 3)
            y_pos = random.randint(0, 3)
        self.field[x_pos][y_pos] = random.choice([2, 2, 2, 4])
        self.show_field()

    def show_field(self):
        for x_pos in range(4):
            for y_pos in range(4):
                if self.field[x_pos][y_pos] == 0:
                    self.ButtonsField[x_pos][y_pos].hide()
                    self.ButtonsField[x_pos][y_pos].setText('')
                else:
                    self.ButtonsField[x_pos][y_pos].show()
                    self.ButtonsField[x_pos][y_pos].setText(str(self.field[x_pos][y_pos]))

    def count_score(self):
        self.CurrentScore_LineEdit.setText(str(sum([sum(self.field[i]) for i in range(4)])))

    def do_save(self):
        if self.field == []:
            message = QtWidgets.QMessageBox.warning(self, 'Внимание!', "Игра не начата!")
        else:
            name, ok_pressed = QtWidgets.QInputDialog.getText(self, "Сохранить",
                                                    "Введите название для сохранения")
            if ok_pressed:
                file = open('saves/' + name + '.txt','w+')
                str_for_save = ' '.join([' '.join(list(map(lambda x: str(x), self.field[i]))) for i in range(4)])
                file.write(str_for_save)
                file.close()

    def load_save(self):
        if self.currentPlayer is None:
            message = QtWidgets.QMessageBox.warning(self, 'Внимание!', "Выберите пользователя")
        else:
            filename = QtWidgets.QFileDialog.getOpenFileName(
                self, 'Выбрать сохранение', 'saves/',
                'Сохранение(*.txt)')[0]
            if filename != '':
                file = open(filename,'r')
                save = file.readlines()[0].split(' ')
                save = list(map(lambda x: int(x),save))
                save = [[save[4 * i + j] for j in range(4)]for i in range(4)]
                self.field = save
                self.show_field()
                self.count_score()

    def save_result(self):
        con = sqlite3.connect(self.DataBaseName)
        cur = con.cursor()
        best_result = cur.execute('select best_result from players where id = ?', (self.currentPlayer, )).fetchone()[0]
        if cur.execute('select all_results from players where id = ?', (self.currentPlayer,)).fetchone()[0] == '':
            all_results = cur.execute('select all_results from players where id = ?', (self.currentPlayer,)).fetchone()[
                              0] + self.CurrentScore_LineEdit.text()
        else:
            all_results = cur.execute('select all_results from players where id = ?', (self.currentPlayer, )).fetchone()[0] + ' ' + self.CurrentScore_LineEdit.text()
        cur.execute('UPDATE players set all_results = ? where id = ?', (all_results,self.currentPlayer))
        if best_result < int(self.CurrentScore_LineEdit.text()):
            cur.execute('UPDATE players set best_result = ? where id = ?', (int(self.CurrentScore_LineEdit.text()), self.currentPlayer))
        con.commit()
        con.close()
        self.load_leaders_board()

    def is_win(self):
        self.count_score()
        for x_pos in range(4):
            for y_pos in range(4):
                if self.field[x_pos][y_pos] == 2048:
                    return True
        for x_pos in range(4):
            for y_pos in range(4):
                if self.field[x_pos][y_pos] == 0:
                    return None
        for x_pos in range(3):
            for y_pos in range(3):
                if self.field[x_pos][y_pos] == self.field[x_pos + 1][y_pos] or self.field[x_pos][y_pos] == self.field[x_pos][y_pos + 1]:
                    return None
        for y_pos in range(3):
            if self.field[3][y_pos] == self.field[3][y_pos + 1]:
                return None
        for x_pos in range(3):
            if self.field[x_pos][3] == self.field[x_pos + 1][3]:
                return None
        return False

    def compress(self):
        changed = False
        new_field = [[0, 0, 0, 0] for i in range(4)]
        for x_pos in range(4):
            pos = 0
            for y_pos in range(4):
                if self.field[x_pos][y_pos] != 0:
                    new_field[x_pos][pos] = self.field[x_pos][y_pos]
                    if y_pos != pos:
                        changed = True
                    pos += 1
        return new_field, changed

    def merge(self):
        changed = False
        for x_pos in range(4):
            for y_pos in range(3):
                if self.field[x_pos][y_pos] == self.field[x_pos][y_pos + 1] and self.field[x_pos][y_pos] != 0:
                    self.field[x_pos][y_pos] = self.field[x_pos][y_pos] * 2
                    self.field[x_pos][y_pos + 1] = 0
                    changed = True
        return changed

    def reverse(self):
        new_field = []
        for x_pos in range(4):
            new_field.append([])
            for y_pos in range(4):
                new_field[x_pos].append(self.field[x_pos][3 - y_pos])
        return new_field

    def transpose(self):
        new_field = []
        for x_pos in range(4):
            new_field.append([])
            for y_pos in range(4):
                new_field[x_pos].append(self.field[y_pos][x_pos])
        return new_field

    def move_up(self):
        self.field, changed1 = self.compress()
        changed2 = self.merge()
        self.changed = changed1 or changed2
        self.field, temp = self.compress()

    def move_down(self):
        self.field = self.reverse()
        self.move_up()
        self.field = self.reverse()

    def move_left(self):
        self.field = self.transpose()
        self.move_up()
        self.field = self.transpose()

    def move_right(self):
        self.field = self.transpose()
        self.move_down()
        self.field = self.transpose()

    def keyPressEvent(self, event):
        if self.field == []:
            pass
        elif self.blocked:
            pass
        elif event.key() == Qt.Key_Left:
            self.move_left()
            if self.is_win() is None and self.changed:
                self.player.play()
                self.add_new_plate()
            elif self.is_win() is None and self.changed is False:
                pass
            else:
                self.blocked = True
                self.show_field()
                self.save_result()
                result = Ui_ResultOfGameForm(self)
        elif event.key() == Qt.Key_Right:
            self.move_right()
            if self.is_win() is None and self.changed:
                self.player.play()
                self.add_new_plate()
            elif self.is_win() is None and self.changed is False:
                pass
            else:
                self.show_field()
                self.blocked = True
                self.save_result()
                result = Ui_ResultOfGameForm(self)
        elif event.key() == Qt.Key_Down:
            self.move_down()
            if self.is_win() is None and self.changed:
                self.player.play()
                self.add_new_plate()
            elif self.is_win() is None and self.changed is False:
                pass
            else:
                self.blocked = True
                self.show_field()
                self.save_result()
                result = Ui_ResultOfGameForm(self)
        elif event.key() == Qt.Key_Up:
            self.move_up()
            if self.is_win() is None and self.changed:
                self.player.play()
                self.add_new_plate()
            elif self.is_win() is None and self.changed is False:
                pass
            else:
                self.blocked = True
                self.show_field()
                self.save_result()
                result = Ui_ResultOfGameForm(self)

    def load_mp3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)

    def load_leaders_board(self):
        con = sqlite3.connect(self.DataBaseName)
        cur = con.cursor()
        ListOfMaxResults = cur.execute('select name,best_result from players where best_result > 0').fetchall()
        ListOfMaxResults = list(map(lambda x: [x[0], int(x[1])], ListOfMaxResults))
        ListOfMaxResults = sorted(ListOfMaxResults, key=lambda x: x[1],reverse=True)
        try:
            self.LeadersBoard_tableWidget.setRowCount(len(ListOfMaxResults))
            self.LeadersBoard_tableWidget.setColumnCount(len(ListOfMaxResults[0]))
            self.LeadersBoard_tableWidget.setHorizontalHeaderLabels(['Имя', 'Результат'])
            for i, elem in enumerate(ListOfMaxResults):
                for j, val in enumerate(elem):
                    self.LeadersBoard_tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(val)))
                    self.LeadersBoard_tableWidget.item(i,j).setFlags(QtCore.Qt.ItemIsEnabled)
            self.LeadersBoard_tableWidget.setColumnWidth(0, self.LeadersBoard_tableWidget.width() / 2.1)
            self.LeadersBoard_tableWidget.setColumnWidth(1, self.LeadersBoard_tableWidget.width() / 2.1)
        except BaseException:
            pass
        con.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Игра \"2048\""))
        self.CurrentPlayer_LineEdit.setText(_translate("MainWindow", "Выберите пользователя"))
        self.CurrentPlayer_Label.setText(_translate("MainWindow", "Имя текущего пользователя"))
        self.SelectCurrentPlayer_PushButton.setText(_translate("MainWindow", "Выбрать пользователя"))
        self.GetStatistic_pushButton.setText(_translate("MainWindow", "Статистика"))
        self.GetInstruction_pushButton.setText(_translate("MainWindow", "Инструкция"))
        self.LeadersBoard_Label.setText(_translate("MainWindow", "Таблица лидеров"))
        self.CurrentScore_LineEdit.setText(_translate("MainWindow", "0"))
        self.BestScore_LineEdit.setText(_translate("MainWindow", "0"))
        self.CurrentScore_Label.setText(_translate("MainWindow", "Текущий счет:"))
        self.BestScore_Label.setText(_translate("MainWindow", "Лучший счет:"))
        self.StartNewGame_PushButton.setText(_translate("MainWindow", "Начать новую игру"))
        self.SaveGame_PushButton.setText(_translate("MainWindow", "Сохранить игру"))
        self.LoadGame_PushButton.setText(_translate("MainWindow", "Загрузить игру"))