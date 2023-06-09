import pyautogui as pt
import time

limit = 100
message = "Eh mafi wenn goemmer?"
i = 0
time.sleep(5)

while i < limit:
    pt.typewrite(message)
    # the message is written where -
    # the cursor belongs
    time.sleep(0.05)
    pt.press("enter")
    i+=1