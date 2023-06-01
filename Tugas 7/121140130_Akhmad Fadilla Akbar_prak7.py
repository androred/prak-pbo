import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, master):
        self.master = master
        master.title("Text Editor")
        master.geometry("900x800")


        self.button_frame = tk.Frame(master, width=100)
        self.button_frame.pack(side=tk.BOTTOM, fill=tk.Y)
        self.text_frame = tk.Frame(master, width=700)
        self.text_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)


        self.open_button = tk.Button(self.button_frame, text="Open", command=self.open_file, bg="#2192FF")
        self.open_button.pack(side=tk.LEFT, pady=10, padx=20)
        self.save_button = tk.Button(self.button_frame, text="Save", command=self.save_file, bg="#38E54D")
        self.save_button.pack(side=tk.RIGHT, pady=10, padx=20)

        self.text_box = tk.Text(self.text_frame)
        self.text_box.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


        self.master.minsize(900, 800)
        self.text_box.config(width=800)


        master.bind("<Configure>", self.resize_text_box)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                text = file.read()
                self.text_box.delete("1.0", tk.END)
                self.text_box.insert("1.0", text)

    def save_file(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            with open(file_path, "w") as file:
                text = self.text_box.get("1.0", tk.END)
                file.write(text)

    def resize_text_box(self, event):
        self.text_frame.config(width=event.width-100)

root = tk.Tk()
text_editor = TextEditor(root)
root.mainloop()
