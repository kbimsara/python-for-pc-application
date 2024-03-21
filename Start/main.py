# main  module
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout
from random import choice

# main app object
app=QApplication([])
main_window=QWidget()
main_window.setWindowTitle("Sample window header text")
main_window.resize(400,200)

# app objects
title_text=QLabel("This is title layout")

lable1=QLabel("Text-01")
lable2=QLabel("Text-02")
lable3=QLabel("Text-03")

btn1=QPushButton("Button-01")
btn2=QPushButton("Button-02")
btn3=QPushButton("Button-03")

# design of application
master_layput=QVBoxLayout()

row1=QHBoxLayout()
row2=QHBoxLayout()
row3=QHBoxLayout()

row1.addWidget(title_text,alignment=Qt.AlignCenter)

row2.addWidget(lable1,alignment=Qt.AlignCenter)
row2.addWidget(lable2,alignment=Qt.AlignCenter)
row2.addWidget(lable3,alignment=Qt.AlignCenter)

row3.addWidget(btn1,alignment=Qt.AlignCenter)
row3.addWidget(btn2,alignment=Qt.AlignCenter)
row3.addWidget(btn3,alignment=Qt.AlignCenter)

master_layput.addLayout(row1)
master_layput.addLayout(row2)
master_layput.addLayout(row3)

main_window.setLayout(master_layput)

# functions
my_word=["hello","goodbty","test","python","PyQt","Code"]

def display_rand1():
    word=choice(my_word)
    lable1.setText(word)

def display_rand2():
    word=choice(my_word)
    lable2.setText(word)

def display_rand3():
    word=choice(my_word)
    lable3.setText(word)

# events
btn1.clicked.connect(display_rand1)
btn2.clicked.connect(display_rand2)
btn3.clicked.connect(display_rand3)

# show/run code
main_window.show()
app.exec_()