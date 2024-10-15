from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont
import sys
import datetime

class Switch(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text Switcher")
        self.setGeometry(200, 200, 1500, 800)
        


        self.reset_button = QPushButton("Clear", self)
        self.font(self.reset_button, 20, 700)
        self.reset_button.setFixedWidth(350)  
        self.reset_button.clicked.connect(self.clear)



        self.text = QLineEdit(self)
        self.text.setPlaceholderText("Enter text..")
        self.font(self.text, 165, 100)
        self.text.setFixedWidth(1200)  




        self.result_text = QLabel("Result: ", self)
        self.result = QLineEdit(self)
        self.font(self.result_text, 10, 255)
        self.font(self.result, 165, 250)
        self.result.setFixedWidth(1200)  
        self.result.setReadOnly(True)
        self.result_text.hide()
        self.result.hide()



        self.text_lower = QPushButton("Lower", self)
        self.font(self.text_lower, 165, 350)
        self.text_lower.setFixedWidth(350) 
        self.text_lower.clicked.connect(self.lower_text)



        self.text_upper = QPushButton("Upper", self)
        self.font(self.text_upper, 600, 350)
        self.text_upper.setFixedWidth(350) 
        self.text_upper.clicked.connect(self.upper_text)



        self.text_len = QPushButton("Length", self)
        self.font(self.text_len, 165, 450) 
        self.text_len.setFixedWidth(350) 
        self.text_len.clicked.connect(self.len_text)



        self.text_reverse = QPushButton("Reverse", self)
        self.font(self.text_reverse, 600, 450)
        self.text_reverse.setFixedWidth(350) 
        self.text_reverse.clicked.connect(self.reverse_text)




        self.text_time = QPushButton("Time now", self)
        self.font(self.text_time, 165, 550)
        self.text_time.setFixedWidth(350) 
        self.text_time.clicked.connect(self.xozirgi_sana)




        self.text_capitalize = QPushButton("Capitalize", self)
        self.font(self.text_capitalize, 600, 550)
        self.text_capitalize.setFixedWidth(350) 
        self.text_capitalize.clicked.connect(self.capitalize_text)


        



    def check_text(self):
        if not self.text.text():
            QMessageBox.warning(self, "Xato", "Ma'lumot kiritilmagan!")
            return False
        return True




    def reverse_text(self):
        if not self.check_text():
            return
        text = self.text.text()
        self.result.setText(text[::-1])
        self.result_text.show()
        self.result.show()




    def len_text(self):
        if not self.check_text():
            return
        text = self.text.text()
        self.result.setText(str(len(text)))
        self.result_text.show()
        self.result.show()




    def lower_text(self):
        if not self.check_text():
            return
        text = self.text.text()
        self.result.setText(text.lower().strip())
        self.result_text.show()
        self.result.show()




    def capitalize_text(self):
        if not self.check_text():
            return
        text = self.text.text()
        self.result.setText(text.capitalize().strip())
        self.result_text.show()
        self.result.show()




    def upper_text(self):
        if not self.check_text():
            return
        text = self.text.text()
        self.result.setText(text.upper().strip())
        self.result_text.show()
        self.result.show()




    def font(self, obj, x, y):
        obj.setFont(QFont("Kristen ITC", 24))
        obj.move(x, y)




    def xozirgi_sana(self):
        now = datetime.datetime.now()
        self.result.setText(str(now.strftime("%Y-%m-%d %H:%M:%S")))
        self.result_text.show()
        self.result.show()




    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()  
        else:
            event.ignore()  

    

    def clear(self):
        self.text.setText("")
        self.result.setText("")
        self.result_text.hide()
        self.result.hide()
        




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Switch()
    window.show()
    sys.exit(app.exec_())
