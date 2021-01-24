import pyautogui as pag
import keyboard
import time

while True:
    if keyboard.is_pressed('F4'):
        t1 = pag.position()
        print(t1)
        time.sleep(0.5)
        break
while True:
    if keyboard.is_pressed('F4'):
        t2 = pag.position()
        print(t2)
        time.sleep(0.5)
        break
while True:
    if keyboard.is_pressed('F4'):
        f1 = pag.position()
        print(f1)
        time.sleep(0.5)
        break
while True:
    if keyboard.is_pressed('F4'):
        f2 = pag.position()
        print(f2)
        time.sleep(0.5)
        break

region1 = (t1[0], t1[1], t2[0]-t1[0], t2[1]-t1[1])
pag.screenshot('C:/temp/find.png', region = region1)

p_list = pag.locateAllOnScreen('C:/temp/find.png', confidence = 0.9)
p_list = list(p_list)
if len(p_list) == 0:
    print("이미지 없음")
else:
    for p in p_list:
    pag.moveTo(pag.center(p))
    time.sleep(1)