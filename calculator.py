from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QLineEdit,QMessageBox
from PyQt5.QtGui import QFont
import sys

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(200, 200, 1000, 600)


        self.txt = QLabel("Enter number 1: ", self)
        self.num1 = QLineEdit(self)
        self.num1.setPlaceholderText("Enter number..")
        self.font(self.txt, 20, 100)
        self.font(self.num1, 400, 100)
        

        
        self.txt2 = QLabel("Enter number 2: ", self)
        self.num2 = QLineEdit(self)
        self.num2.setPlaceholderText("Enter number...")
        self.font(self.txt2, 20, 170)
        self.font(self.num2, 400, 170)
        


        self.matn1 = QLabel("Result: ", self)
        self.result = QLineEdit(self)
        self.font(self.matn1, 20, 255)
        self.font(self.result, 400, 250)
        self.result.setReadOnly(True)
        self.matn1.hide()
        self.result.hide()
        


        self.kopaytirish = QPushButton("*", self)
        self.font(self.kopaytirish, 250, 350)
        self.kopaytirish.clicked.connect(self.kopaytirish_amal)
       
    

        self.bolish = QPushButton("/", self)
        self.font(self.bolish, 370, 350)
        self.bolish.clicked.connect(self.bolish_amal)




        self.ayirish = QPushButton("-", self)
        self.font(self.ayirish, 490, 350)
        self.ayirish.clicked.connect(self.ayirish_amal)




        self.qoshish = QPushButton("+", self)
        self.font(self.qoshish, 610, 350)
        self.qoshish.clicked.connect(self.qoshish_amal)





        self.reset_button = QPushButton("Reset", self)
        self.font(self.reset_button, 120, 350)
        self.reset_button.clicked.connect(self.reset)

        
        
    def font(self, obj, x, y):
        obj.setFont(QFont("Kristen ITC", 24))
        obj.move(x, y)




    def qoshish_amal(self):
        self.calculate(lambda x, y: x + y)





    def ayirish_amal(self):
        self.calculate(lambda x, y: x - y)




    def kopaytirish_amal(self):
        self.calculate(lambda x, y: x * y)

    def show_error(self):
        xato = QMessageBox()
        xato.setIcon(QMessageBox.Critical)
        xato.setText("0 ga bo'linmaydi")
        xato.setWindowTitle("Error")
        xato.setStandardButtons(QMessageBox.Ok)
        xato.exec_()

    def bolish_amal(self):
        
        try:
            num1 = int(self.num1.text())
            num2 = int(self.num2.text())
            if num2 == 0:
                self.show_error()
                return
            else:
                result = num1 // num2
                self.result.setText(str(result))
            self.matn1.show()
            self.result.show()
        except ValueError:
            self.result.setText("Invalid input")
            self.matn1.show()
            self.result.show()

    def calculate(self, operation):
        try:
            num1 = int(self.num1.text())
            num2 = int(self.num2.text())
            result = operation(num1, num2)
            self.result.setText(str(result))
            self.matn1.show()
            self.result.show()
        except ValueError:
            self.result.setText("Invalid input")
            self.matn1.show()
            self.result.show()

    def reset(self):
        self.num1.setText("")
        self.num2.setText("")
        self.result.setText("")
        self.matn1.hide()
        self.result.hide()


    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()  
        else:
            event.ignore() 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())
