from pytube import YouTube
import tkinter as tk
from tkinter import filedialog, messagebox
import os


def download_video(url, save_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(
            progressive=True,
            file_extension="mp4"
        ).get_highest_resolution()

        stream.download(output_path=save_path)

        messagebox.showinfo(
            "Success",
            "Video downloaded successfully!"
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            str(e)
        )


def open_folder_dialog():
    folder = filedialog.askdirectory(
        title="Select folder to save video"
    )
    return folder


if __name__ == "__main__":
    # Initialize Tkinter (Windows-safe)
    root = tk.Tk()
    root.withdraw()       # Hide main window
    root.attributes("-topmost", True)  # Bring dialog to front

    video_url = input("Enter YouTube URL: ").strip()

    if not video_url:
        messagebox.showwarning(
            "Warning",
            "No URL provided."
        )
        exit()

    save_dir = open_folder_dialog()

    if save_dir and os.path.exists(save_dir):
        download_video(video_url, save_dir)
    else:
        messagebox.showwarning(
            "Warning",
            "Invalid save location selected."
        )

    root.destroy()
