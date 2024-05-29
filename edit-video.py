# # # ffmpeg -i DVDES-513.ts -ss 0:35:40 -to 1:06:45 -c:v copy -c:a copy trimmedVideo.mp4

import subprocess
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

files = []
ONE = 1


def browse_file():
    """Opens a file dialog and sets the selected file path to the label."""
    filename = filedialog.askopenfilename()
    if filename:
        files.append(filename)
        file_label.config(text=f"Selected File: {filename}")


def show_warning():
    """Displays a warning message box."""
    messagebox.showwarning(title="Warning", message="This is a warning message.")


def submit():
    value_start = input_start.get(1.0, "end-1c")
    value_end = input_end.get(1.0, "end-1c")
    if len(files) < ONE:
        messagebox.showwarning(title="Warning", message="Please select file")
        return
    if len(value_start.split()) < 1:
        messagebox.showwarning(title="Warning", message="Input start none")
        return
    if len(value_end.split()) < 1:
        messagebox.showwarning(title="Warning", message="Input end none")
        return
    else:
        new_filename = ""
        type_video = files[0].split(".")[1:2]
        if str(type_video[0]) == "ts":
            new_filename = ".".join(files[0].split(".")[0:-1]) + ".mp4"
        else:
            new_filename = ".".join(files[0].split(".")[0:-1]) + "_new.mp4"

        subprocess.run(
            [
                "ffmpeg",
                "-i",
                files[0],
                "-ss",
                value_start,
                "-to",
                value_end,
                "-c:v",
                "copy",
                "-c:a",
                "copy",
                new_filename,
            ]
        )
        root.destroy()


# Create the main window
root = tk.Tk()
root.title("File Browser")

# Create a label to display the selected file path
file_label = tk.Label(root, text="No file selected yet.")
file_label.pack(padx=10, pady=10)

# Create a button to trigger the file selection dialog
browse_button = tk.Button(root, text="Browse File", command=browse_file)
browse_button.pack(pady=10)


# input start
label_start = tk.Label(root, text=f"Start")
label_start.pack(padx=5, pady=5)
input_start = tk.Text(height=3, width=30)
input_start.pack()

# input end
label_end = tk.Label(root, text=f"End")
label_end.pack(padx=5, pady=5)
input_end = tk.Text(height=3, width=30)
input_end.pack()

button_submit = tk.Button(root, text="Submit", command=submit)
button_submit.pack(pady=10)

# Run the main loop
root.mainloop()
