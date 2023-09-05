import tkinter as tk

# Function to handle button clicks
def button_click(button_num):
    text_field.delete(1.0, tk.END)  # Clear the text field
    text_field.insert(tk.END, f"Button {button_num} clicked!")
    text_field.insert(tk.END, "\nWe made it!")


# Create the main window
window = tk.Tk()
window.title("Real Estate Web Scraper")

# Create a text field
text_field = tk.Text(window, height=5, width=30)
text_field.pack(pady=10)

# Button 1 and label 1
label1 = tk.Label(window, text="Sales Web - Foreclosure Sales Listing")
label1.pack()

button1 = tk.Button(window, text="Click to Scrape", command=lambda: button_click(1))
button1.pack(pady=10)

# Button 2 and Label 2
label2 = tk.Label(window, text="Website to Implement:")
label2.pack()

button2 = tk.Button(window, text="Click to Scrape", command=lambda: button_click(2))
button2.pack(pady=10)

# Button 3 and Label 3
label3 = tk.Label(window, text="Experimental Feature")
label3.pack()

button3 = tk.Button(window, text="Click me!", command=lambda: button_click(3))
button3.pack(pady=10)

# Start the main event loop
window.mainloop()
