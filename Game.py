# ИМПОРТ МОДУЛЕЙ
# -----------------
# импорт фреймворка
from PyQt6.QtCore import *
from PyQt6.QtGui import * 
from PyQt6.QtWidgets import *

# импорт прочих модулей
import icecream as ic # для логирования переменных
import cryptography as crypt # для шифрования данных
from tqdm.auto import tqdm # для отслеживания прогресса выполнения кода
import sys
import json # работа с файлом настроек игры

# ФУНКЦИИ
# ------------------
# функция шифрования

# КЛАССЫ
# ----------------------------------
# Класс управления файлами в системе
class FileManager:
    def __init__(self):
        self._example_player = {
            'nickname': None,
            'points': 0,
        }
    
    def load_save(self):
        pass

# Класс игрока
class Player:
    def __init__(self):
        self.name = ''
        self.points = 1

# Класс приложения(должен быть самым нижним, так как в нём будет вся расставка выше приготовленного фарша)
class App(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.change_theme()

    def change_theme(self):
        theme = 'dark_theme.qss'
        with open(theme) as file_theme:
            self.setStyleSheet(file_theme.read())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    game = App()
    game.show()

    sys.exit(app.exec())
