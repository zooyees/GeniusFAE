import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['GeniusFAE.ico','themes/']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="GeniusFAE.ico"
)

# SETUP CX FREEZE
setup(
    name = "GeniusFAE",
    version = "1.0",
    description = "FAE support system.",
    author = "WindLink",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)
