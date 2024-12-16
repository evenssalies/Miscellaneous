:: This script is used to run a python script as an executable
:: 1) Install pyinstaller
::      pip install pyinstaller
:: 
:: 2) Execute this from the cmd prompt to run a python script as an executable
::      call "C:\Users\evens\OneDrive\GitHub\Miscellaneous\pyexecutable.cmd"
pyinstaller --onefile my_script.py
:: The --onefile option tells PyInstaller to bundle everything into a single executable file
:: After running the command, PyInstaller will create a dist directory in your project folder. Inside this directory
::  I'll find the standalone executable file in dist
exit /b