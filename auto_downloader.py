import pyautogui

button_start_pos = (277, 168)
button_offset_x = 250
button_offset_y = 250
button_cols = 7
button_rows = 4

pyautogui.PAUSE = 2.5
pyautogui.FAILSAFE = True

for row in range(0, button_rows):
    for col in range(0, button_cols):
        pyautogui.moveTo(button_start_pos[0] + button_offset_x*col, button_start_pos[1] + button_offset_y * row)
        pyautogui.click()

