# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Design.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLayout, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.NonModal)
        Form.setEnabled(True)
        Form.resize(478, 380)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setSizeIncrement(QSize(0, 0))
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"")
        Form.setInputMethodHints(Qt.ImhNone)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.pushButton_Point = QPushButton(Form)
        self.pushButton_Point.setObjectName(u"pushButton_Point")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_Point.sizePolicy().hasHeightForWidth())
        self.pushButton_Point.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(18)
        self.pushButton_Point.setFont(font)
        self.pushButton_Point.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_Point, 2, 4, 1, 1)

        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy1.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy1)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_4, 2, 0, 1, 1)

        self.pushButton_Div = QPushButton(Form)
        self.pushButton_Div.setObjectName(u"pushButton_Div")
        sizePolicy1.setHeightForWidth(self.pushButton_Div.sizePolicy().hasHeightForWidth())
        self.pushButton_Div.setSizePolicy(sizePolicy1)
        self.pushButton_Div.setMinimumSize(QSize(110, 0))
        self.pushButton_Div.setFont(font)
        self.pushButton_Div.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.pushButton_Div.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_Div, 0, 2, 1, 1)

        self.pushButton_0 = QPushButton(Form)
        self.pushButton_0.setObjectName(u"pushButton_0")
        sizePolicy1.setHeightForWidth(self.pushButton_0.sizePolicy().hasHeightForWidth())
        self.pushButton_0.setSizePolicy(sizePolicy1)
        self.pushButton_0.setMinimumSize(QSize(0, 50))
        self.pushButton_0.setFont(font)
        self.pushButton_0.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_0, 4, 1, 1, 1)

        self.pushButton_6 = QPushButton(Form)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy1.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy1)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_6, 2, 2, 1, 1)

        self.pushButton_Rand = QPushButton(Form)
        self.pushButton_Rand.setObjectName(u"pushButton_Rand")
        sizePolicy1.setHeightForWidth(self.pushButton_Rand.sizePolicy().hasHeightForWidth())
        self.pushButton_Rand.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(14)
        self.pushButton_Rand.setFont(font1)
        self.pushButton_Rand.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_Rand, 3, 4, 1, 1)

        self.pushButton_1 = QPushButton(Form)
        self.pushButton_1.setObjectName(u"pushButton_1")
        sizePolicy1.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy1)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet(u"")
        self.pushButton_1.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_1, 1, 0, 1, 1)

        self.pushButton_9 = QPushButton(Form)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy1.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy1)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_9, 3, 2, 1, 1)

        self.pushButton_Back = QPushButton(Form)
        self.pushButton_Back.setObjectName(u"pushButton_Back")
        sizePolicy1.setHeightForWidth(self.pushButton_Back.sizePolicy().hasHeightForWidth())
        self.pushButton_Back.setSizePolicy(sizePolicy1)
        self.pushButton_Back.setFont(font)
        self.pushButton_Back.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_Back, 4, 2, 1, 1)

        self.pushButton_8 = QPushButton(Form)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy1.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy1)
        self.pushButton_8.setMinimumSize(QSize(0, 50))
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_8, 3, 1, 1, 1)

        self.pushButton_Equal = QPushButton(Form)
        self.pushButton_Equal.setObjectName(u"pushButton_Equal")
        sizePolicy1.setHeightForWidth(self.pushButton_Equal.sizePolicy().hasHeightForWidth())
        self.pushButton_Equal.setSizePolicy(sizePolicy1)
        self.pushButton_Equal.setFont(font)
        self.pushButton_Equal.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_Equal, 4, 4, 1, 1)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_3, 1, 2, 1, 1)

        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy1.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy1)
        self.pushButton_5.setMinimumSize(QSize(0, 50))
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)

        self.pushButton_Mod = QPushButton(Form)
        self.pushButton_Mod.setObjectName(u"pushButton_Mod")
        sizePolicy1.setHeightForWidth(self.pushButton_Mod.sizePolicy().hasHeightForWidth())
        self.pushButton_Mod.setSizePolicy(sizePolicy1)
        self.pushButton_Mod.setFont(font)
        self.pushButton_Mod.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_Mod, 1, 4, 1, 1)

        self.pushButton_7 = QPushButton(Form)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy1.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy1)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_7, 3, 0, 1, 1)

        self.pushButton_Add = QPushButton(Form)
        self.pushButton_Add.setObjectName(u"pushButton_Add")
        sizePolicy1.setHeightForWidth(self.pushButton_Add.sizePolicy().hasHeightForWidth())
        self.pushButton_Add.setSizePolicy(sizePolicy1)
        self.pushButton_Add.setMinimumSize(QSize(110, 50))
        self.pushButton_Add.setFont(font)
        self.pushButton_Add.setStyleSheet(u"")
        self.pushButton_Add.setIconSize(QSize(50, 16))

        self.gridLayout.addWidget(self.pushButton_Add, 0, 0, 1, 1)

        self.pushButton_Sub = QPushButton(Form)
        self.pushButton_Sub.setObjectName(u"pushButton_Sub")
        sizePolicy1.setHeightForWidth(self.pushButton_Sub.sizePolicy().hasHeightForWidth())
        self.pushButton_Sub.setSizePolicy(sizePolicy1)
        self.pushButton_Sub.setMinimumSize(QSize(110, 0))
        self.pushButton_Sub.setFont(font)
        self.pushButton_Sub.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_Sub, 0, 1, 1, 1)

        self.pushButton_Mul = QPushButton(Form)
        self.pushButton_Mul.setObjectName(u"pushButton_Mul")
        sizePolicy1.setHeightForWidth(self.pushButton_Mul.sizePolicy().hasHeightForWidth())
        self.pushButton_Mul.setSizePolicy(sizePolicy1)
        self.pushButton_Mul.setMinimumSize(QSize(110, 0))
        self.pushButton_Mul.setFont(font)
        self.pushButton_Mul.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_Mul, 0, 4, 1, 1)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setMinimumSize(QSize(0, 50))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.pushButton_Clear = QPushButton(Form)
        self.pushButton_Clear.setObjectName(u"pushButton_Clear")
        sizePolicy1.setHeightForWidth(self.pushButton_Clear.sizePolicy().hasHeightForWidth())
        self.pushButton_Clear.setSizePolicy(sizePolicy1)
        self.pushButton_Clear.setFont(font)
        self.pushButton_Clear.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_Clear, 4, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setMinimumSize(QSize(400, 70))
        self.lineEdit.setMaximumSize(QSize(2000, 2000))
        self.lineEdit.setSizeIncrement(QSize(1600, 1000))
        font2 = QFont()
        font2.setPointSize(22)
        font2.setBold(False)
        font2.setItalic(False)
        self.lineEdit.setFont(font2)
        self.lineEdit.setStyleSheet(u"")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setClearButtonEnabled(False)

        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.pushButton_1.setDefault(True)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Calculator", None))
        self.pushButton_Point.setText(QCoreApplication.translate("Form", u".", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.pushButton_Div.setText(QCoreApplication.translate("Form", u"\u00f7", None))
        self.pushButton_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_Rand.setText(QCoreApplication.translate("Form", u"Rand", None))
        self.pushButton_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.pushButton_Back.setText(QCoreApplication.translate("Form", u"\u232b", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.pushButton_Equal.setText(QCoreApplication.translate("Form", u"=", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_Mod.setText(QCoreApplication.translate("Form", u"%", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"7", None))
#if QT_CONFIG(tooltip)
        self.pushButton_Add.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt; color:#55ffff;\">+</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_Add.setText(QCoreApplication.translate("Form", u"+", None))
#if QT_CONFIG(shortcut)
        self.pushButton_Add.setShortcut(QCoreApplication.translate("Form", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_Sub.setText(QCoreApplication.translate("Form", u"-", None))
        self.pushButton_Mul.setText(QCoreApplication.translate("Form", u"x", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_Clear.setText(QCoreApplication.translate("Form", u"\u24b8", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u" 0", None))
    # retranslateUi

