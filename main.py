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
        self.start_button.clicked.connect(self.organizer)

    def open_path(self):
        self.file = QFileDialog.getExistingDirectory(self, str("pasta xml"),
                                                     '/home',
                                                     QFileDialog.ShowDirsOnly | 
                                                     QFileDialog.DontResolveSymlinks)
        self.txt_path.setText(self.file)
        self.file = str(self.file)
        
    def organizer(self):
        
        path = self.file
        files = os.listdir(path)
        
        for file in files:
            filename, extension = os.path.splitext(file)
            extension = extension[1:]
            if file == filename + '':
                pass
            if os.path.exists(path + '/'):
                pass
            if os.path.exists(path + '/' + extension):
                shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
            else:
                os.makedirs(path +  '/' + extension)
                shutil.move(path + '/' + file, path + '/' + extension)
                
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText('Arquivos Organizados!')
        msg.exec_()
                
    
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    