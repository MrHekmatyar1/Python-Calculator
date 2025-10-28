import sys
from typing import Union, Optional
from operator import add, sub, mul, truediv
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QFontDatabase
from design import Ui_MainWindow

operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
}


class Calculator(QMainWindow):
    def __init__(self) -> None:
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.le.setReadOnly(False)
        QFontDatabase.addApplicationFont("fonts/Rubik-Regular.ttf")

        #digit
        self.ui.btn_0.clicked.connect(lambda: self.add_digit('0'))
        self.ui.btn_1.clicked.connect(lambda: self.add_digit('1'))
        self.ui.btn_2.clicked.connect(lambda: self.add_digit('2'))
        self.ui.btn_3.clicked.connect(lambda: self.add_digit('3'))
        self.ui.btn_4.clicked.connect(lambda: self.add_digit('4'))
        self.ui.btn_5.clicked.connect(lambda: self.add_digit('5'))
        self.ui.btn_6.clicked.connect(lambda: self.add_digit('6'))
        self.ui.btn_7.clicked.connect(lambda: self.add_digit('7'))
        self.ui.btn_8.clicked.connect(lambda: self.add_digit('8'))
        self.ui.btn_9.clicked.connect(lambda: self.add_digit('9'))

        # action

        self.ui.btn_c.clicked.connect(self.clear_all)
        self.ui.btn_ce.clicked.connect(self.clear_entry)
        self.ui.btn_point.clicked.connect(self.add_point)

        # math
        self.ui.btn_sub.clicked.connect(self.calculate)
        self.ui.btn_plus.clicked.connect(lambda: self.add_temp('+'))
        self.ui.btn_neg.clicked.connect(lambda: self.add_temp('-'))
        self.ui.btn_mul.clicked.connect(lambda: self.add_temp('*'))
        self.ui.btn_div.clicked.connect(lambda: self.add_temp('/'))


    def add_digit(self, btn_text: str) -> None:
        # print(f"нашел кнопку: {btn_text}")
        if self.ui.le.text() == '0':
            self.ui.le.setText(btn_text)
        else:
            self.ui.le.setText(self.ui.le.text() + btn_text)


    def clear_all(self) -> None:
        self.ui.le.setText('0')
        self.ui.lbl.clear()

    def clear_entry(self) -> None:
        self.ui.le.setText('0')

    def add_point(self, btn_text: str) -> None:
        if '.' not in self.ui.le.text():
            self.ui.le.setText(self.ui.le.text() + '.')

    @staticmethod
    def remove_trailing_zeros(num: str) -> str:
        n = str(float(num))
        return n[:-2] if n[-2:] == '.0' else n

    def add_temp(self, math_sing: str):
        if not self.ui.lbl.text() or self.get_math_sign() == '=':
            self.ui.lbl.setText(self.remove_trailing_zeros(self.ui.le.text()) + f' {math_sing} ')
            self.ui.le.setText('0')

    def get_entry_num(self) -> Union[int, float]:
        entry = self.ui.le.text().strip('.')

        return float(entry) if '.' in entry else int(entry)

    def get_temp_num(self) -> Union[int, float, None]:
        if self.ui.lbl.text():
            temp = self.ui.lbl.text().strip('.').split()[0]
            return float(temp) if '.' in temp else int(temp)

    def get_math_sign(self) -> Optional[str]:
        if self.ui.lbl.text():
            return self.ui.lbl.text().strip('.').split()[-1]

    def calculate(self) -> Optional[str]:
        entry = self.ui.le.text()
        temp = self.ui.lbl.text()

        if temp:
            result = self.remove_trailing_zeros(
                str(operations[self.get_math_sign()](self.get_temp_num(), self.get_entry_num()))
            )
            self.ui.lbl.setText(temp + self.remove_trailing_zeros(entry) + ' =')
            self.ui.le.setText(result)
            return result

    def math_operation(self, math_sign: str):
        temp = self.ui.lbl.text()

        if not temp:
            self.add_temp(math_sign)
        else:
            if self.get_math_sign() != math_sign:
                if self.get_math_sign() == '=':
                    self.add_temp(math_sign)
                else:
                    self.ui.lbl.setText(temp[:-2] + f' {math_sign} ')
            else:
                self.ui.lbl.setText(self.calculate() + f' {math_sign} ')

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec())








