from pytube import YouTube
from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from tkinter import messagebox
from os import getcwd, mkdir
from os.path import isdir
from tkinter import filedialog
from sys import argv, exit

# region SetVariables
link: str
title: str
path: str = getcwd()
directory_file: str
out_file_type: str = ".mp3"

# endregion

# region functions


# endregion

#region INIT

if not isdir(f"{path}\\audio"):
    mkdir(f"{path}\\audio")

#endregion

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(919, 676)
        Dialog.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, -20, 521, 91))
        font = QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.textEdit = QTextEdit(Dialog)
        self.textEdit.textChanged.connect(self.change_entry1)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(130, 100, 671, 71))
        font1 = QFont()
        font1.setPointSize(24)
        self.textEdit.setFont(font1)
        self.video_title = QLabel(Dialog)
        self.video_title.setObjectName(u"video_title")
        self.video_title.setGeometry(QRect(100, 300, 721, 181))
        font2 = QFont()
        font2.setPointSize(24)
        self.video_title.setFont(font2)
        self.video_title.setAlignment(Qt.AlignCenter)
        self.video_title.setWordWrap(True)
        self.choose_dir = QPushButton(Dialog)
        self.choose_dir.clicked.connect(self.get_out_path)
        self.choose_dir.setObjectName(u"choose_dir")
        self.choose_dir.setGeometry(QRect(110, 250, 40, 40))
        font3 = QFont()
        font3.setPointSize(18)
        self.choose_dir.setFont(font3)
        self.choose_dir.setIconSize(QSize(16, 16))
        self.start_download = QPushButton(Dialog)
        self.start_download.clicked.connect(self.downloading)
        self.start_download.setObjectName(u"start_download")
        self.start_download.setGeometry(QRect(620, 250, 191, 40))
        font4 = QFont()
        font4.setPointSize(16)
        self.start_download.setFont(font4)
        self.path_save = QTextEdit(Dialog)
        self.path_save.setObjectName(u"path_save")
        self.path_save.setGeometry(QRect(150, 250, 471, 40))
        self.path_save.setFont(font4)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Audio Downloader", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter URL", None))
        self.video_title.setText(QCoreApplication.translate("Dialog", u"Video Title", None))
        self.choose_dir.setText(QCoreApplication.translate("Dialog", u"Dir", None)) # \ud83c\udf0d
        self.start_download.setText(QCoreApplication.translate("Dialog", u"Find And Download", None))
        self.path_save.setPlaceholderText(QCoreApplication.translate("Dialog", u"Path to Save", None))
    # retranslateUi

    def change_entry1(self):
        print("Edit Text changed")
        try:
            self.video_title.setText(YouTube(self.textEdit.toPlainText()).title)
        except Exception as err:
            self.video_title.setText("Video Title")
            print(err)

    def get_out_path(self):
        directory_file = filedialog.askdirectory()
        # print(directory_file)
        self.path_save.setText(directory_file)

    def downloading(self):
        print("Downloading")
        try:
            directory_file = self.path_save.toPlainText()
            if directory_file == "":
                directory_file = f"{path}\\audio"
            link = self.textEdit.toPlainText()
            print(link)
            yt = YouTube(link)
            title = yt.title
            self.video_title.setText(title)
            stream = yt.streams.filter(only_audio=True).first()
            stream.download(output_path=directory_file, filename=title + out_file_type)
            messagebox.showinfo(title="Success", message="Downloaded Successfully!")
        except Exception as e:
            print("---- ---- -----  --- - --- - -- - --------  ----- - ---")
            print(e)
            pass


if __name__ == "__main__":
    app = QApplication(argv)
    MainWindow = QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    exit(app.exec())