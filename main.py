import pyautogui as pg
import time
import PIL 
import cv2
import customtkinter as tk
import pyperclip
pg.FAILSAFE = False
subcount = None
def change_mode():
    if dark.get() == True:
        tk.set_appearance_mode("dark")
    else:
        tk.set_appearance_mode("light")
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
    js_get_count_script = (
        "var countElem=document.querySelector('#subscriber-count, .yt-core-attributed-string, [aria-label*=\"subscribers\"]');"
        "var cleanCount=countElem?countElem.textContent.replace(/[^0-9.KM]/g,'').trim():'Not Found';"
        "copy(cleanCount);"  # <-- JavaScript sends the data to your system clipboard
    )
    pg.typewrite(js_get_count_script)
    pg.hotkey("return",interval=0.1)
    pg.hotkey("command","option","j",interval=0.1)
    subcount = pyperclip.paste()
    if subcount != None:
        subs.configure(text="You were the " + str(subcount) + " subscriber of the channel " + str(channel) + "!")
    if auto_close.get() == True:
        pg.hotkey("command","shift","w",interval=0.1)
        
root = tk.CTk()
root.title = "Auto Subscriber"
root.geometry("600x400")
tk.set_appearance_mode("light")
tk.set_default_color_theme("blue")
title = tk.CTkLabel(root,text="Auto Subscriber",font=("Ariel", 24, "bold"))
title.pack(pady=(10,10))
label = tk.CTkLabel(root,text="Input a channel name", font = ("Ariel" ,13,"bold"))
label.pack(pady=(10,10))
line_edit = tk.CTkEntry(root, width=200,border_width=5,font=("Ariel",12))
line_edit.pack()
button = tk.CTkButton(root,text="Subscribe",border_width=5,font=("Ariel", 15, "bold"), command=youtube)
button.pack(pady=(10,0))
subs = tk.CTkLabel(root,text="")
subs.pack()
label2 = tk.CTkLabel(root,text="Customization", font=("Ariel",16, "bold"))
label2.pack(pady=(30,0))
notify = tk.BooleanVar()
notifications = tk.CTkCheckBox(root,text="Notifications On",variable=notify)
notifications.pack()
dark = tk.BooleanVar()
dark_mode = tk.CTkCheckBox(root,text="Dark Mode        ",variable=dark,command=change_mode)
dark_mode.pack(pady=(10,0))
auto_close = tk.BooleanVar()
autoclose = tk.CTkCheckBox(root,text="Auto Close Tab ",variable=auto_close)
autoclose.pack(pady=(10,0))
root.mainloop()