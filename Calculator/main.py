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

btn=["7","8","9","/","4","5","6","*","1","2","3","-","0",".","=","+",]

clear=QPushButton("Clear")
delete=QPushButton("<")

# function
def click():
    new_btn=app.sender()
    txt=new_btn.text()
    # txt_box.setText(str(txt)) #we can see witch button click

    if txt=="=":
        symbol=txt_box.text()
        try:
            result=eval(symbol)
            txt_box.setText(str(result))
        except Exception as e:
            print("Error :",e)
    elif txt=="clear":
        txt_box.clear()
    elif txt=="<":
        current_val=txt_box.text()
        txt_box.setText(current_val[:-1])
    else:
        current_val=txt_box.text()
        txt_box.setText(current_val+txt)

row=0
col=0

for txt in btn:
    new_btn=QPushButton(txt)   
    new_btn.clicked.connect(click)
    grid.addWidget(new_btn,row,col)
    col+=1
    if col >3:
        col=0
        row+=1
    
# desing of application
master_layout=QVBoxLayout()
master_layout.addWidget(txt_box)
master_layout.addLayout(grid)

btn_row=QHBoxLayout()
btn_row.addWidget(clear)
btn_row.addWidget(delete)

master_layout.addLayout(btn_row)
main_window.setLayout(master_layout)


# events
clear.clicked.connect(click)
delete.clicked.connect(click)

# show and run
main_window.show()
app.exec_()