import ctypes
import threading
import time
import tkinter as tk
from tkinter import messagebox, scrolledtext
from typing import List

class CNTApp:
    def __init__(self):
        self.m_wndMain = None
        self.m_wndStatus = None
        self.m_wndAbout = None

theApp = CNTApp()

class CAboutDlg:
    def __init__(self, parent):
        self.parent = parent
        self.dialog = tk.Toplevel(parent)
        self.on_init_dialog()

    def on_init_dialog(self):
        version = f"{SPHERE_TITLE} {SPHERE_VERSION}"
        compiled_at = f"Compiled at {__DATE__} ({__TIME__})"
        tk.Label(self.dialog, text=version).pack()
        tk.Label(self.dialog, text=compiled_at).pack()
        tk.Button(self.dialog, text="OK", command=self.dialog.destroy).pack()

class CStatusDlg:
    def __init__(self, parent):
        self.parent = parent
        self.dialog = tk.Toplevel(parent)
        self.client_list = tk.Listbox(self.dialog)
        self.client_list.pack()
        self.stats_list = tk.Listbox(self.dialog)
        self.stats_list.pack()
        self.on_init_dialog()

    def fill_clients(self):
        self.client_list.delete(0, tk.END)
        self.client_list.insert(tk.END, *g_Serv.list_clients())

    def fill_stats(self):
        self.stats_list.delete(0, tk.END)
        stats = g_Serv.list_stats()
        for stat in stats:
            self.stats_list.insert(tk.END, stat)

    def on_init_dialog(self):
        self.fill_clients()
        self.fill_stats()

class CListTextConsole:
    def __init__(self, hWndList):
        self.m_wndList = tk.Listbox(hWndList)
    
    def get_priv_level(self):
        return "Admin"
    
    def get_name(self):
        return "Stats"
    
    def sys_message(self, psz_message):
        if not psz_message:
            return
        messages = psz_message.split('\n')
        for message in messages:
            if message:
                self.m_wndList.insert(tk.END, message)

class CNTWindow(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.window = None
        self.log = None
        self.input = None
        self.init_params = {}
        self.log_text_len = 0
        self.log_scroll_lock = False
        self.color_new = "#afafaf"
        self.color_prev = "#afafaf"
        self.height_input = 0
        self.log_font = "Courier"
        self.commands = ["" for _ in range(5)]
        self.new_window_title = False
        self._str_window_title = ""
        self._f_new_window_title = False
        self._mutex_window_title = threading.Lock()

    def run(self):
        self.on_start()

    def on_start(self):
        self.window = tk.Tk()
        self.window.title(SPHERE_WINDOW_TITLE_BASE)
        self.window.geometry("800x600")

        self.log = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, font=(self.log_font, 10), bg="black", fg=self.color_prev)
        self.log.pack(expand=True, fill=tk.BOTH)

        self.input = tk.Entry(self.window)
        self.input.pack(fill=tk.X)

        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.window.bind("<Return>", self.on_enter_pressed)
        self.window.bind("<Up>", self.on_up_pressed)

        self.update_window_title()
        self.window.mainloop()

    def on_enter_pressed(self, event):
        self.on_command(0, IDOK, None)

    def on_up_pressed(self, event):
        self.input.delete(0, tk.END)
        self.input.insert(0, self.commands[0])
        self.commands = self.commands[1:] + [self.commands[0]]

    def on_close(self):
        if g_Serv.get_exit_flag() == 0:
            if messagebox.askyesno(theApp.m_pszAppName, "Are you sure you want to close the server?"):
                self.window.destroy()
                return True
            return False
        else:
            self.window.destroy()
            return True

    def update_window_title(self):
        with self._mutex_window_title:
            if not self._f_new_window_title:
                return

            mode = {
                SERVMODE_RESTOCK_ALL: "Restocking",
                SERVMODE_GARBAGE_COLLECTION: "Collecting Garbage",
                SERVMODE_SAVING: "Saving",
                SERVMODE_RUN: "Running",
                SERVMODE_PRE_LOADING_INI: "Pre-Loading INI",
                SERVMODE_LOADING: "Loading",
                SERVMODE_RESYNC_PAUSE: "Resync Pause",
                SERVMODE_RESYNC_LOAD: "Resync Load",
                SERVMODE_EXITING: "Exiting"
            }.get(g_Serv.get_server_mode(), "Unknown")

            title = f"{theApp.m_pszAppName} - {g_Serv.get_name()} ({mode}) {self._str_window_title}"
            self.window.title(title)
            self._str_window_title = ""
            self._f_new_window_title = False

    def on_command(self, w_notify_code, w_id, hwnd_ctl):
        if w_id == IDOK and not g_Serv.m_f_console_text_ready_flag:
            self.commands = [self.input.get()] + self.commands[:-1]
            g_Serv.m_s_console_text = self.input.get()
            self.input.delete(0, tk.END)
            g_Serv.m_f_console_text_ready_flag = True
            return True
        return False

    def tick(self):
        self.update_window_title()
        self.window.update()

    def set_window_title(self, p_text=None):
        with self._mutex_window_title:
            self._str_window_title = p_text if p_text else ""
            self._f_new_window_title = True

g_Serv = None  # Mock the global server object
SPHERE_TITLE = "Sphere"
SPHERE_VERSION = "1.0"
SPHERE_WINDOW_TITLE_BASE = f"{SPHERE_TITLE} {SPHERE_VERSION}"
SERVMODE_RESTOCK_ALL = 1
SERVMODE_GARBAGE_COLLECTION = 2
SERVMODE_SAVING = 3
SERVMODE_RUN = 4
SERVMODE_PRE_LOADING_INI = 5
SERVMODE_LOADING = 6
SERVMODE_RESYNC_PAUSE = 7
SERVMODE_RESYNC_LOAD = 8
SERVMODE_EXITING = 9
IDOK = 1
IDCANCEL = 2

if __name__ == "__main__":
    theApp.m_wndMain = CNTWindow()
    theApp.m_wndMain.start()
