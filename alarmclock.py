import tkinter as tk
from tkinter import ttk, messagebox
import datetime
import threading
import pygame

class AlarmClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")

        self.alarm_time = None
        self.alarm_thread = None

        self.setup_gui()

    def setup_gui(self):
        # Label and entry for setting alarm time
        ttk.Label(self.root, text="Set Alarm Time (HH:MM)").grid(row=0, column=0, padx=10, pady=10)
        self.alarm_entry = ttk.Entry(self.root, width=10)
        self.alarm_entry.grid(row=0, column=1, padx=10, pady=10)

        # Button to set alarm
        set_alarm_btn = ttk.Button(self.root, text="Set Alarm", command=self.set_alarm)
        set_alarm_btn.grid(row=0, column=2, padx=10, pady=10)

        # Label to display current time
        self.time_label = ttk.Label(self.root, text="")
        self.time_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Start button
        start_btn = ttk.Button(self.root, text="Start Alarm", command=self.start_alarm)
        start_btn.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        # Stop button
        stop_btn = ttk.Button(self.root, text="Stop Alarm", command=self.stop_alarm)
        stop_btn.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    def update_time(self):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time_label.config(text=f"Current Time: {now}")
        self.root.after(1000, self.update_time)

    def set_alarm(self):
        alarm_str = self.alarm_entry.get().strip()
        try:
            self.alarm_time = datetime.datetime.strptime(alarm_str, "%H:%M").time()
            messagebox.showinfo("Alarm Set", f"Alarm set for {self.alarm_time.strftime('%H:%M')}")
        except ValueError:
            messagebox.showerror("Error", "Invalid time format. Please enter HH:MM.")

    def play_alarm_sound(self):
        pygame.mixer.init()
        pygame.mixer.music.load("alarm_sound.mp3")  # Replace with your alarm sound file
        pygame.mixer.music.play()

    def alarm_thread_func(self):
        while True:
            now = datetime.datetime.now().time().replace(second=0, microsecond=0)
            if now == self.alarm_time:
                messagebox.showinfo("Alarm", "Wake up!")
                self.play_alarm_sound()
                break

    def start_alarm(self):
        if self.alarm_time:
            self.alarm_thread = threading.Thread(target=self.alarm_thread_func)
            self.alarm_thread.start()
        else:
            messagebox.showwarning("Warning", "Please set the alarm first.")

    def stop_alarm(self):
        if self.alarm_thread and self.alarm_thread.is_alive():
            pygame.mixer.music.stop()
            messagebox.showinfo("Alarm Stopped", "Alarm stopped.")
        else:
            messagebox.showwarning("Warning", "No active alarm.")

if __name__ == "__main__":
    pygame.init()

    root = tk.Tk()
    app = AlarmClockApp(root)
    app.update_time()  # Start updating time label
    root.mainloop()
