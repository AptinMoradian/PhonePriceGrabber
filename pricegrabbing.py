from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from bs4 import BeautifulSoup

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(302, 304)
        self.lineEdit = QtWidgets.QTextEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(52, 50, 181, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 20, 111, 20))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 100, 93, 28))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.find)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(40, 140, 221, 101))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Price Grabber"))
        self.label.setText(_translate("Dialog", "Your Phone name:"))
        self.pushButton.setText(_translate("Dialog", "Find Price"))
    def find(self):
        name = self.lineEdit.toPlainText()
        url = f"https://www.sellcell.com/search/?q={name}"
        req = requests.get(url).text
        doc = BeautifulSoup(req, "html.parser")
        price = doc.find(class_="price")
        if price:
            self.textBrowser.append(str(price.text))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
