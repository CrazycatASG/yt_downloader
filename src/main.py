"""
this code is hereby released into the public domain, or under CC0, at your option.
"""

import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from yt_dlp import YoutubeDL


def download_video(url, fileformat):
    """Downloads a video from Youtube, either as an audio, or video.

    Args:
        url (string): The URL of the video you wish to download
        fileformat (string): Audio or Video, fairly simply.

    Returns:
        _type_: _description_
    """    
    if "youtube.com" not in url:
        messagebox.showerror("Error", "That's not a Youtube link!")
        return "failed: that's not a yt link"
    else:
        pass

    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    if os.name == 'nt':
        ffmpeg_path = os.path.join(os.path.dirname(__file__), 'ffmpeg', 'ffmpeg.exe') # Defines the ffmpeg folder.
    else:
        ffmpeg_path = os.path.join(os.path.dirname(__file__), 'ffmpeg', 'ffmpeg') 
    
    ydl_opts = {
        'outtmpl': os.path.join(downloads_folder, '%(title)s.%(ext)s'), 
        'ffmpeg_location': ffmpeg_path,
    }

    if fileformat == "audio":
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    elif fileformat == "video":
        ydl_opts.update({
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
        })

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", f"{fileformat.capitalize()} download completed!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Defining the main window
window = tk.Tk()
window.title("Hail's YT Downloader.")
window.geometry('400x200') 

# All widgets that make part of the app.
downloadLabel = ttk.Label(
    text="Enter the link to be downloaded:",
)

watermark = ttk.Label(
    text="Made by your royally, Hailfire",
    font=("Arial", 10)
)

userinput = ttk.Entry(
    
)

downloadaudio = ttk.Button(
    text="Download as audio",
    command=lambda: download_video(userinput.get(), "audio")  
)

downloadvideo = ttk.Button(
    text="Download as a video",
    command=lambda: download_video(userinput.get(), "video")   
)

downloadLabel.pack()
userinput.pack()
downloadaudio.pack()
downloadvideo.pack()
watermark.pack(side=tk.BOTTOM,pady=20)

window.mainloop()
