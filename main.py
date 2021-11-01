import pyautogui
import clipboard
import keyboard
from time import sleep
from modules import clipboard_to_item, clipboard_to_item_advanced
import numpy as np

# mature
# meticulous

sleep_time = 0.15
errors = 0


def copy_to_clipboard():
    pyautogui.hotkey('ctrl', 'altleft', 'c')
    return clipboard.paste()


target_prefixes = [{'name': 'mature', 'tier': 1, "description": 'NA'},
                   {'name': 'meticulous', 'tier': 1, "description": 'NA'},
                   {'name': 'emblematic', 'tier': 1, "description": 'NA'}]
#target_prefixes = [{'name': "NA", 'tier': 10, "description": 'born of'}]
#target_suffixes = [{'name': 'of many', 'tier': 1}]
target_suffixes = []

print(f"I will look for target_prefixes: {target_prefixes} and target_suffixes: {target_suffixes}")
print()

print("Click your Path of Exile client")
print()

print(f"Press space over Orb of Alteration")
while True:
    if keyboard.is_pressed("space"):
        altX, altY = pyautogui.position()
        cb = copy_to_clipboard()
        item, amount = clipboard_to_item(cb)
        if item == "Orb of Alteration":
            altN = amount
            print()
            print(f"Your {altN} Orb of Alteration are located at: ({altX}, {altY})")
            break
        else:
            errors += 1
            if errors > 5:
                quit()
            print()
            print("Try again, make sure you have clicked the Path of Exile window.")

sleep(sleep_time)

print()
print(f"Press space over Orb of Augmentation")
while True:
    if keyboard.is_pressed("space"):
        augX, augY = pyautogui.position()
        cb = copy_to_clipboard()
        item, amount = clipboard_to_item(cb)
        if item == "Orb of Augmentation":
            augN = amount
            print()
            print(f"Your {augN} Orb of Augmentation are located at: ({augX}, {augY})")
            break
        else:
            errors += 1
            if errors > 5:
                quit()
            print()
            print("Try again, make sure you have clicked the Path of Exile window.")

sleep(sleep_time)

print()
print(f"Press space over the item to spam")
while True:
    if keyboard.is_pressed("space"):
        baseX, baseY = pyautogui.position()
        break

sleep(sleep_time)

pyautogui.PAUSE = sleep_time


def augment():
    pyautogui.keyUp('shift')
    pyautogui.moveTo(x=augX, y=augY)
    pyautogui.click(button='right')
    pyautogui.moveTo(baseX, baseY)
    pyautogui.click(x=baseX, y=baseY)
    pyautogui.moveTo(x=altX, y=altY)
    pyautogui.click(button='right')
    pyautogui.keyDown('shift')
    pyautogui.moveTo(baseX, baseY)


pyautogui.moveTo(x=altX, y=altY)
pyautogui.click(button='right')
pyautogui.keyDown('shift')

pyautogui.moveTo(baseX, baseY)

item_hit = False
just_augmented = False


print()
print(f"Hold pause to quit...")
print()

while not item_hit:
    if not just_augmented:
        pyautogui.click(x=baseX, y=baseY)
        altN -= 1

    sleep(np.random.random() / 2)

    just_augmented = False

    prefixes, suffixes = clipboard_to_item_advanced(copy_to_clipboard())

    if len(prefixes) != 0 and len(target_prefixes) != 0:
        for tp in target_prefixes:
            for p in prefixes:
                if (tp['name'] in p['name'] or tp['description'] in p['description']) and p['tier'] <= tp['tier']:
                    item_hit = True

    if len(suffixes) != 0 and len(target_suffixes) != 0:
        for ts in target_suffixes:
            for s in suffixes:
                if (ts['name'] in s['name'] or ts['description'] in s['description']) and s['tier'] <= ts['tier']:
                    item_hit = True

    if altN <= 0:
        print('out of alts')
        print()
        break

    if augN <= 0:
        print('out of augs')
        print()
        break

    if len(prefixes) == 0 and len(target_prefixes) != 0:
        augment()
        augN -= 1
        just_augmented = True

    if len(suffixes) == 0 and len(target_suffixes) != 0:
        augment()
        augN -= 1
        just_augmented = True

    if keyboard.is_pressed("pause"):
        break


if item_hit:
    print("gg")
else:
    print('see ya')

pyautogui.keyUp('shift')