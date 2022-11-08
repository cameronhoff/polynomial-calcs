from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_reper_web(object):
    def setupUi(self, reper_web):
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text")
        font.setPointSize(10)

        reper_web.setObjectName("reper_web")
        reper_web.resize(594, 430)
        reper_web.setFixedSize(594, 430)
        self.centralwidget = QtWidgets.QWidget(reper_web)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setMinimumSize(594, 430)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 561, 181))
        self.groupBox.setMinimumSize(self.groupBox.size())
        self.groupBox.setFixedSize(self.groupBox.size())
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(210, 130, 141, 41))
        self.pushButton.setMinimumSize(self.pushButton.size())
        self.pushButton.setFixedSize(self.pushButton.size())
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.radix_label = QtWidgets.QLabel(self.groupBox)
        self.radix_label.setGeometry(QtCore.QRect(30, 40, 191, 20))
        self.radix_label.setFixedSize(self.radix_label.size())
        self.radix_label.setFont(font)
        self.radix_label.setObjectName("radix_label")
        self.radix_input = QtWidgets.QComboBox(self.groupBox)
        self.radix_input.setGeometry(QtCore.QRect(220, 35, 50, 26))
        self.radix_input.setFixedSize(self.radix_input.size())
        self.radix_input.addItems(["2", "8", "10", "16"])
        self.radix_input.setDisabled(True)
        self.radix_input.setFont(font)
        self.radix_input.setObjectName("lineEdit")
        self.pol_deg_label = QtWidgets.QLabel(self.groupBox)
        self.pol_deg_label.setGeometry(QtCore.QRect(30, 70, 191, 20))
        self.pol_deg_label.setFixedSize(self.pol_deg_label.size())
        self.pol_deg_label.setFont(font)
        self.pol_deg_label.setObjectName("pol_deg_label")
        self.pol_label = QtWidgets.QLabel(self.groupBox)
        self.pol_label.setGeometry(QtCore.QRect(30, 100, 171, 21))
        self.pol_label.setFixedSize(self.pol_label.size())
        self.pol_label.setFont(font)
        self.pol_label.setObjectName("pol_label")
        self.pol_deg_input = QtWidgets.QLineEdit(self.groupBox)
        self.pol_deg_input.setGeometry(QtCore.QRect(220, 65, 50, 26))
        self.pol_deg_input.setFixedSize(self.pol_deg_input.size())
        self.pol_deg_input.setFont(font)
        self.pol_deg_input.setObjectName("lineEdit_2")
        self.pol_deg_input.setDisabled(True)
        self.polinom_input = QtWidgets.QLineEdit(self.groupBox)
        self.polinom_input.setGeometry(QtCore.QRect(220, 100, 331, 26))
        # fix size
        self.polinom_input.setFixedSize(self.polinom_input.size())
        self.polinom_input.setFont(font)
        self.polinom_input.setObjectName("lineEdit_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 185, 561, 201))
        # fix size
        self.groupBox_2.setFixedSize(self.groupBox_2.size())
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.result_label = QtWidgets.QListView(self.groupBox_2)
        self.result_label.setGeometry(QtCore.QRect(20, 30, 520, 165))
        self.result_label.setFixedSize(self.result_label.size())
        self.result_label.setObjectName("result_label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 400, 261, 88))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        reper_web.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(reper_web)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 594, 21))
        self.menubar.setObjectName("menubar")
        reper_web.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(reper_web)
        self.statusbar.setObjectName("statusbar")
        reper_web.setStatusBar(self.statusbar)

        self.retranslateUi(reper_web)
        QtCore.QMetaObject.connectSlotsByName(reper_web)
        # On click calc button exec calculate func
        self.pushButton.clicked.connect(self.calculate)

    def calc_mod(self, step):
        step = bin(step)[2:]
        factor = int(step, 2)
        arr_factor = [x for x in step[::-1]]
        arr_res = []
        for i in range(len(arr_factor)):
            arr_res = [*arr_res, (factor*int(arr_factor[i], 2))<<i]
        x = 0
        for i in arr_res:
            x ^= i
        return bin(x)[2:]+"0"
           

    def if_call_back(self, step, degree, polinom_int):
        if len(bin(step)[2:]) >= degree:
            diff = len(bin(step)[2:]) - (degree+1)
            pol_step = polinom_int * (2**diff)
            print(pol_step)
            step = step ^ int(pol_step)
            step = self.if_call_back(step, degree, polinom_int)
        return step

    def calculate(self):
        try:
            polinom_bin = self.polinom_input.text()
            res_steps = [2]
            step = 2
            polinom_int = int(polinom_bin, int(self.radix_input.currentText()))
            degree = len(bin(polinom_int)[2:])-1 
            self.pol_deg_input.setText(f"{degree}")
            for i in range(1, 255):
                # Step > polinom length
                if len(self.calc_mod(step)) < degree + 1:
                    step = int(self.calc_mod(step), 2)
                    res_steps = [*res_steps, step]
                    if step == 1:
                        return
                # Step < polinom length
                else:
                    step = int(self.calc_mod(step), 2)
                    step = self.if_call_back(step, degree, polinom_int)
                    res_steps = [*res_steps, step]
                    if (int(self.calc_mod(step), 2) in res_steps) and (step == 1 or 
                                                                step == 2 or 
                                                                step == 8 or 
                                                                step == 128 or 
                                                                step == 32768 or 
                                                                step == 2147483648
                    ):
                        break
                        
            res_steps = [bin(x)[2:] for x in res_steps]
            model = QtGui.QStandardItemModel()
            self.result_label.setModel(model)
            for i in range(len(res_steps)):
                item = QtGui.QStandardItem(f"{i+1}. {res_steps[i]}")
                model.appendRow(item)
        except Exception as e:
            print(e)
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

    def retranslateUi(self, reper_web):
        _translate = QtCore.QCoreApplication.translate
        reper_web.setWindowTitle(_translate("reper_web", "Відрахування періоду циклу полінома"))
        self.groupBox.setTitle(_translate("reper_web", "Дані"))
        self.pushButton.setText(_translate("reper_web", "Розрахувати"))
        self.radix_label.setText(_translate("reper_web", "Система числення:"))
        self.pol_deg_label.setText(_translate("reper_web", "Степінь полінома:"))
        self.pol_label.setText(_translate("reper_web", "Поліном:"))
        self.groupBox_2.setTitle(_translate("reper_web", "Результати"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    reper_web = QtWidgets.QMainWindow()
    ui = Ui_reper_web()
    ui.setupUi(reper_web)
    reper_web.show()
    sys.exit(app.exec_())
