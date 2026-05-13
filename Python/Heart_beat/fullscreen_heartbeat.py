import tkinter as tk
import math
import time
import threading
import winsound
import os

SONG_PATH = r"C:\Users\PC\Desktop\HTML AND CSS PROJECT\Python\dandelions.wav"

def heart_points(scale, cx, cy, steps=200):
    pts = []
    for i in range(steps):
        t = 2 * math.pi * i / steps
        x = 16 * math.sin(t)**3
        y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
        pts.append(cx + x * scale)
        pts.append(cy - y * scale)
    return pts

class HeartApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg="black")
        self.root.bind("<Escape>", lambda e: self.close())
        self.root.bind("<Button-1>", lambda e: self.close())

        self.w = self.root.winfo_screenwidth()
        self.h = self.root.winfo_screenheight()

        self.canvas = tk.Canvas(self.root, bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.scale = min(self.w, self.h) / 45
        self.phase = 0
        self.last_beat = 0

        self.heart = self.canvas.create_polygon(
            heart_points(self.scale, self.w//2, self.h//2),
            fill="red", outline="pink", width=3, smooth=True
        )

        self.text = self.canvas.create_text(
            self.w//2, int(self.h*0.75),
            text="I ❤ U",
            fill="white",
            font=("Helvetica", int(self.scale*2), "bold")
        )

        if os.path.exists(SONG_PATH):
            threading.Thread(
                target=lambda: winsound.PlaySound(
                    SONG_PATH, winsound.SND_FILENAME | winsound.SND_LOOP
                ),
                daemon=True
            ).start()

        self.animate()
        self.root.mainloop()

    def animate(self):
        self.phase += 0.06
        pulse = 0.5 + 0.5 * math.sin(self.phase)
        scale = self.scale * (0.95 + 0.25 * pulse)

        self.canvas.coords(
            self.heart,
            *heart_points(scale, self.w//2, self.h//2)
        )

        now = time.time()
        if pulse > 0.97 and now - self.last_beat > 0.4:
            self.last_beat = now
            self.canvas.move(self.heart, 2, 2)
            self.root.after(40, lambda: self.canvas.move(self.heart, -2, -2))

        self.root.after(16, self.animate)

    def close(self):
        winsound.PlaySound(None, winsound.SND_PURGE)
        self.root.destroy()

if __name__ == "__main__":
    HeartApp()
