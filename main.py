import pymysql
from config import host, user, port, password, db_name
import sys
from PyQt5.Qt import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QLabel, QPushButton
from PyQt5 import uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./UI/sing_in_ui.ui', self)

        self.sing_in_btn.clicked.connect(self.sing_in_fnc)
        self.register_btn.clicked.connect(self.reg_fnc)
        self.sing_in_admin_btn.clicked.connect(self.sing_in_admin_fnc)
        self.email_edit.textChanged.connect(self.email_edit_ch)
        self.password_edit.textChanged.connect(self.password_edit_ch)

    def email_edit_ch(self):
        if 'Введите E-mail' in self.email_edit.text():
            self.email_edit.setText(self.email_edit.text()[-1])

    def password_edit_ch(self):
        if 'Введите пароль' in self.password_edit.text():
            self.password_edit.setText(self.password_edit.text()[-1])
            self.password_edit.setEchoMode(2)

    def sing_in_admin_fnc(self):
        ex.close()
        self.admin_sing_in = Admin_sing_in()
        self.admin_sing_in.show()

    def reg_fnc(self):
        self.reg_ui = Register_UI()
        self.reg_ui.show()
        ex.close()

    def sing_in_fnc(self):
        self.email_txt = self.email_edit.text()
        self.password_txt = self.password_edit.text()
        with con.cursor() as cur:
            cur.execute(f'SELECT * FROM org WHERE email = "{self.email_txt}" AND password = "{self.password_txt}"')
            res = cur.fetchall()
            if res:
                self.res = list(res[0])
            else:
                def ok_fnc():
                    dialog.close()
                    self.email_edit.setText('')
                    self.password_edit.setText('')

                dialog = QDialog()
                dialog.setWindowTitle('Неверные данные')
                dialog.setGeometry(400, 200, 695, 150)
                er_lb = QLabel(dialog)
                er_lb.setText('Упс... Похоже, данные введены неверно или организации с такими данными не существует')
                er_lb.setFont((QFont('GillSanss', 12)))
                er_lb.move(10, 30)
                ok_btn = QPushButton(dialog)
                ok_btn.setText('OK')
                ok_btn.setStyleSheet('QPushButton {color: "white"; background: rgb(0, 112, 186);'
                                     ' border: 2px solid rgb(0, 112, 186); '
                                     'border-radius: 10px} '
                                     'QPushButton:pressed {background: rgb(0, 82, 156); '
                                     'border: 2px solid rgb(0, 82, 156)}')
                ok_btn.setFont(QFont('GillSanss', 12))
                ok_btn.move(340, 100)
                ok_btn.clicked.connect(ok_fnc)

                dialog.exec_()



