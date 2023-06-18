import tkinter as tk

root = tk.Tk()
root.attributes('-alpha', 0.9)  # Set window transparency (0.0 - fully transparent, 1.0 - fully opaque)

frame = tk.Frame(root, bg='white', bd=10)  # Create a frame with white background and 10 pixels border
frame.pack(fill='both', expand=True)

# Add your content or widgets to the frame
label = tk.Label(frame, text='Transparent Frame', font=('Arial', 18))
label.pack(padx=20, pady=20)

root.mainloop()