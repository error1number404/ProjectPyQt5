# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddANewPlayerForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
import sqlite3

class Ui_AddANewPlayerForm(QWidget):
    def __init__(self, parent):
        super(Ui_AddANewPlayerForm, self).__init__(parent)
        self.parent = parent
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.Window)
        self.setupUi(self)
        self.show()

    def setupUi(self, AddANewPlayerForm):
        AddANewPlayerForm.setObjectName("AddANewPlayerForm")
        AddANewPlayerForm.setFixedSize(300, 200)
        self.NameForNewPlayer_LineEdit = QtWidgets.QLineEdit(AddANewPlayerForm)
        self.NameForNewPlayer_LineEdit.setGeometry(QtCore.QRect(60, 50, 180, 20))
        self.NameForNewPlayer_LineEdit.setObjectName("NameForNewPlayer_LineEdit")
        self.AddANewPlayer_PushButton = QtWidgets.QPushButton(AddANewPlayerForm)
        self.AddANewPlayer_PushButton.setGeometry(QtCore.QRect(60, 90, 180, 25))
        self.AddANewPlayer_PushButton.setObjectName("AddANewPlayer_PushButton")
        self.NameForNewPlayer_Label = QtWidgets.QLabel(AddANewPlayerForm)
        self.NameForNewPlayer_Label.setGeometry(QtCore.QRect(60, 30, 180, 16))
        self.NameForNewPlayer_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.NameForNewPlayer_Label.setObjectName("NameForNewPlayer_Label")
        self.Debug_Label = QtWidgets.QLabel(AddANewPlayerForm)
        self.Debug_Label.setGeometry(QtCore.QRect(10, 170, 250, 21))
        self.Debug_Label.setText("")
        self.Debug_Label.setObjectName("Debug_Label")
        self.retranslateUi(AddANewPlayerForm)
        QtCore.QMetaObject.connectSlotsByName(AddANewPlayerForm)
        self.AddANewPlayer_PushButton.clicked.connect(self.add_new_player_to_data_base)

    def add_new_player_to_data_base(self):
        self.Debug_Label.setText('')
        con = sqlite3.connect(self.parent.DataBaseName)
        cur = con.cursor()
        if cur.execute('select * from players where name == ?', (self.NameForNewPlayer_LineEdit.text(),)).fetchall() != []:
            self.Debug_Label.setText('Игрок с таким именем уже существует')
        if self.NameForNewPlayer_LineEdit.text() == '':
            self.Debug_Label.setText('Имя игрока не должно быть пустой строкой')
        else:
            try:
                id = con.execute('select id from players').fetchall()[-1][0] + 1
            except BaseException:
                id = 1
            cur.execute('insert into players(id,name,best_result,all_results) values (?,?,0,"")',
                        (id, self.NameForNewPlayer_LineEdit.text()))
            con.commit()
            con.close()
            self.parent.selectCurrentPlayer.update_table()
            self.parent.setFocusPolicy(QtCore.Qt.StrongFocus)
            self.close()

    def retranslateUi(self, AddANewPlayerForm):
        _translate = QtCore.QCoreApplication.translate
        AddANewPlayerForm.setWindowTitle(_translate("AddANewPlayerForm", "Добавить пользователя"))
        self.AddANewPlayer_PushButton.setText(_translate("AddANewPlayerForm", "Сохранить"))
        self.NameForNewPlayer_Label.setText(_translate("AddANewPlayerForm", "Введите желаемое имя"))