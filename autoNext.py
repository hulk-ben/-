import platform
import time

import pyautogui
import pyperclip

import openBrowser
import ovr


def copyText(x1, y1, x2, y2):
    pyautogui.moveTo(x1, y1)
    pyautogui.dragTo(x2, y2, 2, tween=pyautogui.easeOutQuad)
    pyautogui.hotkey('ctrl', 'c')
    # 从剪切板读取内容
    clipboard_content = pyperclip.paste()
    print(f"clipboard content is {clipboard_content}")
    pyautogui.moveTo(500,500)
    return clipboard_content

def clickNext():
    a = 0
    while a != 100:
        try:
            pyautogui.moveTo(500,500)
            ovr.getSite('images/next.png')
            a = 100
        except pyautogui.ImageNotFoundException:
            a = a + 1
            if a == 10:
                choose = pyautogui.confirm(text='识别不到按钮，请检查页面', title='警告', buttons=['确认', '取消'])
                if choose == "取消":
                    raise SystemExit("用户退出")
            print("没有识别到对话框")
    time.sleep(1)
    pyautogui.click()
    print("点击下一节")


def exitFullScreen():
    #退出全屏
    pyautogui.moveTo(500, 700, 3, pyautogui.easeOutQuad)
    time.sleep(1)
    pyautogui.doubleClick()



def skipConfirm():
    a = 0
    while a != 100:
        try:
            pyautogui.moveTo(500'k'pskp
            ovr.getSite("images/conversition.png",165,80)
            a = 100
        except pyautogui.ImageNotFoundException:
            a = a + 1
            if a == 10:
                choose = pyautogui.confirm(text='识别不到按钮，请检查页面', title='警告', buttons=['确认', '取消'])
                if choose == "取消":
                    raise SystemExit("用户退出")
            # pyautogui.moveTo(1073, 937, 3, pyautogui.easeOutQuad)
            print("没有识别到对话框")

    time.sleep(1)
    pyautogui.click()

    print("跳过对话框")

def main():
    systemType = platform.system()

    pyautogui.PAUSE = 1
    SCREENX,SCREENY = 1920,1080
    screenX,screenY = pyautogui.size()
    if screenX != SCREENX or screenY != SCREENY:
        print(screenX,screenY)
        pyautogui.alert("设备分辨率不匹配")
        raise SystemExit("设备屏幕分辨率不匹配，如有需要请找作者")


    itimes = int(pyautogui.prompt(text='请输入要看几集，请输入正整数,运行期间请勿操作', title='自动刷课', default='1'))

    pyautogui.hotkey('win', 'd')
    if systemType == "Linux":
        openBrowser.linuxOpen()
        time.sleep(5)
        openBrowser.typeAddress("https://i.chaoxing.com/base")
    elif systemType == "Windows":
        openBrowser.winOpen()
        time.sleep(5)
        openBrowser.typeAddress("https://i.chaoxing.com/base")
    else:
        pyautogui.alert("系统不匹配")
        raise SystemExit("系统不匹配请联系作者")
    choose = pyautogui.confirm(text='请打开课程的视频页面，然后点击确认', title='准备开始', buttons=['确认', '取消'])

    if choose != '确认':
        raise SystemExit("用户取消")



    i = 1
    for i in range(itimes):

        # 播放视频
        try:
            ovr.getSite("images/play.png")
        except pyautogui.ImageNotFoundException:
            print("图片识别失败")

        pyautogui.click()
        time.sleep(2)
        pyautogui.doubleClick()

        # 解析时间
        videoTime = copyText(139, 1047, 180, 1047)
        # 计算时间为秒
        if videoTime and ':' in videoTime:
            minutes, seconds = map(int, videoTime.split(":"))
            waitTime = minutes * 60 + seconds + 1  # 等待时间是视频时长加1秒
        else:
            print("获取时间失败")
            waitTime = 60 * 20  # 默认等待20分钟
        # waitTime=5 #用来测试的变量
        print(f"播放时间为：{waitTime}秒")
        time.sleep(2)
        exitFullScreen()
        time.sleep(waitTime)  # 休眠视频时长

        pyautogui.scroll(-200)
        pyautogui.scroll(-200)
        clickNext()
        pyautogui.scroll(-800)
        time.sleep(2)
        pyautogui.scroll(-800)
        time.sleep(2)
        pyautogui.scroll(-800)

        #没有章节测试可以删除
        clickNext()
        skipConfirm() 

        i += 1

if __name__ == "__main__":
    main()