class Register_UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./UI/reg_ui.ui', self)

        self.reg_btn.clicked.connect(self.reg_fnc)
        self.org_name_edit.textChanged.connect(self.org_name_edit_ch)
        self.org_inn_edit.textChanged.connect(self.org_inn_edit_ch)
        self.org_email_edit.textChanged.connect(self.org_email_edit_ch)
        self.org_password_edit.textChanged.connect(self.org_password_edit_ch)
        self.org_fio_edit.textChanged.connect(self.org_fio_edit_ch)
        self.org_number_edit.textChanged.connect(self.org_number_edit_ch)

    def org_name_edit_ch(self):
        if 'Введите наименование организации' in self.org_name_edit.text():
            self.org_name_edit.setText(self.org_name_edit.text()[-1])

    def org_inn_edit_ch(self):
        if 'Введите ИНН организации' in self.org_inn_edit.text():
            self.org_inn_edit.setText(self.org_inn_edit.text()[-1])

    def org_email_edit_ch(self):
        if 'Введите E-mail организации' in self.org_email_edit.text():
            self.org_email_edit.setText(self.org_email_edit.text()[-1])

    def org_password_edit_ch(self):
        if 'Введите пароль организации' in self.org_password_edit.text():
            self.org_password_edit.setText(self.org_password_edit.text()[-1])
            self.org_password_edit.setEchoMode(2)

    def org_fio_edit_ch(self):
        if 'Введите ФИО куратора организации' in self.org_fio_edit.text():
            self.org_fio_edit.setText(self.org_fio_edit.text()[-1])

    def org_number_edit_ch(self):
        if 'Введите номер телефона куратора организации' in self.org_number_edit.text():
            self.org_number_edit.setText(self.org_number_edit.text()[-1])

    def reg_fnc(self):
        with con.cursor() as cur:
            try:
                cur.execute(f'INSERT INTO `org` (name) VALUES ("{self.org_name_edit.text()}")')
                cur.execute(f'UPDATE `org` SET inn = "{self.org_inn_edit.text()}" WHERE name = "{self.org_name_edit.text()}"')
                cur.execute(f'UPDATE `org` SET email = "{self.org_email_edit.text()}" WHERE name = "{self.org_name_edit.text()}"')
                cur.execute(f'UPDATE `org` SET password = "{self.org_password_edit.text()}" WHERE name = "{self.org_name_edit.text()}"')
                cur.execute(f'UPDATE `org` SET fio = "{self.org_fio_edit.text()}" WHERE name = "{self.org_name_edit.text()}"')
                cur.execute(f'UPDATE `org` SET number = "{self.org_number_edit.text()}" WHERE name = "{self.org_name_edit.text()}"')
                con.commit()
            except Exception as eee:
                print(eee)


class Admin_sing_in(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./UI/admin_sing_in_ui.ui', self)

        self.sing_in_admin_btn.clicked.connect(self.sing_in_admin_fnc)
        self.back_btn.clicked.connect(self.back_fnc)
        self.admin_email_edit.textChanged.connect(self.email_edit_ch)
        self.admin_password_edit.textChanged.connect(self.password_edit_ch)

    def email_edit_ch(self):
        if 'Введите E-mail' in self.admin_email_edit.text():
            self.admin_email_edit.setText(self.admin_email_edit.text()[-1])

    def password_edit_ch(self):
        if 'Введите пароль' in self.admin_password_edit.text():
            self.admin_password_edit.setText(self.admin_password_edit.text()[-1])
            self.admin_password_edit.setEchoMode(2)

    def back_fnc(self):
        ex.admin_sing_in.close()
        ex.show()

    def sing_in_admin_fnc(self):
        with con.cursor() as cur:
            cur.execute(
                f'SELECT email, password, fio FROM admins WHERE email = "{self.admin_email_edit.text()}" '
                f'AND password = "{self.admin_password_edit.text()}"'
            )
            res = cur.fetchall()
            if res:
                self.res = list(res[0])
                ex.admin_sing_in.close()
                self.admin_work = Admin_work_place()
                self.admin_work.show()
            else:
                def ok_fnc():
                    dialog.close()
                    self.admin_email_edit.setText('')
                    self.admin_password_edit.setText('')

                dialog = QDialog()
                dialog.setWindowTitle('Неверные данные')
                dialog.setGeometry(400, 200, 685, 150)
                er_lb = QLabel(dialog)
                er_lb.setText('Упс... Похоже, данные введены неверно или сотрудника с такими данными не существует')
                er_lb.setFont((QFont('GillSanss', 12)))
                er_lb.move(10, 30)
                ok_btn = QPushButton(dialog)
                ok_btn.setText('OK')
                ok_btn.setStyleSheet('QPushButton {color: "white"; background: rgb(0, 112, 186);'
                                     ' border: 2px solid rgb(0, 112, 186); '
                                     'border-radius: 10px} '
                                     'QPushButton:pressed {background: rgb(0, 82, 156); '
                                     'border: 2px solid rgb(0, 82, 156)}')
                ok_btn.setFont(QFont('GillSanss', 12))
                ok_btn.move(340, 100)
                ok_btn.clicked.connect(ok_fnc)

                dialog.exec_()


class Admin_work_place(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./UI/work_ui_admin_ui.ui', self)


if __name__ == '__main__':
    con = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=db_name,
    )
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
