import pyautogui
import time

# 按下 Alt + F2 打开运行窗口
def linuxOpen():
    pyautogui.hotkey('alt', 'f2')
    
    time.sleep(1)
    
    # 输入应用程序名称，例如 "gnome-terminal" 打开终端
    
    pyautogui.write('chrome')
    
    time.sleep(1)

    # 按下回车键打开应用程序
    pyautogui.press('enter')

def winOpen():
    pyautogui.hotkey('win', 'r')
    
    time.sleep(1)
    
    # 输入应用程序名称，例如 "gnome-terminal" 打开终端
    
    pyautogui.write('chrome')
    
    time.sleep(1)

    
    # 按下回车键打开应用程序
    
    pyautogui.press('enter')


def typeAddress(site):
    pyautogui.hotkey('alt','d')
    pyautogui.write(site)
    pyautogui.press('enter')
    pyautogui.press('enter')
