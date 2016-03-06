#!/usr/bin/python

#QT Version

from PyQt4 import QtGui, QtCore
import subprocess, time, sys, os
from fontlib import fontlib


class main_window(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.backup, self.unzip = 1, 1

        now = time.localtime()
        self.date = str(now[0])+str(now[1])+str(now[2])+"_"+str(now[3])+str(now[4])
        self.notify_window = notify_dialog()

        self.resize(1750, 850)
        self.move(0, 0)
        self.setStyleSheet("background-color: black;")




class notify_dialog(QtGui.QWidget):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setFixedSize(800, 480)
        self.move(0, 0)
        self.background = QtGui.QLabel(self)
        self.setStyleSheet("background-color: rgba(0,0,0,200);")
        self.fontlib = fontlib()

        self.alert_ok_button = QtGui.QLabel(" OK ", self)
        self.alert_ok_button.setStyleSheet(self.fontlib.alert_ok)
        self.alert_ok_button.move(340, 350)
        self.alert_ok_button.setAlignment(QtCore.Qt.AlignVCenter)
        self.alert_ok_button.setFixedSize(120, 60)
        self.alert_ok_button.mousePressEvent = self.alert_close

        self.alert_text = QtGui.QLabel("", self)
        self.alert_text.setFixedSize(760,200)
        self.alert_text.setStyleSheet(self.fontlib.alert_text)
        self.alert_text.move(20, 100)

    def alert(self, message):
        lines = []
        for i in xrange(0, len(message), 40):
            lines.append(message[i:i+40])
        self.alert_text.setAlignment(QtCore.Qt.AlignCenter)
        self.alert_text.setText('\n'.join(lines))
        self.show()
        self.raise_()

    def alert_close(self, event):
        self.hide()




QtGui.QApplication.setStyle('Plastique')


app = QtGui.QApplication(sys.argv)

window = main_window()
window.show()


sys.exit(app.exec_())
