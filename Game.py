# ИМПОРТ МОДУЛЕЙ
# -----------------
# импорт фреймворка
from PyQt6.QtCore import *
from PyQt6.QtGui import * 
from PyQt6.QtWidgets import *

# импорт прочих модулей
from icecream import ic # для логирования переменных
import cryptography as crypt # для шифрования данных
from tqdm.auto import tqdm # для отслеживания прогресса выполнения кода
import sys 
import json # работа с файлом настроек игры
import win32api # для собирания каких-либо системных данных
import time # манипуляуции с временем
from datetime import datetime
import random

# Константы
TITLE = 'UNLIMIT CLICKS'
VERSION = '0.0.1'
UPDATE_THEME = False

# КЛАССЫ
# ----------------------------------
# Класс игрока(пока не ебу нужен он будет или нет)
class Player:
    def __init__(self):
        self.name = ''
        self.points = 1

# Класс приложения(должен быть самым нижним, так как в нём будет вся расставка выше приготовленного фарша)
class App(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.apply_settings() # применяем настройки окна
        self.player = Player() # суём в главный класс игрока

        # штучки для дебага
        self.change_theme() # применение каскадной таблицы стилей Qt

        self.thread_ = QThreadPool()


        self.start() # старт

    # начальное окно
    def start(self):
        self.central_widg = QWidget(self)
        
        label = QLabel(self.central_widg)
        label.setText(TITLE+' '+VERSION)
        label.setMaximumHeight(30)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.move(self.width()//2-label.width()//2, 0)

        self.label_money = QLabel(self.central_widg)
        self.label_money.setText(str(self.player.points))
        self.label_money.setFixedSize(100, 25)
        self.label_money.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_money.move(self.width()//2-self.label_money.width()//2, 20)

        self.list_smiles = [
            '(* ^ ω ^)',
            '(´ ∀ *)',
            '(o^▽^o)',
            '(⌒▽⌒)',
            '☆ヽ(・∀・)ﾉ',
            '(´｡• ω •｡)',
            '(o･ω･o)',
            '(＠＾◡＾)', 
            '(^人^)',
            '(o´▽o)',
            '(´ ω `)',
            '(((o(*°▽°*)o)))',
            '(´• ω •)', '(＾▽＾)', '╰(▔∀▔)╯', '(─‿─)', '(✯◡✯)', '(◕‿◕)', '(⌒‿⌒)', '(≧▽≦)', '(*°▽°*)', '٩(｡•́‿•̀｡)۶', '(´｡• ᵕ •｡)', '( ´ ▽ )', 'ヽ(>∀<☆)ノ', 'o(≧▽≦)o', '(￣▽￣)', '(*¯︶¯*)', '(o˘◡˘o)', '(★ω★)', '(╯✧▽✧)╯', 'o(>ω<)o', '( ‾́ ◡ ‾́ )', '(ﾉ´ヮ)ﾉ*: ･ﾟ', '(๑˘︶˘๑)', '( ˙꒳​˙ )', '(´･ᴗ･ )', '(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧'
        ]

        self.main_button = QPushButton(self.central_widg)
        self.main_button.setObjectName('MAIN_BUTTON')
        self.main_button.setText('Нажми на меня!')
        self.main_button.clicked.connect(self.income)
        self.main_button.resize(self.width()-10, 370)
        self.main_button.move(QPoint(5, 45))

        button_settings = QPushButton(self.central_widg)
        button_settings.setIcon(QIcon('data/files/icons/icons8-настройки.svg'))
        button_settings.resize(55, 55)
        button_settings.move(5, 420)
        
        button_upgrade = QPushButton(self.central_widg)
        button_upgrade.setIcon(QIcon('data/files/icons/icons8-улучшение.png'))
        button_upgrade.clicked.connect(self.open_upgrades)
        button_upgrade.resize(220, 55)
        button_upgrade.move(65, 420)
        
        button_about_us = QPushButton(self.central_widg)
        button_about_us.setIcon(QIcon('data/files/icons/flaticon-information-157933.png'))
        button_about_us.resize(55, 55)
        button_about_us.move(290, 420)

        self.setCentralWidget(self.central_widg)

    def open_upgrades(self):       
        self.animation_main_button = QPropertyAnimation(self.main_button, b'size')
        self.animation_main_button.setDuration(200)
        self.animation_button_upgrade_1 = QPropertyAnimation(self.main_button, b'size')
        self.animation_button_upgrade_1.setDuration(200)
        self.animation_button_upgrade_2 = QPropertyAnimation(self.main_button, b'size')
        self.animation_button_upgrade_2.setDuration(200)
        self.animation_button_upgrade_3 = QPropertyAnimation(self.main_button, b'size')
        self.animation_button_upgrade_3.setDuration(200)
        self.animation_button_upgrade_4 = QPropertyAnimation(self.main_button, b'size')
        self.animation_button_upgrade_4.setDuration(200)
        self.animation_button_upgrade_5 = QPropertyAnimation(self.main_button, b'size')
        self.animation_button_upgrade_5.setDuration(200)
        self.animation_button_upgrade_6 = QPropertyAnimation(self.main_button, b'size')
        self.animation_button_upgrade_6.setDuration(200)


        button_upgrade_1 = QPushButton(self.central_widg)
        button_upgrade_1.setText('Апгрейд 1')
        button_upgrade_1.resize(0, 0)
        button_upgrade_1.move(0, 0)

        button_upgrade_2 = QPushButton(self.central_widg)
        button_upgrade_2.setText('Апгрейд 2')
        button_upgrade_2.resize(0, 0)
        button_upgrade_2.move(0, 0)

        button_upgrade_3 = QPushButton(self.central_widg)
        button_upgrade_3.setText('Апгрейд 3')
        button_upgrade_3.resize(0, 0)
        button_upgrade_3.move(0, 0)

        button_upgrade_4 = QPushButton(self.central_widg)
        button_upgrade_4.setText('Апгрейд 4')
        button_upgrade_4.resize(0, 0)
        button_upgrade_4.move(0, 0)

        button_upgrade_5 = QPushButton(self.central_widg)
        button_upgrade_5.setText('Апгрейд 5')
        button_upgrade_5.resize(0, 0)
        button_upgrade_5.move(0, 0)

        button_upgrade_6 = QPushButton(self.central_widg)
        button_upgrade_6.setText('Апгрейд 6')
        button_upgrade_6.resize(0, 0)
        button_upgrade_6.move(0, 0)

        if self.main_button.height() > 45:
            self.animation_main_button.setEndValue(QSize(self.width()-10, 40))
            self.animation_main_button.setEndValue(QSize(self.width()-10, 40))
            self.animation_main_button.setEndValue(QSize(self.width()-10, 40))
            self.animation_main_button.setEndValue(QSize(self.width()-10, 40))
            self.animation_main_button.setEndValue(QSize(self.width()-10, 40))
            self.animation_main_button.setEndValue(QSize(self.width()-10, 40))
            self.animation_main_button.setEndValue(QSize(self.width()-10, 40))


        else:
            self.animation.setEndValue(QSize(self.width()-10, 370))


        

    def income(self):
        self.player.points += 1
        self.main_button.setText(random.choice(self.list_smiles))
        self.label_money.setText(str(self.player.points))


    def apply_settings(self):
        self.setFixedSize(350, 480)
        self.setWindowTitle(TITLE)

    def change_theme(self):
        theme = 'data/style/theme.qss' # располо
        try:
            with open(theme) as file_theme:
                self.setStyleSheet(file_theme.read())
        except FileNotFoundError:
            pass
        finally:
            print(f'тема применена {datetime.now()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    game = App()
    game.show()

    sys.exit(app.exec())
