import pyautogui
import clipboard
import keyboard
from time import sleep
from modules import clipboard_to_item, clipboard_to_item_adv


sleep_time = 0.15
errors = 0


def copy_to_clipboard():
    pyautogui.hotkey('ctrl', 'altleft', 'c')
    return clipboard.paste()


print("Type desired prefixes. If none or when done, press enter to continue.")
print()
prefixes = []
x = input()

while x != "":
    prefixes.append(x.lower())
    x = input()

print()
print("Type desired prefixes. If none or when done, press enter to continue.")
print()
suffixes = []
x = input()

while x != "":
    suffixes.append(x.lower())
    x = input()

print()
print(f"I will look for prefixes: {prefixes} and suffixes: {suffixes}")
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

    just_augmented = False
    prefix, suffix = clipboard_to_item_adv(copy_to_clipboard())

    if prefix is not None and len(prefixes) != 0:
        for p in prefixes:
            if p in prefix:
                item_hit = True

    if suffix is not None and len(suffixes) != 0:
        for s in suffixes:
            if s in suffix:
                item_hit = True

    if altN <= 0:
        print('out of alts')
        print()
        break

    if augN <= 0:
        print('out of augs')
        print()
        break

    if prefix is None and len(prefixes) != 0:
        augment()
        augN -= 1
        just_augmented = True

    if suffix is None and len(suffixes) != 0:
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