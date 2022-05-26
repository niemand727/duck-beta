from inspect import ClosureVars
from numpy import insert
import pafy
import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
import time
import webbrowser
import os

def download_list():
    file = open('links.txt','r')

    for line in file:
        url = line

        try:
            video = pafy.new(url)
            bestaudio = video.getbestaudio()
            print(video.title)

            bestaudio.download()

        except:
            print('Error')
            pass


    file.close()
    os.remove('links.txt')
    print("Files have been downloaded")
    





def add_link():
    f = open('links.txt','w')
    f.close()
    print("File has been created!")

def open_browser():
    print("User was redirected!")
    webbrowser.open_new_tab("https://youtu.be/jmXtG1xb4zo")

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=6, rowspan=3)



#logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#instructuions
instructions = tk.Label(root, text="              If you don't know how to use this open a browser and press How to use Button!", font = "Sans")
instructions.grid(columnspan=3, column= 0, row = 1)

#dev
dev = tk.Label(root, text="This app was developed by JF")
dev.grid(columnspan=3, column=0, row=3)

#button links
link_text = tk.StringVar()
link_btn = tk.Button(root, textvariable=link_text,command=lambda:add_link(), font = "Sans")
link_text.set('Create File')
link_btn.grid(column=1, columnspan=3, row=2)

#button download music
music_text = tk.StringVar()
music_btn = tk.Button(root, textvariable=music_text,command=lambda:download_list(), font = "Sans")
music_text.set('Download Music')
music_btn.grid(column=2, columnspan=3, row=2)

#button video
video_text = tk.StringVar()
video_btn = tk.Button(root, textvariable=video_text,command=lambda:open_browser(), font = "Sans")
video_text.set('How to use')
video_btn.grid(column=6, columnspan=3, row=2)


root.mainloop()