from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Multiplier(object):
    def setupUi(self, Multiplier):
        Multiplier.setObjectName("Multiplier")
        Multiplier.resize(600, 206)
        self.centralwidget = QtWidgets.QWidget(Multiplier)
        self.centralwidget.setObjectName("centralwidget")
        self.p_label = QtWidgets.QLabel(self.centralwidget)
        self.p_label.setGeometry(QtCore.QRect(20, 10, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.p_label.setFont(font)
        self.p_label.setObjectName("p_label")
        self.radix = QtWidgets.QComboBox(self.centralwidget)
        self.radix.setGeometry(QtCore.QRect(60, 10, 69, 22))
        self.radix.setObjectName("radix")
        self.radix.setFont(font)
        self.radix.addItems(["2", "3", "5", "7"])
        self.mnog1_label = QtWidgets.QLabel(self.centralwidget)
        self.mnog1_label.setGeometry(QtCore.QRect(20, 40, 101, 21))
        self.mnog1_label.setFont(font)
        self.mnog1_label.setObjectName("mnog1_label")
        self.mnog2_label = QtWidgets.QLabel(self.centralwidget)
        self.mnog2_label.setGeometry(QtCore.QRect(20, 70, 101, 21))
        self.mnog2_label.setFont(font)
        self.mnog2_label.setObjectName("mnog2_label")
        self.dobutok_label = QtWidgets.QLabel(self.centralwidget)
        self.dobutok_label.setGeometry(QtCore.QRect(20, 100, 101, 21))
        self.dobutok_label.setFont(font)
        self.dobutok_label.setObjectName("dobutok_label")
        self.mnog1_input = QtWidgets.QLineEdit(self.centralwidget)
        self.mnog1_input.setGeometry(QtCore.QRect(130, 40, 271, 21))
        self.mnog1_input.setFont(font)
        self.mnog1_input.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.mnog1_input.setObjectName("mnog1_input")
        self.mnog2_input = QtWidgets.QLineEdit(self.centralwidget)
        self.mnog2_input.setGeometry(QtCore.QRect(130, 70, 271, 21))
        self.mnog2_input.setFont(font)
        self.mnog2_input.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.mnog2_input.setObjectName("mnog2_input")
        self.dobutok_input = QtWidgets.QLineEdit(self.centralwidget)
        self.dobutok_input.setGeometry(QtCore.QRect(130, 100, 400, 21))
        self.dobutok_input.setFont(font)
        self.dobutok_input.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.dobutok_input.setObjectName("dobutok_input")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 140, 131, 31))
        self.pushButton.clicked.connect(self.calculate)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        Multiplier.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Multiplier)
        self.statusbar.setObjectName("statusbar")
        Multiplier.setStatusBar(self.statusbar)

        self.retranslateUi(Multiplier)
        QtCore.QMetaObject.connectSlotsByName(Multiplier)

    def calculate(self):
        # Convert FROM string TO int
        m1 = int(self.mnog1_input.text(), int(self.radix.currentText()))
        m2 = self.mnog2_input.text()[::-1]
        res = []
        for i in range(len(self.mnog2_input.text())):
            if int(m2[i], int(self.radix.currentText())) != 0:
                res.append(m1 * 2**i)
        x = 0
        for i in res:
            x ^= i
        print(type(x), x)
        if self.radix.currentText() == "2":
            self.dobutok_input.setText(bin(x)[2:])
        else:
            rad = self.radix.currentText()
            self.dobutok_input.setText(self.dec_to_base(x, int(rad)))

    def dec_to_base(self, num,base):  #Maximum base - 36
        base_num = ""
        print(base)
        while num>0:
            dig = int(num%base)
            if dig<10:
                base_num += str(dig)
            else:
                base_num += chr(ord('A')+dig-10)  #Using uppercase letters
            num //= base
        base_num = base_num[::-1]  #To reverse the string
        return base_num

    def retranslateUi(self, Multiplier):
        _translate = QtCore.QCoreApplication.translate
        Multiplier.setWindowTitle(_translate("Multiplier", "Multiplier"))
        self.p_label.setText(_translate("Multiplier", "P:"))
        self.mnog1_label.setText(_translate("Multiplier", "Множник-1:"))
        self.mnog2_label.setText(_translate("Multiplier", "Множник-2:"))
        self.dobutok_label.setText(_translate("Multiplier", "Добуток:"))
        self.pushButton.setText(_translate("Multiplier", "Розрахувати"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Multiplier = QtWidgets.QMainWindow()
    ui = Ui_Multiplier()
    ui.setupUi(Multiplier)
    Multiplier.show()
    sys.exit(app.exec_())
