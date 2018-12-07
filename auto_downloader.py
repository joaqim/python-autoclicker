import pyautogui
from time import sleep, strftime


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
button_progress_offset_y = 145# + window_offset_y
button_progress_width_x = 240
button_progress_color = (46, 204, 113)

def download_has_started(x, y):
    return pyautogui.pixelMatchesColor(x + button_progress_offset_x + 1, y + button_progress_offset_y + 1, button_progress_color)
def download_is_finished_lazy(x, y):
    return pyautogui.pixelMatchesColor(x + button_progress_offset_x + button_progress_width_x - 1, y + button_progress_offset_y + 1, button_progress_color)
def download_is_finished(x, y):
    screenshot(x, y)
    return download_has_started(x, y) and download_is_finished_lazy(x, y)
def download_button_detected(x, y):
    return pyautogui.pixelMatchesColor(x, y+6, (245, 245, 245), tolerance=10)

def screenshot(x, y):
    img = pyautogui.screenshot(region=(x + button_progress_offset_x, y + button_progress_offset_y, button_progress_width_x, 20))
    #timestr = time.strftime("%H%M%S")
    img.save("test-{0}.PNG".format(strftime("%H%M%S")))

print("Starting in 5 seconds")
sleep(5)

for row in range(0, button_rows):
    for col in range(0, button_cols):
        curr_offset_x = button_start_pos[0] + button_offset_x * col
        curr_offset_y = button_start_pos[1] + button_offset_y * row

        if download_has_started(curr_offset_x, curr_offset_y):
            if not download_is_finished_lazy(curr_offset_x, curr_offset_y):
                screenshot(curr_offset_x, curr_offset_y)
                print("Download {0} is downloading".format((col + row)%button_cols))

                while not download_is_finished(curr_offset_x, curr_offset_y):
                    sleep(5)
                print("Download finished")
            else:
                print("Download {0} is complete".format((col + row)%button_cols))
        else:

            if not download_button_detected(curr_offset_x, curr_offset_y):
                print("Failed to detect download icon at Download {0}".format((col + row)%button_cols))
                continue
            print("Trying to start Download {0}".format((col + row)%button_cols))
            pyautogui.moveTo(curr_offset_x, curr_offset_y)
            pyautogui.click()

            sleep(5)
            if not download_has_started(curr_offset_x, curr_offset_y):
                print("Download {0} failed to start, moving on to next target".format((col + row)%button_cols))
            else:
                print("Download {0} is downloading".format((col + row)% button_cols))
                while not download_is_finished(curr_offset_x, curr_offset_y):
                    sleep(5)
                print("Download {0} finished".format((col + row)% button_cols))



