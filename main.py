import os
import shutil
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from ui_main import Ui_MainWindow
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('File Organizer')
        appIcon = QIcon('./img/sigma.png')
        self.setWindowIcon(appIcon)
        self.file = ''
        self.open_button.clicked.connect(self.open_path)

    def open_path(self):
        self.file = QFileDialog.getExistingDirectory(self, str("pasta xml"),
                                                     '/home',
                                                     QFileDialog.ShowDirsOnly | 
                                                     QFileDialog.DontResolveSymlinks)
        self.txt_path.setText(self.file)
        self.file = str(self.file)
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
    