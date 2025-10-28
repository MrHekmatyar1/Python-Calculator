# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 500)
        MainWindow.setMinimumSize(QSize(300, 500))
        icon = QIcon()
        icon.addFile(u":/icons/calculate_24dp_D9D9D9_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"  color: white;\n"
"  background-color: #121212;\n"
"  font-family: Rubik;\n"
"  font-size: 16pt;\n"
"  font-weight: 600;\n"
"}\n"
"\n"
"QPushButton {\n"
"  Backround-color: transparent;\n"
"  border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: #888;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl = QLabel(self.centralwidget)
        self.lbl.setObjectName(u"lbl")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl.sizePolicy().hasHeightForWidth())
        self.lbl.setSizePolicy(sizePolicy)
        self.lbl.setStyleSheet(u"color: #888;")
        self.lbl.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.lbl)

        self.le = QLineEdit(self.centralwidget)
        self.le.setObjectName(u"le")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le.sizePolicy().hasHeightForWidth())
        self.le.setSizePolicy(sizePolicy1)
        self.le.setStyleSheet(u"font-size:40pt;\n"
"border:none;")
        self.le.setMaxLength(100)
        self.le.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.le.setReadOnly(True)

        self.verticalLayout.addWidget(self.le)

        self.Layout_buttons = QGridLayout()
        self.Layout_buttons.setObjectName(u"Layout_buttons")
        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy2)
        self.btn_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.Layout_buttons.addWidget(self.btn_2, 6, 1, 1, 1)

        self.btn_div = QPushButton(self.centralwidget)
        self.btn_div.setObjectName(u"btn_div")
        sizePolicy2.setHeightForWidth(self.btn_div.sizePolicy().hasHeightForWidth())
        self.btn_div.setSizePolicy(sizePolicy2)
        self.btn_div.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.Layout_buttons.addWidget(self.btn_div, 0, 3, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy2.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy2)
        self.btn_8.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.Layout_buttons.addWidget(self.btn_8, 4, 1, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy2.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy2)
        self.btn_6.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.Layout_buttons.addWidget(self.btn_6, 5, 2, 1, 1)

        self.btn_sub = QPushButton(self.centralwidget)
        self.btn_sub.setObjectName(u"btn_sub")
        sizePolicy2.setHeightForWidth(self.btn_sub.sizePolicy().hasHeightForWidth())
        self.btn_sub.setSizePolicy(sizePolicy2)
        self.btn_sub.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.Layout_buttons.addWidget(self.btn_sub, 8, 3, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy2.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy2)
        self.btn_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.Layout_buttons.addWidget(self.btn_4, 5, 0, 1, 1)

        self.btn_point = QPushButton(self.centralwidget)
        self.btn_point.setObjectName(u"btn_point")
        sizePolicy2.setHeightForWidth(self.btn_point.sizePolicy().hasHeightForWidth())
        self.btn_point.setSizePolicy(sizePolicy2)
        self.btn_point.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.Layout_buttons.addWidget(self.btn_point, 8, 2, 1, 1)

        self.btn_c = QPushButton(self.centralwidget)
        self.btn_c.setObjectName(u"btn_c")
        sizePolicy2.setHeightForWidth(self.btn_c.sizePolicy().hasHeightForWidth())
        self.btn_c.setSizePolicy(sizePolicy2)
        self.btn_c.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.Layout_buttons.addWidget(self.btn_c, 0, 0, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy2.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy2)
        self.btn_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.Layout_buttons.addWidget(self.btn_1, 6, 0, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy2.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy2)
        self.btn_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.Layout_buttons.addWidget(self.btn_3, 6, 2, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy2.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy2)
        self.btn_9.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.Layout_buttons.addWidget(self.btn_9, 4, 2, 1, 1)

        self.btn_ce = QPushButton(self.centralwidget)
        self.btn_ce.setObjectName(u"btn_ce")
        sizePolicy2.setHeightForWidth(self.btn_ce.sizePolicy().hasHeightForWidth())
        self.btn_ce.setSizePolicy(sizePolicy2)
        self.btn_ce.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.Layout_buttons.addWidget(self.btn_ce, 0, 1, 1, 1)

        self.btn_plus = QPushButton(self.centralwidget)
        self.btn_plus.setObjectName(u"btn_plus")
        sizePolicy2.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy2)
        self.btn_plus.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.Layout_buttons.addWidget(self.btn_plus, 6, 3, 1, 1)

        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy2.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy2)
        self.btn_0.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.Layout_buttons.addWidget(self.btn_0, 8, 1, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy2.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy2)
        self.btn_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.Layout_buttons.addWidget(self.btn_5, 5, 1, 1, 1)

        self.btn_del = QPushButton(self.centralwidget)
        self.btn_del.setObjectName(u"btn_del")
        sizePolicy2.setHeightForWidth(self.btn_del.sizePolicy().hasHeightForWidth())
        self.btn_del.setSizePolicy(sizePolicy2)
        self.btn_del.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/backspace_24dp_D9D9D9_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_del.setIcon(icon1)
        self.btn_del.setIconSize(QSize(26, 26))
