import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico','themes/']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "WindLink",
    version = "1.0",
    description = "Charging Protocol Analyzer",
    author = "WindLink",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)
