# import QtGui hadha ya3tik l'interaction m3a components ta3 widget kima icon ..etc
from PyQt5 import QtGui,QtWidgets
# hadha kima MainWindow type ta3 widget
# QApplication ta7etjha mbe3d ki dji t9oul le system bli hadhi rah Qapp
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton,\
                            QLabel, QLineEdit, QGridLayout, QVBoxLayout, QGroupBox, \
                            QFileDialog, QTextEdit
import sys
import smtplib
import ssl
import pandas as pd
# create class ydir inherite man mainwindow bah ydi kaml les (objects, functions man mainwindow)
class Window(QDialog):
    def __init__(self):
        # overide the init function from QMainWinodw class
        super().__init__()
        self.title = "Inptic Email System"
        self.top = 200
        self.left = 500
        self.width = 500
        self.height = 300
        self.show()

    def show(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon("csi.jpg"))
        # components functions
        self.components()
        qv = QVBoxLayout()
        qv.addWidget(self.groupebox)
        self.setLayout(qv)

        super().show()

    def components(self):
        # create widget components (buttons .. etc)
        self.email_label = QLabel("Email: ")
        self.email_linedit = QLineEdit()
        self.pass_label = QLabel("Password: ")
        self.pass_linedit = QLineEdit()
        self.emailtitle_label = QLabel("Subject : ")
        self.emailtitle_linedit = QLineEdit()
        self.emailtext_label = QLabel("Email_text: ")
        self.emailtext_linedit = QTextEdit()
        self.groupebox = QGroupBox('INPTIC EMAIL SYSTEM')
        self.button_send = QPushButton('Send Email')
        self.button_exel = QPushButton('Exel file')
        self.file_label = QLabel("choose file")


        # add components to widget
        Grid = QGridLayout()
        Grid.addWidget(self.email_label, 0, 0)
        Grid.addWidget(self.email_linedit, 0, 1)
        Grid.addWidget(self.pass_label, 1, 0)
        Grid.addWidget(self.pass_linedit, 1, 1)
        Grid.addWidget(self.emailtitle_label, 2, 0)
        Grid.addWidget(self.emailtitle_linedit, 2, 1)
        Grid.addWidget(self.emailtext_label, 3, 0)
        Grid.addWidget(self.emailtext_linedit, 3, 1)
        Grid.addWidget(self.button_exel, 4, 1)
        Grid.addWidget(self.file_label, 5, 1)
        Grid.addWidget(self.button_send, 6, 1)
        self.groupebox.setLayout(Grid)

        # set functions to buttons
        # first button connect to send_email function
        self.button_send.clicked.connect(self.send_email)
        # second function used to brorwse to exel file
        self.button_exel.clicked.connect(self.openfunction)

    def openfunction(self):
        file = QFileDialog
        # set file path to file_label
        self.file_label.setText(file.getOpenFileName(self, 'Open File', "File", "Exel Files (*.xlsx *.xla *.xlam *.xls *.xlsb *.xlsm *.xlt *.xltm)")[0])
    def send_email(self):
        #get the inputs from line_edits in form and set it in variables
        user_email=self.email_linedit.text()
        user_password=self.pass_linedit.text()
        email_subject=self.emailtitle_linedit.text()
        subject="Subject: {} ".format(email_subject)+"\n"
        emai_text=subject+self.emailtext_linedit.toPlainText()
        path=self.file_label.text()

        try:
            context = ssl.create_default_context()
            #to connect to smtp server (email_send protocole) taleb xd:)
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                #connect with personnal email & password
                server.login(str(user_email),str(user_password))
                #open and read file with pandas
                pf = pd.read_excel(str(path))
                #get column name and email from exel and set it like list
                names = pf['Nom et prénom'].tolist()
                emails = pf['Adresse e-mail'].tolist()
                for i in range(len(names)):
                    #send email one by one and set special name in wish email with Format function
                    server.sendmail(
                        user_email,
                        emails[i],
                        emai_text.format(name=names[i]).encode('utf-8')
                    )

            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Question)
            msg.setText("Emails Sent")
            msg.setWindowTitle("Successful")
            msg.exec_()
            print('email sent')
        except:
            print('emails not sent')
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Email not Sent")
            msg.setInformativeText('Check informations')
            msg.setWindowTitle("Faild")
            msg.exec_()








App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
