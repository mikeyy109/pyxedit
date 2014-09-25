#/usr/bin/python
# -*- coding: utf-8 -*-
'''
Author: Mike Clarke 13/09/14
'''

import sys
from PyQt4 import QtGui

class Main_Window(QtGui.QMainWindow):

    def __init__(self):
        super(Main_Window, self).__init__()
        self.initUI()

    def initUI(self):
        text_edit = QtGui.QTextEdit()
        self.setCentralWidget(text_edit)

        exit_action = QtGui.QAction(QtGui.QIcon('assets/exit.png'), 'Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(QtGui.qApp.quit)

        self.statusBar().showMessage('...')

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(exit_action)

        #tool_bar = self.addToolBar('Exit')
        #tool_bar.addAction(exit_action)

        self.resize(800, 600)
        self.center()
        self.setWindowTitle('PyxEdit')
        #self.setWindowIcon(QtGui.QIcon())#TODO

        self.show()

    def center(self):
        get_rect = self.frameGeometry()
        center_point = QtGui.QDesktopWidget().availableGeometry().center()
        get_rect.moveCenter(center_point)
        self.move(get_rect.topLeft())

def main():
    app = QtGui.QApplication(sys.argv)
    w = Main_Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()