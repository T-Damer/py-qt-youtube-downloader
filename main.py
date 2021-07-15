import os
import re
import sys
import youtube_dl
from PyQt5 import QtCore, QtWidgets
from des import *

class downloader(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.url = None

    def run(self):
        self.mysignal.emit("Download process started!")

        with youtube_dl.YoutubeDL({}) as ytdl:
                ytdl.download([self.url])
                # QtWidgets.QMessageBox.warning(self, "Error", "Paste a correct url")

        self.mysignal.emit("Download process finished!")
        self.mysignal.emit("Finish")

    def init_args(self, url):
        self.url = url


class gui(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_YTDownloader()
        self.ui.setupUi(self)

        self.download_folder = None
        self.ui.pushButton.clicked.connect(self.get_folder)
        self.ui.pushButton_2.clicked.connect(self.start)
        self.mythread = downloader()
        self.mythread.mysignal.connect(self.handler)

    def start(self):
        if len(self.ui.lineEdit.text()) > 5:
            if self.download_folder != None:
                link = self.ui.lineEdit.text()
                self.mythread.init_args(link)
                self.mythread.start()
                self.locker(True)
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "You didn't choose a download folder")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "You didn't specified a download link")

        
    def get_folder(self):
        self.download_folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Choose a download folder")
        if (self.download_folder != ''):
            os.chdir(self.download_folder)
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Choose a downloader folder")

    def handler(self, value):
        if value == 'finish':
            self.locker(False)
        else:
            self.ui.plainTextEdit.appendPlainText(value)
    

    def locker(self, lock_value):
        base = [self.ui.pushButton, self.ui.pushButton_2]

        for item in base:
            item.setDisabled(lock_value)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = gui()
    win.show()
    sys.exit(app.exec_())