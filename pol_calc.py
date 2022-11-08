from PyQt5 import QtCore, QtGui, QtWidgets
import re

class Ui_mod_calculations(object):
    def setupUi(self, mod_calculations):
        mod_calculations.setObjectName("mod_calculations")
        mod_calculations.resize(874, 524)
        font = QtGui.QFont()
        font.setPointSize(9)
        mod_calculations.setFont(font)
        self.centralwidget = QtWidgets.QWidget(mod_calculations)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 841, 451))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setIconSize(QtCore.QSize(19, 19))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.calc_mult_button = QtWidgets.QPushButton(self.tab)
        self.calc_mult_button.setGeometry(QtCore.QRect(300, 220, 131, 41))
        self.calc_mult_button.setObjectName("calc_mult_button")
        # added
        self.calc_mult_button.clicked.connect(self.calculate_mult)
        self.mnog1_input = QtWidgets.QLineEdit(self.tab)
        self.mnog1_input.setGeometry(QtCore.QRect(200, 70, 521, 21))
        self.mnog1_input.setObjectName("mnog1_input")
        self.mnog1_label = QtWidgets.QLabel(self.tab)
        self.mnog1_label.setGeometry(QtCore.QRect(20, 70, 141, 41))
        self.mnog1_label.setObjectName("mnog1_label")
        self.mnog2_label = QtWidgets.QLabel(self.tab)
        self.mnog2_label.setGeometry(QtCore.QRect(20, 120, 131, 31))
        self.mnog2_label.setObjectName("mnog2_label")
        self.dobutok_mult_label = QtWidgets.QLabel(self.tab)
        self.dobutok_mult_label.setGeometry(QtCore.QRect(20, 170, 141, 31))
        self.dobutok_mult_label.setObjectName("dobutok_mult_label")
        self.mnog2_input = QtWidgets.QLineEdit(self.tab)
        self.mnog2_input.setGeometry(QtCore.QRect(200, 120, 521, 21))
        self.mnog2_input.setObjectName("mnog2_input")
        self.dobutok_input = QtWidgets.QLineEdit(self.tab)
        self.dobutok_input.setGeometry(QtCore.QRect(200, 170, 571, 21))
        self.dobutok_input.setObjectName("dobutok_input")
        self.radix_mult = QtWidgets.QComboBox(self.tab)
        self.radix_mult.setGeometry(QtCore.QRect(70, 20, 69, 22))
        self.radix_mult.setObjectName("radix_mult")
        # added
        self.radix_mult.addItems(["2", "3", "5", "7"])
        self.radix_mult_label = QtWidgets.QLabel(self.tab)
        self.radix_mult_label.setGeometry(QtCore.QRect(20, 10, 51, 41))
        self.radix_mult_label.setObjectName("radix_mult_label")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.radix_rweb = QtWidgets.QComboBox(self.tab_2)
        self.radix_rweb.setGeometry(QtCore.QRect(200, 30, 69, 22))
        self.radix_rweb.setObjectName("radix_rweb")
        self.radix_rweb_label = QtWidgets.QLabel(self.tab_2)
        self.radix_rweb_label.setGeometry(QtCore.QRect(10, 20, 171, 41))
        self.radix_rweb_label.setObjectName("radix_rweb_label")
        # added
        self.radix_rweb.addItems(["2"])
        self.radix_rweb.setDisabled(True)
        self.pol_deg_rweb_label = QtWidgets.QLabel(self.tab_2)
        self.pol_deg_rweb_label.setGeometry(QtCore.QRect(10, 70, 141, 41))
        self.pol_deg_rweb_label.setObjectName("pol_deg_rweb_label")
        self.pol_rweb_label = QtWidgets.QLabel(self.tab_2)
        self.pol_rweb_label.setGeometry(QtCore.QRect(10, 130, 141, 41))
        self.pol_rweb_label.setObjectName("pol_rweb_label")
        self.pol_deg_input = QtWidgets.QLineEdit(self.tab_2)
        self.pol_deg_input.setGeometry(QtCore.QRect(180, 80, 91, 21))
        self.pol_deg_input.setObjectName("pol_deg_input")
        self.pol_rweb_input = QtWidgets.QLineEdit(self.tab_2)
        self.pol_rweb_input.setGeometry(QtCore.QRect(160, 140, 611, 21))
        self.pol_rweb_input.setObjectName("pol_rweb_input")
        self.calc_rweb_button = QtWidgets.QPushButton(self.tab_2)
        self.calc_rweb_button.setGeometry(QtCore.QRect(330, 170, 111, 41))
        self.calc_rweb_button.setObjectName("calc_rweb_button")
        # added
        self.calc_rweb_button.clicked.connect(self.calculate_rweb)
        self.results_rweb_groupbox = QtWidgets.QGroupBox(self.tab_2)
        self.results_rweb_groupbox.setGeometry(QtCore.QRect(10, 210, 771, 201))
        self.results_rweb_groupbox.setObjectName("results_rweb_groupbox")
        self.results_rweb = QtWidgets.QListView(self.results_rweb_groupbox)
        self.results_rweb.setGeometry(QtCore.QRect(10, 20, 751, 171))
        self.results_rweb.setObjectName("results_rweb")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pol1_fstep_input = QtWidgets.QLineEdit(self.tab_3)
        self.pol1_fstep_input.setGeometry(QtCore.QRect(10, 30, 611, 21))
        self.pol1_fstep_input.setObjectName("pol1_fstep_input")
        self.pol2_fstep_input = QtWidgets.QLineEdit(self.tab_3)
        self.pol2_fstep_input.setGeometry(QtCore.QRect(10, 80, 611, 21))
        self.pol2_fstep_input.setObjectName("pol2_fstep_input")
        self.pol3_fstep_input = QtWidgets.QLineEdit(self.tab_3)
        self.pol3_fstep_input.setGeometry(QtCore.QRect(10, 130, 611, 21))
        self.pol3_fstep_input.setObjectName("pol3_fstep_input")
        self.pol4_fstep_input = QtWidgets.QLineEdit(self.tab_3)
        self.pol4_fstep_input.setGeometry(QtCore.QRect(10, 180, 611, 21))
        self.pol4_fstep_input.setObjectName("pol4_fstep_input")
        self.pol5_fstep_input = QtWidgets.QLineEdit(self.tab_3)
        self.pol5_fstep_input.setGeometry(QtCore.QRect(10, 230, 611, 21))
        self.pol5_fstep_input.setObjectName("pol5_fstep_input")
        self.pol6_fstep_input = QtWidgets.QLineEdit(self.tab_3)
        self.pol6_fstep_input.setGeometry(QtCore.QRect(10, 280, 611, 21))
        self.pol6_fstep_input.setObjectName("pol6_fstep_input")
        self.pol1_fstep_label = QtWidgets.QLabel(self.tab_3)
        self.pol1_fstep_label.setGeometry(QtCore.QRect(10, 10, 161, 21))
        self.pol1_fstep_label.setObjectName("pol1_fstep_label")
        self.pol2_fstep_label = QtWidgets.QLabel(self.tab_3)
        self.pol2_fstep_label.setGeometry(QtCore.QRect(10, 60, 161, 21))
        self.pol2_fstep_label.setObjectName("pol2_fstep_label")
        self.pol3_fstep_label = QtWidgets.QLabel(self.tab_3)
        self.pol3_fstep_label.setGeometry(QtCore.QRect(10, 110, 161, 21))
        self.pol3_fstep_label.setObjectName("pol3_fstep_label")
        self.pol4_fstep_label = QtWidgets.QLabel(self.tab_3)
        self.pol4_fstep_label.setGeometry(QtCore.QRect(10, 160, 161, 21))
        self.pol4_fstep_label.setObjectName("pol4_fstep_label")
        self.pol5_fstep_label = QtWidgets.QLabel(self.tab_3)
        self.pol5_fstep_label.setGeometry(QtCore.QRect(10, 210, 161, 21))
        self.pol5_fstep_label.setObjectName("pol5_fstep_label")
        self.pol6_fstep_label = QtWidgets.QLabel(self.tab_3)
        self.pol6_fstep_label.setGeometry(QtCore.QRect(10, 260, 161, 21))
        self.pol6_fstep_label.setObjectName("pol6_fstep_label")
        self.calc_fstep_button = QtWidgets.QPushButton(self.tab_3)
        self.calc_fstep_button.setGeometry(QtCore.QRect(10, 310, 111, 41))
        self.calc_fstep_button.setObjectName("calc_fstep_button")
        # added
        self.calc_fstep_button.clicked.connect(self.calculate_fstep)
        self.results_fstep_input = QtWidgets.QLineEdit(self.tab_3)
        self.results_fstep_input.setGeometry(QtCore.QRect(10, 380, 771, 21))
        self.results_fstep_input.setObjectName("results_fstep_input")
        self.results_fstep_label = QtWidgets.QLabel(self.tab_3)
        self.results_fstep_label.setGeometry(QtCore.QRect(10, 360, 161, 21))
        self.results_fstep_label.setObjectName("results_fstep_label")
        self.pol_fstep_deg_1 = QtWidgets.QLabel(self.tab_3)
        self.pol_fstep_deg_1.setGeometry(QtCore.QRect(150, 10, 31, 21))
        self.pol_fstep_deg_1.setObjectName("pol_fstep_deg_1")
        self.pol_fstep_deg_2 = QtWidgets.QLabel(self.tab_3)
        self.pol_fstep_deg_2.setGeometry(QtCore.QRect(150, 60, 31, 21))
        self.pol_fstep_deg_2.setObjectName("pol_fstep_deg_2")
        self.pol_fstep_deg_3 = QtWidgets.QLabel(self.tab_3)
        self.pol_fstep_deg_3.setGeometry(QtCore.QRect(150, 110, 31, 21))
        self.pol_fstep_deg_3.setObjectName("pol_fstep_deg_3")
        self.pol_fstep_deg_4 = QtWidgets.QLabel(self.tab_3)
        self.pol_fstep_deg_4.setGeometry(QtCore.QRect(150, 160, 31, 21))
        self.pol_fstep_deg_4.setObjectName("pol_fstep_deg_4")
        self.pol_fstep_deg_5 = QtWidgets.QLabel(self.tab_3)
        self.pol_fstep_deg_5.setGeometry(QtCore.QRect(150, 210, 31, 21))
        self.pol_fstep_deg_5.setObjectName("pol_fstep_deg_5")
        self.pol_fstep_deg_6 = QtWidgets.QLabel(self.tab_3)
        self.pol_fstep_deg_6.setGeometry(QtCore.QRect(150, 260, 31, 21))
        self.pol_fstep_deg_6.setObjectName("pol_fstep_deg_6")
        self.pol_fstep_deg_value_1 = QtWidgets.QLabel(self.tab_3)
        self.pol_fstep_deg_value_1.setGeometry(QtCore.QRect(190, 10, 121, 21))
        self.pol_fstep_deg_value_1.setText("")
        self.pol_fstep_deg_value_1.setObjectName("pol_fstep_deg_value_1")
        # added
        self.pol1_fstep_input.textChanged.connect(lambda: self.change_deg(1))
        self.pol_fstep_deg_value_2 = QtWidgets.QLabel(self.tab_3)
        self.pol_fstep_deg_value_2.setGeometry(QtCore.QRect(190, 60, 131, 21))
        self.pol_fstep_deg_value_2.setText("")
        self.pol_fstep_deg_value_2.setObjectName("pol_fstep_deg_value_2")
        self.pol_fstep_deg_value_3 = QtWidgets.QLabel(self.tab_3)
        self.pol_fstep_deg_value_3.setGeometry(QtCore.QRect(190, 110, 131, 21))
        self.pol_fstep_deg_value_3.setText("")
        self.pol_fstep_deg_value_3.setObjectName("pol_fstep_deg_value_3")
        self.pol_fstep_deg_value_4 = QtWidgets.QLabel(self.tab_3)
        self.pol_fstep_deg_value_4.setGeometry(QtCore.QRect(190, 160, 121, 21))
        self.pol_fstep_deg_value_4.setText("")
        self.pol_fstep_deg_value_4.setObjectName("pol_fstep_deg_value_4")
        self.pol_fstep_deg_value_5 = QtWidgets.QLabel(self.tab_3)
        self.pol_fstep_deg_value_5.setGeometry(QtCore.QRect(190, 210, 131, 21))
        self.pol_fstep_deg_value_5.setText("")
        self.pol_fstep_deg_value_5.setObjectName("pol_fstep_deg_value_5")
        self.pol_fstep_deg_value_6 = QtWidgets.QLabel(self.tab_3)
        self.pol_fstep_deg_value_6.setGeometry(QtCore.QRect(200, 260, 121, 21))
        self.pol_fstep_deg_value_6.setText("")
        self.pol_fstep_deg_value_6.setObjectName("pol_fstep_deg_value_6")
        self.tabWidget.addTab(self.tab_3, "")
        self.author_label = QtWidgets.QLabel(self.centralwidget)
        self.author_label.setGeometry(QtCore.QRect(20, 460, 301, 21))
        self.author_label.setObjectName("author_label")
        mod_calculations.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mod_calculations)
        self.statusbar.setObjectName("statusbar")
        mod_calculations.setStatusBar(self.statusbar)

        self.retranslateUi(mod_calculations)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(mod_calculations)

    def retranslateUi(self, mod_calculations):
        _translate = QtCore.QCoreApplication.translate
        mod_calculations.setWindowTitle(_translate("mod_calculations", "Розрахунки над поліномами"))
        self.calc_mult_button.setText(_translate("mod_calculations", "Розрахувати"))
        self.mnog1_label.setText(_translate("mod_calculations", "Множник-1:"))
        self.mnog2_label.setText(_translate("mod_calculations", "Множник-2:"))
        self.dobutok_mult_label.setText(_translate("mod_calculations", "Добуток:"))
        self.radix_mult_label.setText(_translate("mod_calculations", "Р:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("mod_calculations", "Модулярне множення"))
        self.radix_rweb_label.setText(_translate("mod_calculations", "Система числення:"))
        self.pol_deg_rweb_label.setText(_translate("mod_calculations", "Степінь полінома:"))
        self.pol_rweb_label.setText(_translate("mod_calculations", "Поліном:"))
        self.calc_rweb_button.setText(_translate("mod_calculations", "Розрахувати"))
        self.results_rweb_groupbox.setTitle(_translate("mod_calculations", "Результати"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("mod_calculations", "Відрахування періоду циклу полінома"))
        self.pol1_fstep_label.setText(_translate("mod_calculations", "Поліном 1:"))
        self.pol2_fstep_label.setText(_translate("mod_calculations", "Поліном 2:"))
        self.pol3_fstep_label.setText(_translate("mod_calculations", "Поліном 3:"))
        self.pol4_fstep_label.setText(_translate("mod_calculations", "Поліном 4:"))
        self.pol5_fstep_label.setText(_translate("mod_calculations", "Поліном 5:"))
        self.pol6_fstep_label.setText(_translate("mod_calculations", "Поліном 6:"))
        self.calc_fstep_button.setText(_translate("mod_calculations", "Розрахувати"))
        self.results_fstep_label.setText(_translate("mod_calculations", "Результати:"))
        self.pol_fstep_deg_1.setText(_translate("mod_calculations", "С = "))
        self.pol_fstep_deg_2.setText(_translate("mod_calculations", "С = "))
        self.pol_fstep_deg_3.setText(_translate("mod_calculations", "С = "))
        self.pol_fstep_deg_4.setText(_translate("mod_calculations", "С = "))
        self.pol_fstep_deg_5.setText(_translate("mod_calculations", "С = "))
        self.pol_fstep_deg_6.setText(_translate("mod_calculations", "С = "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("mod_calculations", "Факторизація степенів"))
        self.author_label.setText(_translate("mod_calculations", "Розробник: Дорошенко Денис"))

    def calculate_mult(self):
        # Convert FROM string TO int
        m1 = int(self.mnog1_input.text(), int(self.radix_mult.currentText()))
        m2 = self.mnog2_input.text()[::-1]
        res = []
        for i in range(len(self.mnog2_input.text())):
            if int(m2[i], int(self.radix_mult.currentText())) != 0:
                res.append(m1 * 2**i)
        x = 0
        for i in res:
            x ^= i
        if self.radix_mult.currentText() == "2":
            self.dobutok_input.setText(bin(x)[2:])
        else:
            rad = self.radix_mult.currentText()
            self.dobutok_input.setText(self.dec_to_base(x, int(rad)))

    def dec_to_base(self, num,base):  #Maximum base - 36
        base_num = ""
        while num>0:
            dig = int(num%base)
            if dig<10:
                base_num += str(dig)
            else:
                base_num += chr(ord('A')+dig-10)  #Using uppercase letters
            num //= base
        base_num = base_num[::-1]  #To reverse the string
        return base_num

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

    def calculate_rweb(self):
        try:
            polinom_bin = self.pol_rweb_input.text()
            res_steps = [2]
            step = 2
            polinom_int = int(polinom_bin, int(self.radix_rweb.currentText()))
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
            self.results_rweb.setModel(model)
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

    def check(self, arr):
       c = re.compile('[^01 ]')
       for i in arr:
        if (len(c.findall(i))):
            return False
        else:
            return True

    def calc_fstep(self, m1, m2):
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

    def calculate_fstep(self):
        arr_pols = [self.pol1_fstep_input.text(), 
                    self.pol2_fstep_input.text(), 
                    self.pol3_fstep_input.text(), 
                    self.pol4_fstep_input.text(), 
                    self.pol5_fstep_input.text(), 
                    self.pol6_fstep_input.text()]
        c = 0
        for i in arr_pols:
            if i == '' or int(i, 2) == 0:
                arr_pols[c] = "1"
            c+=1
        print(arr_pols)
        if self.check(arr_pols):
            f2 = self.calc_fstep(arr_pols[0], arr_pols[1])
            f3 = self.calc_fstep(f2, arr_pols[2])
            f4 = self.calc_fstep(f3, arr_pols[3])
            f5 = self.calc_fstep(f4, arr_pols[4])
            f6 = self.calc_fstep(f5, arr_pols[5])
            self.results_fstep_input.setText(f"{f6}")
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

    # change degree of label in fstep
    def change_deg(self, n):
        pol_deg_labels = [
            self.pol_fstep_deg_value_1,
            #self.pol_fstep_deg_value_2,
            #self.pol_fstep_deg_value_3,
            #self.pol_fstep_deg_value_4,
            #self.pol_fstep_deg_value_5,
            #self.pol_fstep_deg_value_6
        ]
        pol_inputs = [
            self.pol1_fstep_input,
            self.pol2_fstep_input,
            self.pol3_fstep_input,
            self.pol4_fstep_input,
            self.pol5_fstep_input,
            self.pol6_fstep_input
        ]
        for i in range(len(pol_deg_labels)):
            if i == n-1:
                pol_deg_labels[i].setText(str(len(pol_inputs[i].text())))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mod_calculations = QtWidgets.QMainWindow()
    ui = Ui_mod_calculations()
    ui.setupUi(mod_calculations)
    mod_calculations.show()
    sys.exit(app.exec_())