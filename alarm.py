import time
from datetime import datetime
import tkinter as tk
from tkinter import *
import pyglet
from tkinter import ttk
from PIL import Image,ImageTk
import pygame.mixer as pmx
from threading import Thread


# pyglet.font.add_file('Digital.ttf')
def main():
    def changetext():
        now = time.strftime('%H:%M:%S',time.localtime())
        clock.config(text=now)
        clock.after(200,changetext) 

    root = tk.Tk()
    root.title('Time Table',)
    root.geometry('400x400+1020+0')
    schedule = tk.PhotoImage(file='source/schedule.png')
    root.iconphoto(True,schedule)
   # root.minsize(400,400)
    root.maxsize(400,400)
    #root.overrideredirect(True)

    pyglet.font.add_file('D:\字体\let_s_go_digital\Let_s_go_Digital\Digital.ttf')
    # zh = tfont.Font(family='Pixtile',size=50)

    line = Canvas(root,bd=0)
    line.create_rectangle(2,90,398,95,outline='#33FFF6',fill='#33FFF6')
    line.pack()

    #时间显示区域
    clock = Label(root,text='00:00:00',fg='#4682B4',font=('Let\'s go Digital', 48))
    clock.place(x=96,y=20)
    changetext()
    #小时区域
    Hour = Label(root,text='Hou',font=('Times',16))
    Hour.place(x=45,y=110)
    #分钟区域
    Min = Label(root,text='Min',font=('Times',16))
    Min.place(x=179,y=110)
    #秒钟区域
    Sec = Label(root,text='Sec',font=('Times',16))
    Sec.place(x=320,y=110)
    #设置时钟图标
    icon = Image.open('source/icon.png')
    icon=icon.resize((72,72))
    icon = ImageTk.PhotoImage(icon)
    alarm_icon = Label(root,image=icon)
    alarm_icon.place(x=14,y=14)
    #设置时钟选项
    c_hou = ttk.Combobox(root,font=('',14),width=2)
    c_hou['value'] = ('00','01','02','03','04','05','06','07','08','09','10','11','12',\
    '13','14','15','16','17','18','19','20','21','22','23','24')
    c_hou.place(x=45,y=140)
    c_hou.current(0)
    #设置分钟选项
    c_min = ttk.Combobox(root,font=('',14),width=2)
    c_min['value'] = ('00','01','02','03','04','05','06','07','08','09','10','11','12',\
    '13','14','15','16','17','18','19','20','21','22','23','24',\
    '25','26','27','28','29','30','31','32','33','34',\
    '35','36','37','38','39','40','41','42','43','44',\
    '45','46','47','48','49','50','51','52','53','54',\
    '55','56','57','58','59','60')
    c_min.place(x=179,y=140)
    c_min.current(0)
    #设置秒钟选项
    c_sec = ttk.Combobox(root,font=('',14),width=2)
    c_sec['value'] = ('00','01','02','03','04','05','06','07','08','09','10','11','12',\
    '13','14','15','16','17','18','19','20','21','22','23','24',\
    '25','26','27','28','29','30','31','32','33','34',\
    '35','36','37','38','39','40','41','42','43','44',\
    '45','46','47','48','49','50','51','52','53','54',\
    '55','56','57','58','59','60')
    c_sec.place(x=320,y=140)
    c_sec.current(0)
    '''
    引入播放音乐模块
    '''
    def activate_alarm():
        t = Thread(target=alarm,daemon=True)
        t.start()
    def deactivate_alarm():
        pmx.music.stop()
    def music_play():
        pmx.music.load('Closer.mp3')
        pmx.music.play()
        print('time reached')

    def alarm():
        while True:
            
            
            c_hour = c_hou.get()
            c_minute = c_min.get()
            c_second = c_sec.get()

            now = datetime.now()
            hour = now.strftime('%H')
            min = now.strftime('%M')
            sec = now.strftime('%S')

            if hour==c_hour and min==c_minute and sec==c_second:
                music_play()
            time.sleep(1)

        
    #设置启动按钮
    start = Button(root,bg='#00FA9A',text='Start',font='Times',width=5,command=activate_alarm)
    start.place(x=168,y=200)
    #设置停止按钮
    stop = Button(root,bg='#2F4F4F',text='Stop',font='Times',width=5,command=deactivate_alarm)
    stop.place(x=108,y=260)
    #记录时间值
    record = Button(root,bg='#2F4F4F',text='Record',font='Times',width=5)
    record.place(x=232,y=260)

    pmx.init()
    root.mainloop()
if __name__=='__main__':
    main()
