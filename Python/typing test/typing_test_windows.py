import tkinter as tk
import time
import random

TEXTS = [
    "The quick brown fox jumps over the lazy dog",
    "Typing speed improves with consistent practice",
    "Python is powerful and easy to learn",
    "Discipline and focus create excellence",
    "Software engineering rewards clarity of thought"
]


class TypingTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Speed Typing Test")
        self.root.geometry("900x300")
        self.root.resizable(False, False)

        self.text = random.choice(TEXTS)
        self.start_time = None
        self.running = False

        self.build_ui()

    def build_ui(self):
        self.label_text = tk.Label(
            self.root, text=self.text, font=("Consolas", 16)
        )
        self.label_text.pack(pady=20)

        self.entry = tk.Entry(
            self.root, font=("Consolas", 16), width=60
        )
        self.entry.pack()
        self.entry.bind("<KeyRelease>", self.on_key)

        self.wpm_label = tk.Label(
            self.root, text="WPM: 0", font=("Arial", 14)
        )
        self.wpm_label.pack(pady=10)

        self.result_label = tk.Label(
            self.root, text="", font=("Arial", 14)
        )
        self.result_label.pack()

        self.restart_btn = tk.Button(
            self.root, text="Restart", command=self.restart
        )
        self.restart_btn.pack(pady=10)

    def on_key(self, event):
        if not self.running:
            self.start_time = time.time()
            self.running = True

        typed = self.entry.get()

        if typed == self.text:
            self.finish()
            return

        elapsed = max(time.time() - self.start_time, 1)
        wpm = round((len(typed) / 5) / (elapsed / 60))
        self.wpm_label.config(text=f"WPM: {wpm}")

        self.update_colors(typed)

    def update_colors(self, typed):
        correct = 0
        for i in range(min(len(typed), len(self.text))):
            if typed[i] == self.text[i]:
                correct += 1

        self.result_label.config(
            text=f"Correct Characters: {correct} / {len(self.text)}"
        )

    def finish(self):
        elapsed = time.time() - self.start_time
        final_wpm = round((len(self.text) / 5) / (elapsed / 60))

        self.wpm_label.config(text=f"Final WPM: {final_wpm}")
        self.result_label.config(text="Completed!")
        self.entry.config(state="disabled")

    def restart(self):
        self.text = random.choice(TEXTS)
        self.label_text.config(text=self.text)
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)
        self.wpm_label.config(text="WPM: 0")
        self.result_label.config(text="")
        self.start_time = None
        self.running = False


if __name__ == "__main__":
    root = tk.Tk()
    TypingTest(root)
    root.mainloop()
