import pyautogui



print(pyautogui.position())

pyautogui.screenshot('7.png', region=(1165, 472, 30, 30))

num7 = pyautogui.locateCenterOnScreen('7.png')

pyautogui.click(num7)
