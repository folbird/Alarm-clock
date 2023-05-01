import tkinter as tk
from datetime import datetime
import time
from playsound import playsound
window = tk.Tk()
window.geometry('100x100')

def music_play():
    playsound('Closer.mp3')

def alarm():
    while True:
        control = 1
        print(control)
        c_hour = '16'
        c_minute = '15'
        c_second = '10'
        now = datetime.now()
        hour = now.strftime('%H')
        min = now.strftime('%M')
        sec = now.strftime('%S')

        if hour==c_hour and min==c_minute and sec==c_second:
            music_play()
        print(hour,min,sec)

        time.sleep(1)
if __name__=='__main__':
    alarm()
window.mainloop()