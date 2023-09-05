import tkinter as tk
from tkinter import ttk
import time


# Function to simulate a task
def simulate_task():
    progress_bar.start(10)  # Start the progress bar animation

    # Simulate a task that takes 5 seconds
    for _ in range(5):
        time.sleep(1)
        progress_bar['value'] += 19
        window.update_idletasks()  # Update the window to display the progress bar

    progress_bar.stop()  # Stop the progress bar animation
    # progress_bar['value'] = 0  # Reset the progress bar value


# Create the main window
window = tk.Tk()
window.title("Loading Screen")

# Create a label for the loading text
loading_label = tk.Label(window, text="Loading...")
loading_label.pack(pady=10)

# Create a progress bar
progress_bar = ttk.Progressbar(window, mode='determinate', length=300)
progress_bar.pack(pady=10)

# Create a button to start the task
start_button = tk.Button(window, text="Start Task", command=simulate_task)
start_button.pack(pady=10)

# Start the main event loop
window.mainloop()
