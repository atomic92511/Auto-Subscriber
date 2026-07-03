import pyautogui as pg
import time
import PIL 
import cv2
import tkinter as tk
pg.FAILSAFE = False
def youtube():
    notify_on = notify.get()
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
    js_click_script_notify = (
    "var s=Array.from(document.querySelectorAll('button,span,yt-formatted-string')).find(e=>['Subscribe','Subscribed'].includes(e.textContent.trim()));if(s){s.click();setTimeout(()=>{var a=Array.from(document.querySelectorAll('ytd-menu-service-item-renderer,tp-yt-paper-item,span')).find(e=>e.textContent.trim()==='All');if(a)a.click();},400);}"
    )


    if notify_on == False:
        pg.typewrite(js_click_script)
    else:
        pg.typewrite(js_click_script_notify)
    pg.hotkey("return")
    pg.hotkey("command","option","j",interval=0.1)
root = tk.Tk()
root.title = "Auto Subscriber"
root.geometry("600x400")

title = tk.Label(root,text="Auto Subscriber",font=("Ariel", 16, "bold"))
title.pack(pady=(20,10))
label = tk.Label(root,text="Input a channel name", font = ("Ariel" ,10,"bold"))
label.pack(pady=(10,10))
line_edit = tk.Entry(root, width=20,borderwidth=5,font=("Ariel",12))
line_edit.pack()
button = tk.Button(root,text="Subscribe",borderwidth=5,font=("Ariel", 15, "bold"), command=youtube)
button.pack()
label2 = tk.Label(root,text="Customization", font=("Ariel",16, "bold"))
label2.pack(pady=(30,0))
notify = tk.BooleanVar()
notifications = tk.Checkbutton(root,text="Notifications On",variable=notify)
notifications.pack()
root.mainloop()