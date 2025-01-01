import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import psutil
import numpy as np

class HMIDesign:
    def __init__(self, root):
        self.root = root
        self.root.title("HMI Design")
        self.root.geometry("800x600")

        self.control_frame = ttk.Frame(root)
        self.control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        self.start_button = ttk.Button(self.control_frame, text="Start", command=self.start_system)
        self.start_button.pack(pady=5)
        
        self.stop_button = ttk.Button(self.control_frame, text="Stop", command=self.stop_system)
        self.stop_button.pack(pady=5)

        self.monitor_button = ttk.Button(self.control_frame, text="Monitor", command=self.monitor_system)
        self.monitor_button.pack(pady=5)

        self.figure = plt.Figure(figsize=(6,5), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, root)
        self.canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.x_data = np.linspace(0, 10, 100)
        self.y_data = np.sin(self.x_data)

        self.ax.plot(self.x_data, self.y_data)
        self.ax.set_title("System Data Visualization")
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Value")

    def start_system(self):
        print("System started.")

    def stop_system(self):
        print("System stopped.")

    def monitor_system(self):
        cpu_usage = psutil.cpu_percent()
        mem_usage = psutil.virtual_memory().percent
        print(f"CPU Usage: {cpu_usage}%")
        print(f"Memory Usage: {mem_usage}%")

if __name__ == "__main__":
    root = tk.Tk()
    app = HMIDesign(root)
    root.mainloop()
