import pyautogui
from time import sleep

window_offset_x = 0
window_offset_y = 60

button_start_pos = (277 + window_offset_x, 168 + window_offset_y)
button_offset_x = 251
button_offset_y = 248
button_cols = 7
button_rows = 4
#button_cols = 1
#button_rows = 1

pyautogui.PAUSE = 2.5
#pyautogui.PAUSE = 5400 # Wait 1.5h between mouse clicks
pyautogui.FAILSAFE = True

button_progress_offset_x = -120
button_progress_offset_y = 145
button_progress_width_x = 240
button_progress_color = (46, 204, 113)


for row in range(0, button_rows):
    for col in range(0, button_cols):
        curr_offset_x = button_start_pos[0] + button_offset_x * col
        curr_offset_y = button_start_pos[1] + button_offset_y * row

        img = pyautogui.screenshot(region=(curr_offset_x + button_progress_offset_x, curr_offset_y + button_progress_offset_y, button_progress_width_x, 20))
        img.save("test.PNG")

        if pyautogui.pixelMatchesColor(curr_offset_x + button_progress_offset_x + 1, curr_offset_y + button_progress_offset_y + 1, button_progress_color):
            if not pyautogui.pixelMatchesColor(curr_offset_x + button_progress_offset_x + button_progress_width_x - 1, curr_offset_y + button_progress_offset_y + 1, button_progress_color):
                img = pyautogui.screenshot(region=(curr_offset_x + button_progress_offset_x, curr_offset_y + button_progress_offset_y, button_progress_width_x, 20))
                img.save("test.PNG")
                print("Download is in progress")
                #pyautogui.moveTo(1, 1)
                #pyautogui.click()
                while not pyautogui.pixelMatchesColor(curr_offset_x + button_progress_offset_x + button_progress_width_x - 1, curr_offset_y + button_progress_offset_y + 1, button_progress_color):
                    sleep(5)
                print("Download finished")
            else:
                print("Download at position: {0} is complete".format((col + row)%button_cols))
        else:
            print("Starting Download at position: {0}".format((col + row)%button_cols))
            pyautogui.moveTo(curr_offset_x, curr_offset_y)
            pyautogui.click()


