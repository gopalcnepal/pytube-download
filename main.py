######################################
######## YouTube Downloader ##########
######################################

#  Importing Suitable Libraries 
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from pytube import YouTube
from pytube import Playlist
import time

# Adding Window Components
root = tk.Tk()
root.title("YouTube Downloader")
root.geometry('1200x900')

# Add a Scrollbar(horizontal)
v=Scrollbar(root, orient='vertical', width=25, bg="red")
v.pack(side=RIGHT, fill='y')

#function code 
def download():
    TYPE = typeVar.get() #selectType()
    #print(TYPE,RESOLUTION)

    link = str(name_tf.get())
    
    if link == '':
        messagebox.showerror("YouTube Downloader", "Please Enter a Link") 
    else:
        if TYPE == 2:
            try:
                p = Playlist(link)
            except:
                messagebox.showinfo("ERROR. Connection Error.")
            
            count = 1
            #print('Playlist Download')
            total = len(p.videos)
            for video in p.videos:
                root.update()
                update_text(video, count, total)
                download_vid(video, count, total)
                count += 1

        else:
            #print('Video Download')
            yt = YouTube(link)
            update_text(yt, 1, 1)
            root.update()
            download_vid(yt, 1, 1)
        
        messagebox.showinfo("YouTube Downloader",'All Video Download Completed Successfully')

def download_vid(yt,count,total):
    #print('download_vid function called')
    RESOLUTION = resolutionVar.get() #selectResolution()

    if RESOLUTION == 2:
        stream = yt.streams.get_lowest_resolution()
    else:
        stream = yt.streams.get_highest_resolution()

    #Prepares the file for download
    stream.download()
    
def update_text(yt,count,total):
    # Writing Downloading Output
    Wtext = 'Downloading ('+str(count)+'/'+str(total)+') : ' + yt.title + '\n'
    t.insert(END, Wtext)
    
# main design code 
#youtube logo image
#yt1_logo = ImageTk.PhotoImage(Image.open('yt.png'))
#tk.Label(root, image = yt1_logo,borderwidth=0).pack()

tk.Label(root,text="YouTube Downloader", fg = "red", font = "Times 15 bold").pack()

#get the url
name_tf = Entry(root)
name_lbl = Label(root,text='Enter URL',fg='black')
name_lbl.pack()
name_tf.pack(fill='x', padx=20)
# Type of Download
typeVar = IntVar()
frame = LabelFrame(root, text='Choose Type')
frame.pack(pady=10)

Radiobutton(frame, text='Video', variable=typeVar, value=1).pack(anchor=W)
Radiobutton(frame, text="Playlist", variable=typeVar, value=2).pack(anchor=W)

# Resolution Selection
resolutionVar = IntVar()
frame = LabelFrame(root, text='Choose Resolution')
frame.pack(pady=10)

Radiobutton(frame, text='Highest', variable=resolutionVar, value=1).pack(anchor=W)
Radiobutton(frame, text="Lowest", variable=resolutionVar, value=2).pack(anchor=W)

#Download Buttons
btn = Button(root,text='Download',relief=RIDGE,font=('verdana',10,'bold'),bg="green",fg="white",command=download)
btn.pack(pady=10)

#Close
Button(root, text="Cancel and Quit", relief=RIDGE,font=('verdana',10,'bold'),bg="red",fg="white", command=root.destroy).pack(pady=10)

Label(root,text='Download Status',fg='black').pack(pady=10)
t = tk.Text(root,yscrollcommand=v.set)
v.config(command=t.yview)
t.pack(expand=True, fill='both', padx=20)

root.update()

root.mainloop()