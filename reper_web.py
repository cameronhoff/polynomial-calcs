from logging import PlaceHolder
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class App(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Title
        self.setWindowTitle("Реперна сітка")
        # Layout
        form_layout = qtw.QFormLayout()
        self.setLayout(form_layout)
        
        # Inputs
        radix_in = qtw.QLineEdit()
        radix_in.setFont(qtg.QFont('Helvetica', 16))
        polDegIn = qtw.QLineEdit()
        polDegIn.setFont(qtg.QFont('Helvetica', 16))
        polIn = qtw.QLineEdit()
        polIn.setFont(qtg.QFont('Helvetica', 16))
        cModeIn = qtw.QComboBox(self)
        cModeIn.setFont(qtg.QFont('Helvetica', 16))
        cModeIn.addItems(["A", "T"])

        # Button
        calc = qtw.QPushButton("Розрахувати", 
            clicked = lambda: self.calculate(cModeIn.currentText()))
        calc.setFont(qtg.QFont('Helvetica', 16))

        # Layout inputs
        form_layout.addRow("Система числення:", radix_in)
        form_layout.addRow("Степінь полінома:", polDegIn)
        form_layout.addRow("Поліном:", polIn)
        form_layout.addRow("Режим рахунку:", cModeIn)
        # Layout buttons
        form_layout.addRow(calc)
        self.show()

    def calculate(self, mode):
        print(mode)

app = qtw.QApplication([])
mw = App()

app.exec_()