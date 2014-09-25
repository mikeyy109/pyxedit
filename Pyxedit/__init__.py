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
        self.resize(800, 600)
        self.center()
        self.setWindowTitle('PyxEdit')
        #self.setWindowIcon(QtGui.QIcon(TODO))
        self.statusBar().showMessage('...')
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