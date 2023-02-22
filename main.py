import threading
import tkinter
import os
import sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
# from tkFileDialog   import askopenfilename
from pytube import YouTube

has_download = False

def display(message):
    tkinter.messagebox.showwarning(title='Information Error', message=message)
    return False

def handle_info(link, url):
    check = True
    if not link and not url:
        check = display('Invalid Youtube Video Link and Directory')
    elif not link:
        check = display('Invalid Youtube Video Link')
    elif not url:
        check = display('Invalid Directory')
    return check

def download_video():
    link = url.get() 
    path = directory.get()
    check = handle_info(link, path)

    if not check:
        progress.grid_forget()
        return

    progress.start()
    YouTube(link).streams.filter(progressive=True, file_extension='mp4').last().download(path)
    progress.stop()
    progress.grid_forget()
    tkinter.messagebox.showinfo(title='success', message='Download completed')

def download():
    progress.grid(row=4, column=1, pady=20)
    threading.Thread(target=download_video).start()
    

def select():
    path = filedialog.askdirectory()
    directory.delete(0, END)
    directory.insert(0, path)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

window = Tk()
window.title('YouTube Downloader')
window.iconbitmap(resource_path('youtube.ico'))
window.geometry('800x350')
window.maxsize(800, 350)
window.minsize(800, 350)

youtbe_image_path = resource_path('youtube.png')
image = PhotoImage(file=youtbe_image_path)
image = image.subsample(10, 10)
youtube_image = Label(window, image=image)
youtube_image.grid(row=0, column=0, pady=5)
header = Label(window, text='Youtube Downloader')
header.grid(row=0,column=1, sticky='w', pady=5)
header.configure(font=('Adobe Garamond Pro', 16, 'bold'))


url_label = Label(window, text='YouTube URL')
url_label.grid(row=1,column=0, padx=10, pady=20)
url_label.configure(font=('Adobe Garamond Pro', 12, 'normal'))
url = Entry(window, bd=3)
url.grid(row=1, column=1, sticky='E', ipadx=200, ipady=2, padx=10, pady=20)


directory_label = Label(window, text='Directory')
directory_label.grid(row=2, column=0, sticky='w', padx=10, pady=20)
directory_label.configure(font=('Adobe Garamond Pro', 12, 'normal'))
directory = Entry(window, bd=3)
directory.grid(row=2, column=1, sticky='E', ipadx=200, ipady=2, padx=10, pady=20)
Button(window, text='Select', command=select).grid(row=2, column=2, padx=10)


Button(window, text='Download', command=download).grid(row=3, column=1)


progress = ttk.Progressbar(
    window,
    orient='horizontal',
    mode='indeterminate',
    length=280,
    maximum=100
)


window.mainloop()
