from modules import clipboard_to_item_advanced
from time import sleep
import pyautogui
import clipboard


def copy_to_clipboard():
    pyautogui.hotkey('ctrl', 'altleft', 'c')
    return clipboard.paste()


sleep(1)

print(clipboard_to_item_advanced(copy_to_clipboard()))