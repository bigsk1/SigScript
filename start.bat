@echo off

if not exist "%~dp0venv" (
    echo Creating virtual environment...
    python -m venv %~dp0venv
) else (
    echo Virtual environment found.
)

echo Activating virtual environment...
call %~dp0venv\Scripts\activate

echo Installing required packages...
pip install pillow opencv-python

echo Running the script...
python %~dp0scripts\signature.py

echo Script completed. Press any key to exit.
pause

