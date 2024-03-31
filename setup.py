import sys
from cx_Freeze import setup, Executable
from Game import VERSION, TITLE

build_exe_options = {
    "excludes": ['tkinter', 'unittest'],
    "zip_include_packages": ['PyQt6']
}

setup(
    name=TITLE,
    version=VERSION,
    options={'build_exe':build_exe_options},
    executables=[Executable('Game.py')]
)