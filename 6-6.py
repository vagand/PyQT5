## Ex 6-6. CustomDialog

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QPushButton, QLineEdit, QVBoxLayout, QLabel, QHBoxLayout

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MyDialog')
        self.le = QLineEdit()
        btnOK = QPushButton("확인")
        btnCancel = QPushButton("취소")

        btnOK.clicked.connect(self.accept)
        btnCancel.clicked.connect(self.reject)

        layout2 = QHBoxLayout()
        layout2.addWidget(btnOK)
        layout2.addWidget(btnCancel)

        layout = QVBoxLayout()
        layout.addWidget(self.le)
        layout.addLayout(layout2)

        self.setLayout(layout)
        self.show()

    def showModal(self):
        return super().exec_()

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel("test", self)

        btn = QPushButton('showCustomDialog', self)
        btn.move(20, 20)
        btn.clicked.connect(self.showDialog)

        self.setWindowTitle('QMessageBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def showDialog(self):
        d = MyDialog()
        r = d.showModal()

        if r:
            text = d.le.text()
            self.lbl.setText(text)


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())