import pyautogui as pg
import time
import PIL 
import cv2
import tkinter as tk
pg.FAILSAFE = False
def youtube():
    channel = line_edit.get()
    pg.moveTo(0,0)

    pg.click()

    pg.hotkey("command","space", interval=0.1)

    pg.typewrite("chrome")

    pg.hotkey("return",interval=0.1)

    pg.hotkey("command", "t", interval=0.1)

    pg.typewrite("youtube.com/@" + str(channel))

    pg.hotkey("return",interval=0.1)
    pg.hotkey("command", "option", "j", interval=0.1)
    js_click_script = (
        "var b=Array.from(document.querySelectorAll('button,span,yt-formatted-string'))"
        ".find(e=>['Subscribe','Subscribed'].includes(e.textContent.trim()));if(b)b.click();"
    )
    pg.typewrite(js_click_script)
    pg.hotkey("return")
    pg.hotkey("command","option","j",interval=0.1)
root = tk.Tk()
root.title = "Auto Subscriber"
root.geometry("300x200")

title = tk.Label(root,text="Auto Subscriber",font=("Ariel", 16, "bold"))
title.pack(pady=(20,10))
label = tk.Label(root,text="Input a channel name", font = ("Ariel" ,10,"bold"))
label.pack(pady=(10,10))
line_edit = tk.Entry(root, width=20,borderwidth=5,font=("Ariel",12))
line_edit.pack()
button = tk.Button(root,text="Subscribe",borderwidth=5,font=("Ariel", 15, "bold"), command=youtube)
button.pack()
root.mainloop()