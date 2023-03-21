import tkinter as tk
from datetime import datetime

class DigitalClockGUI:
    def __init__(self, master):
        self.master = master
        master.title("WELCOME TO HIGH SPACE COMPUTER SCHOOL")
        master.geometry("500x300")
        master.config(bg="#7f7fd5")
        master.resizable(True, True) #  window resizing

        # Create a label for the heading text
        self.heading_label = tk.Label(master, text="HIGH SPACE COMPUTER SCHOOL", font=("Segoe UI", 50), bg="#7f7fd5", fg="#fff")

        self.heading_label.pack(pady=(20,10))

        # Create a label for the clock display
        self.clock_label = tk.Label(master, text="", font=("Segoe UI", 100), bg="#2c2c54", fg="#fff", width=11)
        self.clock_label.pack(pady=30)

        # Create a label for the instrustion_label
        self.instrustion_label = tk.Label(master, text="WELCOME TO PROGRAMMING CLASS", font=("Segoe UI", 40), bg="#2c2c54", fg="#fff", width=100)
        self.instrustion_label.pack(pady=(30))

        # Create a label for the instrustion_label
        self.instrustion2_label = tk.Label(master, text="WEB DESIGN -DESKTOP APP - MOBILE APP", font=("Segoe UI", 30), bg="#2c2c54", fg="#fff", width=100)
        self.instrustion2_label.pack(pady=(30))

         # Create a label for the instrustion_label
        self.instrustion3_label = tk.Label(master, text="CYBER SECURITY-ETHICAL HACKING", font=("Segoe UI", 30), bg="#2c2c54", fg="#fff", width=100)
        self.instrustion3_label.pack(pady=(30))

         # Create a label for the instrustion_label
        self.instrustion4_label = tk.Label(master, text="ARTIFICIAL INTELLIGENT", font=("Segoe UI", 30), bg="#2c2c54", fg="#fff", width=100)
        self.instrustion4_label.pack(pady=(30))

        # Create a label for the instrustion_label
        self.instrustion5_label = tk.Label(master, text="DATA SCIENCE-MACHINE LEARNING", font=("Segoe UI", 30), bg="#2c2c54", fg="#fff", width=100)
        self.instrustion5_label.pack(pady=(30))
        

        # Create a label for the footer text
        self.footer_label = tk.Label(master, text="©2023 HIGH SPACE COMPUTER SCHOOL", font=("Segoe UI", 8), bg="#7f7fd5", fg="#fff")
        self.footer_label.pack(side=tk.BOTTOM, pady=30)

        self.update_clock()

    def update_clock(self):
        time = datetime.now().strftime("%I:%M:%S %p")
        self.clock_label.config(text=time)
        self.master.after(1000, self.update_clock)

root = tk.Tk()
gui = DigitalClockGUI(root)
root.mainloop()