#if QT_CONFIG(shortcut)
        self.btn_del.setShortcut(u"Backspace")
#endif // QT_CONFIG(shortcut)

        self.Layout_buttons.addWidget(self.btn_del, 0, 2, 1, 1)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy2.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy2)
        self.btn_7.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.Layout_buttons.addWidget(self.btn_7, 4, 0, 1, 1)

        self.btn_plusmin = QPushButton(self.centralwidget)
        self.btn_plusmin.setObjectName(u"btn_plusmin")
        sizePolicy2.setHeightForWidth(self.btn_plusmin.sizePolicy().hasHeightForWidth())
        self.btn_plusmin.setSizePolicy(sizePolicy2)
        self.btn_plusmin.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.Layout_buttons.addWidget(self.btn_plusmin, 8, 0, 1, 1)

        self.btn_neg = QPushButton(self.centralwidget)
        self.btn_neg.setObjectName(u"btn_neg")
        sizePolicy2.setHeightForWidth(self.btn_neg.sizePolicy().hasHeightForWidth())
        self.btn_neg.setSizePolicy(sizePolicy2)
        self.btn_neg.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.Layout_buttons.addWidget(self.btn_neg, 5, 3, 1, 1)

        self.btn_mul = QPushButton(self.centralwidget)
        self.btn_mul.setObjectName(u"btn_mul")
        sizePolicy2.setHeightForWidth(self.btn_mul.sizePolicy().hasHeightForWidth())
        self.btn_mul.setSizePolicy(sizePolicy2)
        self.btn_mul.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.Layout_buttons.addWidget(self.btn_mul, 4, 3, 1, 1)


        self.verticalLayout.addLayout(self.Layout_buttons)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"calculator", None))
        self.lbl.setText("")
        self.le.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.btn_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.btn_div.setText(QCoreApplication.translate("MainWindow", u"/", None))
#if QT_CONFIG(shortcut)
        self.btn_div.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.btn_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.btn_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.btn_sub.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)
        self.btn_sub.setShortcut(QCoreApplication.translate("MainWindow", u"=", None))
#endif // QT_CONFIG(shortcut)
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.btn_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.btn_point.setText(QCoreApplication.translate("MainWindow", u".", None))
#if QT_CONFIG(shortcut)
        self.btn_point.setShortcut(QCoreApplication.translate("MainWindow", u".", None))
#endif // QT_CONFIG(shortcut)
        self.btn_c.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.btn_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.btn_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.btn_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.btn_ce.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.btn_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.btn_plus.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.btn_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.btn_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.btn_del.setText("")
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.btn_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.btn_plusmin.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
#if QT_CONFIG(shortcut)
        self.btn_plusmin.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.btn_neg.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.btn_neg.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.btn_mul.setText(QCoreApplication.translate("MainWindow", u"*", None))
#if QT_CONFIG(shortcut)
        self.btn_mul.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

