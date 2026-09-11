from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, Key
import threading
import time

mouse = Controller()
clicking = False
running = True

def click_loop():
    """循环点击，直到 clicking 被设为 False"""
    global clicking
    while running:
        if clicking:
            mouse.click(Button.left, 1)  # 点击左键一次
            time.sleep(0.01)  # 每0.1秒点击一次（可调）
        else:
            time.sleep(0.01)  # 暂停时轻微休眠，减少CPU占用


def on_press(key):
    global clicking, running
    if key == Key.f6:          # F6 切换开关
        clicking = not clicking
        status = "启动" if clicking else "暂停"
        print(f"自动点击已{status}")
    elif key == Key.esc:       # ESC 退出
        running = False
        return False  # 停止键盘监听

# 启动点击线程（后台运行）
thread = threading.Thread(target=click_loop, daemon=True)
thread.start()

# 启动键盘监听（阻塞主线程）
with Listener(on_press=on_press) as listener:
    listener.join()