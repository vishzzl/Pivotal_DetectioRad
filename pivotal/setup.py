import sys

from cx_Freeze import setup, Executable

setup( name = "pivotal", version = "1.0",

       description = "detectionRad",

       executables = [Executable("start_gui.py", base = "Win32GUI")])
