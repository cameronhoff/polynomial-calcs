from PyQt5 import QtCore, QtGui, QtWidgets
import re

class Ui_FactorStep(object):
    def setupUi(self, FactorStep):
        FactorStep.setObjectName("FactorStep")
        FactorStep.resize(772, 581)
        font = QtGui.QFont()
        font.setPointSize(9)
        FactorStep.setFont(font)
        self.centralwidget = QtWidgets.QWidget(FactorStep)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 701, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pol_1_lb = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pol_1_lb.setObjectName("pol_1_lb")
        self.gridLayout.addWidget(self.pol_1_lb, 0, 0, 1, 1)
        self.pol_1_in = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.pol_1_in.setObjectName("pol_1_in")
        self.gridLayout.addWidget(self.pol_1_in, 1, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 70, 701, 61))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pol_2_lb = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.pol_2_lb.setObjectName("pol_2_lb")
        self.gridLayout_2.addWidget(self.pol_2_lb, 0, 0, 1, 1)
        self.pol_2_in = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.pol_2_in.setObjectName("pol_2_in")
        self.gridLayout_2.addWidget(self.pol_2_in, 1, 0, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 130, 701, 61))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pol_3_lb = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.pol_3_lb.setObjectName("pol_3_lb")
        self.gridLayout_3.addWidget(self.pol_3_lb, 0, 0, 1, 1)
        self.pol_3_in = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.pol_3_in.setObjectName("pol_3_in")
        self.gridLayout_3.addWidget(self.pol_3_in, 1, 0, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 190, 701, 61))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pol_4_lb = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.pol_4_lb.setObjectName("pol_4_lb")
        self.gridLayout_4.addWidget(self.pol_4_lb, 0, 0, 1, 1)
        self.pol_4_in = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.pol_4_in.setObjectName("pol_4_in")
        self.gridLayout_4.addWidget(self.pol_4_in, 1, 0, 1, 1)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 250, 701, 61))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pol_5_lb = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.pol_5_lb.setObjectName("pol_5_lb")
        self.gridLayout_5.addWidget(self.pol_5_lb, 0, 0, 1, 1)
        self.pol_5_in = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.pol_5_in.setObjectName("pol_5_in")
        self.gridLayout_5.addWidget(self.pol_5_in, 1, 0, 1, 1)
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(10, 310, 701, 61))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pol_6_lb = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.pol_6_lb.setObjectName("pol_6_lb")
        self.gridLayout_6.addWidget(self.pol_6_lb, 0, 0, 1, 1)
        self.pol_6_in = QtWidgets.QLineEdit(self.gridLayoutWidget_6)
        self.pol_6_in.setObjectName("pol_6_in")
        self.gridLayout_6.addWidget(self.pol_6_in, 1, 0, 1, 1)
        self.calc_button = QtWidgets.QPushButton(self.centralwidget)
        self.calc_button.setGeometry(QtCore.QRect(10, 380, 141, 41))
        self.calc_button.setObjectName("calc_button")
        self.result_lb = QtWidgets.QLabel(self.centralwidget)
        self.result_lb.setGeometry(QtCore.QRect(40, 420, 161, 41))
        self.result_lb.setObjectName("result_lb")
        self.result_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.result_bar.setGeometry(QtCore.QRect(210, 430, 521, 31))
        self.result_bar.setObjectName("result_bar")
        FactorStep.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FactorStep)
        self.statusbar.setObjectName("statusbar")
        FactorStep.setStatusBar(self.statusbar)

        self.retranslateUi(FactorStep)
        QtCore.QMetaObject.connectSlotsByName(FactorStep)
        self.calc_button.clicked.connect(self.calculate)

    def check(self, arr):
       c = re.compile('[^01 ]')
       for i in arr:
        if (len(c.findall(i))):
            return False
        else:
            return True

    def calc_mod(self, m1, m2):
        m1_bin = int(m1, 2)
        m2_bin = m2[::-1]
        res = []
        for i in range(len(m2_bin)):
            if int(m2_bin[i], 2) != 0:
                res.append(m1_bin * int(m2_bin[i], 2) * 2**i)
        x = 0
        for i in res:
            x ^= i
        return bin(x)[2:]

    def calculate(self):
        arr_pols = [self.pol_1_in.text(), 
                    self.pol_2_in.text(), 
                    self.pol_3_in.text(), 
                    self.pol_4_in.text(), 
                    self.pol_5_in.text(), 
                    self.pol_6_in.text()]
        c = 0
        for i in arr_pols:
            if i == '' or int(i, 2) == 0:
                arr_pols[c] = "1"
            c+=1
        print(arr_pols)
        if self.check(arr_pols):
            f2 = self.calc_mod(arr_pols[0], arr_pols[1])
            f3 = self.calc_mod(f2, arr_pols[2])
            f4 = self.calc_mod(f3, arr_pols[3])
            f5 = self.calc_mod(f4, arr_pols[4])
            f6 = self.calc_mod(f5, arr_pols[5])
            self.result_bar.setText(f"{f6}")
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            # setting message for Message Box
            msg.setText("Перевірте правильність введених даних.")
            # setting Message box window title
            msg.setWindowTitle("Помилка!")
            # declaring buttons on Message Box
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            # start the app
            retval = msg.exec_()

    def retranslateUi(self, FactorStep):
        _translate = QtCore.QCoreApplication.translate
        FactorStep.setWindowTitle(_translate("FactorStep", "FactorStep"))
        self.pol_1_lb.setText(_translate("FactorStep", "Поліном 1"))
        self.pol_2_lb.setText(_translate("FactorStep", "Поліном 2"))
        self.pol_3_lb.setText(_translate("FactorStep", "Поліном 3"))
        self.pol_4_lb.setText(_translate("FactorStep", "Поліном 4"))
        self.pol_5_lb.setText(_translate("FactorStep", "Поліном 5"))
        self.pol_6_lb.setText(_translate("FactorStep", "Поліном 6"))
        self.calc_button.setText(_translate("FactorStep", "Розрахувати"))
        self.result_lb.setText(_translate("FactorStep", "Результати:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FactorStep = QtWidgets.QMainWindow()
    ui = Ui_FactorStep()
    ui.setupUi(FactorStep)
    FactorStep.show()
    sys.exit(app.exec_())
