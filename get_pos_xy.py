"""
    获取 窗口内坐标
"""
import win32gui
import win32ui
import win32con
import win32api
import time


def  findTitle(window_title):
    hWndList = []

    # 枚举所有屏幕上顶层窗口, 获取全部窗口 hwnd 窗口句柄
    win32gui.EnumWindows(lambda hWnd, param:param.append(hWnd), hWndList)
    print("hWndList" , hWndList)
    for hwnd in hWndList:
        
        # 根据窗口句柄获取标题
        title = win32gui.GetWindowText(hwnd)
        print("title:", title, "wid:", hwnd)
        if (title == window_title):
            print("title:", title, "wid:", hwnd)
            break
    return hwnd

window_title = u'乀小火柴【2017】一线 问道(1.721.210924)'
hwnd = findTitle(window_title)

def show_pos():
    while True:
        # 获取前台鼠标位置
        p = win32api.GetCursorPos()
        print(p[0], p[1])
        # 获取窗口内范围矩阵
        x, y, w, h = win32gui.GetWindowRect(hwnd)

        # 减去窗口内范围矩阵
        pos_x = p[0] - x
        pos_y = p[1] - y
        print(pos_x, pos_y)
        time.sleep(0.5)
