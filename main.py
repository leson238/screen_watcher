import cv2
import pyautogui
import numpy as np
import winsound

tpl = cv2.imread("first_frame.png", cv2.COLOR_BGR2RGB)
h, w, _ = tpl.shape
frame = pyautogui.screenshot()
frame = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
res = cv2.matchTemplate(frame,tpl,cv2.TM_CCOEFF_NORMED)
_, _, _, maxLoc = cv2.minMaxLoc(res) 
x, y = maxLoc

while True:
    pyautogui.sleep(5)
    pyautogui.click(800,400)
    frame = pyautogui.screenshot(region=(x, y, w, h))
    frame = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)

    difference = cv2.subtract(frame, tpl)
    b, g, r = cv2.split(difference)

    if cv2.countNonZero(b) or cv2.countNonZero(g) or cv2.countNonZero(r):
        winsound.Beep(2500, 500)
    key = cv2.waitKey(1)
    cv2.imshow('capturing', frame)
    if key == ord('q'):
        break
