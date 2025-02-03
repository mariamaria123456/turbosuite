import psutil
import time
import tkinter as tk
from tkinter import ttk

class TurboSuite:
    def __init__(self, root):
        self.root = root
        self.root.title("TurboSuite - CPU and Memory Usage Monitor")
        self.root.geometry("400x300")
        
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        self.cpu_label = ttk.Label(self.root, text="CPU Usage", font=("Arial", 14))
        self.cpu_label.pack(pady=10)

        self.cpu_bar = ttk.Progressbar(self.root, orient='horizontal', length=300, mode='determinate')
        self.cpu_bar.pack(pady=10)

        self.memory_label = ttk.Label(self.root, text="Memory Usage", font=("Arial", 14))
        self.memory_label.pack(pady=10)

        self.memory_bar = ttk.Progressbar(self.root, orient='horizontal', length=300, mode='determinate')
        self.memory_bar.pack(pady=10)

        self.update_usage()

    def update_usage(self):
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.percent

        self.cpu_bar['value'] = cpu_usage
        self.memory_bar['value'] = memory_usage

        self.cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
        self.memory_label.config(text=f"Memory Usage: {memory_usage}%")

        self.root.after(1000, self.update_usage)

if __name__ == "__main__":
    root = tk.Tk()
    app = TurboSuite(root)
    root.mainloop()