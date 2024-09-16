@echo off
echo Installing required Python packages...

REM 检查是否安装了pip，如果没有安装，提示用户安装
python -m ensurepip --default-pip
pip install --upgrade pip

REM 安装所需的 Python 包
pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple pyautogui pyperclip pillow opencv-python

echo Packages installed successfully.
echo Running Python scripts...

REM 运行你的 Python 脚本
python "autoNext.py"

pause
