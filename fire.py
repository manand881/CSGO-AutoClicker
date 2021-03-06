import pyautogui                                                # importing pyautogui to automate click task
import mouse                                                    # importing mouse to set a key press listener
import time                                                     # importing time to use sleep function
from intro import csgo                                          # importing ascii text

autoclick_counter = 0
keypress_counter = 0

while True:                                                     # starting an infinite loop to keep listening to keypress events

    try:                                                        # using try so that the program will not end abruptly in the event of an error

        if mouse.is_pressed(button='middle'):                   # if scroll wheel or middle button is pressed

            keypress_counter += 1
            print(keypress_counter, "total keypresses recieved")  # keeping track of input key strokes and printing it

            for x in range(5):                                  # setting a sub loop to run 10 times and fire once per iteration

                autoclick_counter += 1                          # keeping track of iterated auto clicks
                pyautogui.click()                               # automating mouse click at current mouse position
                time.sleep(0.04)                                # sleeping for sometime so the autocheat does not feel like something fishy is happening
                print("clicked")

            print(autoclick_counter, "successful clicks this round")
            autoclick_counter = 0                               # reset click counter

    except Exception as e:
        print(e)                                                # print error if something wrong happens

    time.sleep(0.1)                                             # putting a hold on the while loop so it does not take up too much system resources
