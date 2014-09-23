#/usr/bin/python
# -*- coding: utf-8 -*-
'''
Author: Mike Clarke 13/09/14
'''

import sys
from PyQt4 import QtGui

class Window(QtGui.QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('PyxEdit')
        #self.setWindowIcon(QtGui.QIcon(TODO))
        self.show()
def main():
    app = QtGui.QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()