import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class SphereMainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PySphere")
        self.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        # Menu bar
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.quit)

        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about_dialog)

        # Status bar
        self.status = tk.Label(self, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

    def show_about_dialog(self):
        AboutDialog(self)

class AboutDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("About PySphere")
        self.geometry("400x200")

        version_label = tk.Label(self, text="Version: PySphere X.Y.Z")
        version_label.pack(pady=10)

        compiler_label = tk.Label(self, text="Compiled at: YYYY-MM-DD")
        compiler_label.pack(pady=10)

        credits = (
            "This software makes use of:\n"
            "DEELX Regular Expression Engine (v1.2)\n"
            "Copyright (C) 2006 RegExLab.com\n"
            "libev library (v4.22)\n"
            "General Public License v2 (GPLv2) 2007-2013 Marc Alexander Lehmann\n"
            "MySQL (v5.7)\n"
            "General Public License v2 (GPLv2) 2000-2016 Oracle\n"
            "SQLite (v3.33.0)\n"
            "General Public License (GPL) 2000-2020\n"
            "Twofish encryption library (v1.0)\n"
            "Copyright (C) 1998 Bruce Schneier, Doug Whiting, John Kelsey, Chris Hall, David Wagner\n"
            "Zlib data compression library (v1.2.11)\n"
            "Copyright (C) 1995-2017 Jean-loup Gailly, Mark Adler"
        )

        credits_label = tk.Label(self, text=credits, justify=tk.LEFT)
        credits_label.pack(pady=10)

        close_button = tk.Button(self, text="Close", command=self.destroy)
        close_button.pack(pady=10)

def main():
    app = SphereMainWindow()
    app.mainloop()

if __name__ == '__main__':
    main()
