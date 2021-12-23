from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from mTT import Worker, MissingDataException, EmailFormatException, PhoneNumberException
import re

class Ui_MainWindow(object):
    myWorkerList = []

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(391, 509)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 71, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 81, 31))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 90, 91, 31))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 130, 161, 31))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 170, 71, 31))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 240, 131, 31))
        self.list_person = QListWidget(self.centralwidget)
        self.list_person.setObjectName(u"list_person")
        self.list_person.setGeometry(QRect(10, 270, 361, 192))
        self.btn_add = QPushButton(self.centralwidget)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setGeometry(QRect(10, 210, 75, 23))
        self.btn_edit = QPushButton(self.centralwidget)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setGeometry(QRect(100, 210, 75, 23))
        self.btn_modify = QPushButton(self.centralwidget)
        self.btn_modify.setObjectName(u"btn_modify")
        self.btn_modify.setGeometry(QRect(190, 210, 75, 23))
        self.btn_delete = QPushButton(self.centralwidget)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setGeometry(QRect(290, 210, 75, 23))
        self.in_name = QLineEdit(self.centralwidget)
        self.in_name.setObjectName(u"in_name")
        self.in_name.setGeometry(QRect(100, 20, 261, 20))
        self.in_id = QLineEdit(self.centralwidget)
        self.in_id.setObjectName(u"in_id")
        self.in_id.setGeometry(QRect(110, 60, 251, 20))
        self.in_address = QLineEdit(self.centralwidget)
        self.in_address.setObjectName(u"in_address")
        self.in_address.setGeometry(QRect(110, 100, 251, 20))
        self.in_phon_number = QLineEdit(self.centralwidget)
        self.in_phon_number.setObjectName(u"in_phon_number")
        self.in_phon_number.setGeometry(QRect(180, 140, 181, 20))
        self.in_email = QLineEdit(self.centralwidget)
        self.in_email.setObjectName(u"in_email")
        self.in_email.setGeometry(QRect(90, 180, 271, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 391, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.btn_add.clicked.connect(self.addButtonClicked)
        self.btn_edit.clicked.connect(self.editButtonClicked)
        self.btn_modify.clicked.connect(self.addButtonClicked)
        self.btn_delete.clicked.connect(self.deleteButtonClicked)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Name:</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">ID code:</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Address:</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Phone number:</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Email:</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">List of persons</span><span style=\" font-size:14pt; font-weight:600;\">:</span></p></body></html>", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.btn_edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.btn_modify.setText(QCoreApplication.translate("MainWindow", u"Modify", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.in_name.setPlaceholderText("")
        self.in_phon_number.setPlaceholderText(QCoreApplication.translate("MainWindow", u"+36301234567", None))
        self.in_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"joeblack@mailbox.com", None))
        self.in_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Joe Black", None))
        self.in_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"123456", None))
        self.in_address.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Heaven Street 13", None))




        self.reloadData()

    def clearInputs(self):
        self.in_name.setText('')
        self.in_id.setText('')
        self.in_address.setText('')
        self.in_phon_number.setText('')
        self.in_email.setText('')

    def addButtonClicked(self):
        try:
            name = self.in_name.text()
            id = self.in_id.text()
            address = self.in_address.text()
            phone_number = self.in_phon_number.text()
            email = self.in_email.text()

            if not name:
                raise MissingDataException('name')
            if not id:
                raise MissingDataException('id')
            if not address:
                raise MissingDataException('address')
            if not phone_number:
                raise MissingDataException('phone_number')
            if not email:
                raise MissingDataException('email')

            # ha nem jo a telefonszam formatum
            # raise PhoneNumberFormatException
            if not re.match('\+\d{11}', phone_number):
                raise PhoneNumberException
            # telefonszam = "+36123456789"
            # re.match('3+', telefonszam)

            if not re.match('[a-z.]+@[a-z]+.\w{2,3}', email):
                raise EmailFormatException
            # ha nem jo az email formatum
            # raise EmailFormatException

        except MissingDataException as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setWindowTitle("Error")
            msg.setText(e.__str__())
            msg.exec()

        except EmailFormatException:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Nem jo formatumban van megadva az email.")
            msg.exec()

        except PhoneNumberException:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Nem jo formatumban van megadva a telefonszam.")
            msg.exec()

        else:
            if not self.in_id.isReadOnly(): # Megnézem, hogy ez az edit mód után van e. Vagyis megnézem, hogy ugye nem
                worker = Worker(name, id, address, phone_number, email)

                if worker not in self.myWorkerList:
                    self.myWorkerList.append(worker)
                    self.list_person.addItem(worker.__str__())
                    self.saveData()
                else:
                    msg = QMessageBox()
                    msg.setText("Mar van ilyen elem a listaban.")
                    msg.setWindowTitle("Warning!")
                    msg.setIcon(QMessageBox.Icon.Critical)
                    msg.exec()
            else: # Ez a kód fut le, ha modify-t nyom a user
                for worker in self.myWorkerList:
                    if worker.id == id:
                        worker.name = name
                        worker.address = address
                        worker.phone_number = phone_number
                        worker.email = email


                self.list_person.clear()
                self.saveData()

                for worker in self.myWorkerList:
                    self.list_person.addItem(worker.__str__())
            self.clearInputs()


    def editButtonClicked(self):
        worker = self.list_person.currentItem()

        if not worker:
            msg = QMessageBox()
            msg.setText("Nincs kivalasztva elem.")
            msg.setWindowTitle("Warning!")
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.exec()
        else:
            worker = worker.text()
            worker_li = worker.split(',')
            self.in_name.setText(worker_li[0])
            self.in_id.setText(worker_li[1])
            self.in_address.setText(worker_li[2])
            self.in_phon_number.setText(worker_li[3])
            self.in_email.setText(worker_li[4])

            self.in_id.setReadOnly(True)

    def deleteButtonClicked(self):
        worker = self.list_person.currentItem()

        if not worker:
            msg = QMessageBox()
            msg.setText("Nincs kivalasztva elem.")
            msg.setWindowTitle("Warning!")
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.exec()
        else:
            for w in self.myWorkerList:
                if w.id == worker.text().split(',')[1]:
                    self.myWorkerList.remove(w)

            self.list_person.clear()
            self.saveData()
            for w in self.myWorkerList:
                self.list_person.addItem(w.__str__())

    def saveData(self):
        f = open("db.txt", "w")
        for worker in self.myWorkerList:
            print(worker.__str__(), file=f)
        f.close()

    def reloadData(self):
        f = open("db.txt", "r")
        for line in f:
            tmp = line.rstrip().split(',')

            worker = Worker(tmp[0], tmp[1], tmp[2], tmp[3], tmp[4])

            self.myWorkerList.append(worker)

        for worker in self.myWorkerList:
            self.list_person.addItem(worker.__str__())


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())