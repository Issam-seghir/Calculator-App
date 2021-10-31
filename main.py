#!/usr/bin/env python
# coding: utf-8


# ?  Copyright (c) <2021> <Seghir Issam>

# *  This program is free software: you can redistribute it and/or modify
# *  it under the terms of the GNU General Public License as published by
# *  the Free Software Foundation, either version 3 of the License, or
# *  (at your option) any later version.

# *  This program is distributed in the hope that it will be useful,
# *  but WITHOUT ANY WARRANTY; without even the implied warranty of
# *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# *  GNU General Public License for more details.

# *  You should have received a copy of the GNU General Public License
# *  along with this program.  If not, see <https://www.gnu.org/licenses/>.


# * theme :  QDarkGrayStyle  under ( MIT License)            #
# ?    Copyright (c) <2013-2014> <Colin Duquesnoy>            #
# ?    Copyright (c) <2017> <Michell Stuttgart>               #

# * Permission is hereby granted, free of charge, to any person obtaining a copy
# * of this software and associated documentation files (the "Software"), to deal
# * in the Software without restriction, including without limitation the rights
# * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# * copies of the Software, and to permit persons to whom the Software is
# * furnished to do so, subject to the following conditions:

# * The above copyright notice and this permission notice shall be included in
# * all copies or substantial portions of the Software.

# * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# * THE SOFTWARE.
# */

# ? for more details of MIT and GPLv3 License  file please read LICENSE.text
# ? for more explain of regex used in this script please read : Explain.md
# ? for more details of how  loops with exec/eval keyword work in this script , please read : Explain.md

import re
from random import randrange
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon, QScreen
from PyQt6.QtWidgets import (
    QAbstractButton,
    QApplication,
    QButtonGroup,
    QLineEdit,
    QWidget,
    QPushButton,
)
from PyQt6.uic.load_ui import loadUi

# u can replace ([]) with (sys.argv)
app = QApplication([])
window = QWidget()
# load Designer File
window = loadUi("Design.ui")


# add icon with specific size to main window
# * (use addFile to change mainwindow icon size because setIconSize() isn't working on QMainWindow)
icon = QIcon()
icon.addFile("icons/images.jpg", QSize(120, 120))
window.setWindowIcon(icon)


# button Groupe operands = 0,1,2,3,4,5,6,7,8,9
btnG_operands = QButtonGroup(window)
# button Groupe operator  = Sub,Add,Point,Div,Mod,Mul
btnG_operator = QButtonGroup(window)


# call Designer objects
for number in range(10):
    exec(f'btn{number} = window.findChild(QPushButton, "pushButton_{number}")')
    exec(f"btnG_operands.addButton(btn{number},number)")

operator = [
    "Sub",
    "Add",
    "Div",
    "Mod",
    "Mul",
    "Point",
    "Equal",
    "Clear",
    "Back",
    "Rand",
]

# operator[0:6] = "Sub","Point","Add","Div","Mod","Mul"
for opr in operator:
    exec(f'btn{opr} = window.findChild(QPushButton, "pushButton_{opr}")')
    if opr in operator[0:6]:
        exec(f"btnG_operator.addButton(btn{opr})")


# lineText where The Result of expression  showed
lineText = window.findChild(QLineEdit, "lineEdit")
lineText.setMaxLength(40)
BtnList = []  # List to contain the expression


def center(self):
    """center the app in the center of screen"""
    self.cordonne = self.frameGeometry()
    self.cp = QScreen.availableGeometry(QApplication.primaryScreen()).center()
    # methode 2 for pyqt5: cp = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()


def handler_btn(btn: QAbstractButton):
    # if the clicked button in [0,1,2,3,4,5,6,7,8,9]
    if btn in btnG_operands.buttons():
        # if the list = '0' ,avoid the case 0 in the beginning of expression => example: 000158 ,0000.78,0000-9
        if BtnList != ["0"]:
            BtnList.append(btn.text())
        # if list = 0 and the clicked button in (0..9) : clear list and add number
        # example : 0 => 5
        else:
            BtnList.clear()
            BtnList.append(btn.text())

    # if the clicked button in [Sub,Add,Point,Div,Mod,Mul]
    elif btn in btnG_operator.buttons():
        # if the list is not empty
        if BtnList:
            # example list = 18*8 last element is number
            if BtnList[-1].isdigit():
                # if the last element is number add any operator or point ,example : 18*8+ , 18*8. ,18*8-
                BtnList.append(btn.text())
            # example list = 12+ last element is operator
            # and the button clicked is Sub (-)
            elif BtnList[-1] in ["÷", "x", "+", "%"] and btn.text() == "-":
                # the case : 12+-5 ,12*-5 ...
                BtnList.append(btn.text())
        # if the list is empty and the button clicked is (-)
        elif btn.text() == "-":
            # the case (-) in the beginning : -5+2
            BtnList.append(btn.text())
    # ['7', '+', '2'] => 7+2
    x = re.sub("[',[\] ]", "", str(BtnList))
    # avoid the case two point or more : 18.15. ,12..1
    if not re.findall(r"[0-9]+\.[0-9]+\.", x):
        lineText.setText(x)
    # if the case is true ,then pop secend point : 18.15. => 18.15
    else:
        BtnList.pop()


def calcul_operation():
    # if the list is not empty => if BtnList != []
    if BtnList:
        x = re.sub("[',[\] ]", "", str(BtnList))
        x = re.sub("x", "*", x)
        x = re.sub("÷", "/", x)
        t = ("-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
        # test if the expression is complete , avoid case : 15*8/ => is not complete , -15*8+2
        if x.startswith(t) and x.endswith(  # start with (-) or number
            t[1:]
        ):  # end with number
            # * eval methode to convert string to commande line (Python code)
            res = str(eval(x))
            lineText.setText(res)
            BtnList.clear()
            BtnList.append(res)
        elif x != "":
            lineText.setText("Error...")
            BtnList.clear()


# Undo button : 148+93 => 148+9 =>148+ ...
def back():
    # if the list is not empty
    if BtnList:
        BtnList.pop()
        lineText.setText(str(BtnList)[1:-1].replace("'", "").replace(", ", ""))


def clear():
    """clear Button to clear text in <>LineText<> and clear List <>BtnList<>"""
    lineText.clear()
    #! Don't Forget to Clear the list after clear the text in Line Text
    BtnList.clear()


def rand():
    """Show random number between 1 and 999"""
    x = str(randrange(1, 999))
    lineText.setText(x)
    BtnList.clear()
    BtnList.append(x)


btnG_operands.buttonClicked.connect(handler_btn)
btnG_operator.buttonClicked.connect(handler_btn)

slots = ["calcul_operation", "clear", "back", "rand"]
for i, j in zip(operator[6:], slots):
    exec(f"btn{i}.clicked.connect({j})")

File = open("./Themes/QDarkGrayStyle.qss", "r")
with File:
    qss = File.read()
    app.setStyleSheet(qss)


def main():
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
