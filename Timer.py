from plyer import notification
from tkinter import messagebox, Tk, Label, Entry, Button, IntVar
from tkinter import ttk
import time

class CountdownTimer:
    def __init__(self, window):
        self.window = window
        self.window.geometry("400x300")
        self.window.title("Countdown Timer")
        self.window.configure(bg="#2C3E50")

        # Variables to store the timer values
        self.hours = IntVar()
        self.minutes = IntVar()
        self.seconds = IntVar()

        # UI Setup
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        Label(self.window, text="Countdown Timer", font=("Arial", 16, "bold"), bg="#2C3E50", fg="white").pack(pady=10)
        Label(self.window, text="Enter hours, minutes, and seconds", font=("Arial", 10), bg="#2C3E50", fg="#BDC3C7").pack()

        # Time Entry Fields
        self.hour_entry = ttk.Entry(self.window, width=5, textvariable=self.hours, font=("Arial", 14))
        self.minute_entry = ttk.Entry(self.window, width=5, textvariable=self.minutes, font=("Arial", 14))
        self.second_entry = ttk.Entry(self.window, width=5, textvariable=self.seconds, font=("Arial", 14))
        
        # Default values
        self.hour_entry.insert(0, "00")
        self.minute_entry.insert(0, "00")
        self.second_entry.insert(0, "00")
        
        # Positioning entry fields
        self.hour_entry.place(x=110, y=80)
        self.minute_entry.place(x=170, y=80)
        self.second_entry.place(x=230, y=80)

        # Bind click events to clear placeholders
        self.hour_entry.bind("<FocusIn>", lambda event: self.clear_entry(self.hour_entry))
        self.minute_entry.bind("<FocusIn>", lambda event: self.clear_entry(self.minute_entry))
        self.second_entry.bind("<FocusIn>", lambda event: self.clear_entry(self.second_entry))

        # Start Button
        self.start_button = ttk.Button(self.window, text='Start Timer', command=self.start_timer, style="TButton")
        self.start_button.pack(pady=50)

        # Styling
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 12, "bold"), padding=6, background="#E74C3C", foreground="white")

    def clear_entry(self, entry):
        """Clear the placeholder text when the entry is clicked."""
        if entry.get() in ["00", "Hours", "Minutes", "Seconds"]:
            entry.delete(0, "end")

    def start_timer(self):
        """Start the countdown timer."""
        try:
            total_time = self.hours.get() * 3600 + self.minutes.get() * 60 + self.seconds.get()

            if total_time <= 0:
                messagebox.showerror(message="Please enter a valid time greater than 0.")
                return

            while total_time >= 0:
                hours, remainder = divmod(total_time, 3600)
                minutes, seconds = divmod(remainder, 60)

                self.hours.set(hours)
                self.minutes.set(minutes)
                self.seconds.set(seconds)

                self.window.update()
                time.sleep(1)
                total_time -= 1

            # Notify when timer is complete
            notification.notify(
                title="TIMER ALERT",
                message="Hey amigo!\nDid you do what you wanted to achieve? \nIf not, try again with a new timer!",
                timeout=30
            )
            messagebox.showinfo(message="Timer Complete!")

        except ValueError:
            messagebox.showerror(message="Please enter valid numbers in all fields.")

if __name__ == "__main__":
    root = Tk()
    app = CountdownTimer(root)
    root.mainloop()
