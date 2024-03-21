# main module
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout,QGridLayout

# main app object
app=QApplication([])
main_window=QWidget()
main_window.setWindowTitle("Calculator")
main_window.resize(250,300)

# app object
txt_box=QLineEdit()
grid=QGridLayout()

btn=["7","8","9","/","4","5","6","*","1","2","3","-","0",".","=","=",]

clear=QPushButton("Clear")
delete=QPushButton("<")

row=0
col=0
for txt in btn:
    new_btn=QPushButton(txt)
    # new_btn.clicked.connect()
    col+=1
    if col >3:
        col=0
        row+=1
    

# desing of application
master_layout=QVBoxLayout()
master_layout.addWidget(txt_box)
# master_layout.addLayout(grid)

btn_row=QHBoxLayout()
btn_row.addWidget(clear)
btn_row.addWidget(delete)

master_layout.addLayout(btn_row)
main_window.setLayout(master_layout)

# function

# events

# show and run
main_window.show()
app.exec_()