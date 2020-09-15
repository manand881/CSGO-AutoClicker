import pyautogui
import keyboard
# import mouse
import time 

counter=0
input_counter=0
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('`'):  # if key 'q' is pressed 
            input_counter+=1
            print(input_counter)
            for x in range(10):
                counter+=1
                # mouse.press(button='left')
                pyautogui.click()
                time.sleep(0.1)
                print("clicked")
            print(counter," successful clicks")
    except:
        break  # if user pressed a key other than the given key the loop will break
    counter=0
    time.sleep(0.1)