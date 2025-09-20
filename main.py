import os
import tkinter as tk
from tkinter import filedialog, messagebox
import translations
import json

SETTINGS_FILE = "settings.json"

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {"DefaultTargetFolder": "", "Language": "en_US"}

def save_settings(settings):
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=4)

settings = load_settings()

root = tk.Tk()
root.title("DB Mover")
root.geometry("500x300")

selected_file = tk.StringVar()
selected_folder = tk.StringVar(value=settings.get("DefaultTargetFolder", ""))

status_text = tk.Text(root, height=6)
status_text.config(state="disabled")

def update_status(message, color="black"):
    status_text.config(state="normal")
    status_text.delete(1.0, tk.END)
    status_text.insert(tk.END, message)
    status_text.config(fg=color)
    status_text.config(state="disabled")

def browse_file():
    file_path = filedialog.askopenfilename(
        title=translations.get_translation("Select DB File", settings.get("Language", "en_US")),
        filetypes=[("DB Files", "*.db")]
    )
    if file_path:
        selected_file.set(file_path)
        update_status(translations.get_translation("File selected", settings.get("Language", "en_US")) + ": " + file_path)

def browse_folder():
    folder_path = filedialog.askdirectory(
        title=translations.get_translation("Select Target Folder", settings.get("Language", "en_US"))
    )
    if folder_path:
        selected_folder.set(folder_path)
        update_status(translations.get_translation("Folder selected", settings.get("Language", "en_US")) + ": " + folder_path)
        settings["DefaultTargetFolder"] = folder_path
        save_settings(settings)

def move_file():
    file_path = selected_file.get()
    folder_path = selected_folder.get()
    if not file_path or not folder_path:
        update_status(translations.get_translation("Please select file and folder", settings.get("Language", "en_US")), "red")
        return
    try:
        filename = os.path.basename(file_path)
        dest_path = os.path.join(folder_path, filename)
        os.replace(file_path, dest_path)
        update_status(translations.get_translation("File moved successfully", settings.get("Language", "en_US")), "green")
    except Exception as e:
        update_status(translations.get_translation("Error moving file", settings.get("Language", "en_US")) + ": " + str(e), "red")

def open_settings():
    win = tk.Toplevel(root)
    win.title("Settings")
    win.geometry("300x250")

    tk.Label(win, text=translations.get_translation("Default Target Folder", settings.get("Language", "en_US"))).pack(pady=5)
    tk.Button(win, text=translations.get_translation("Browse Folder", settings.get("Language", "en_US")), command=browse_folder).pack(pady=5)

    tk.Label(win, text=translations.get_translation("Select Language", settings.get("Language", "en_US"))).pack(pady=5)
    lang_var = tk.StringVar(value=settings.get("Language", "en_US"))
    lang_menu = tk.OptionMenu(win, lang_var, "en_US", "fr_FR", "de_DE")
    lang_menu.pack(pady=5)

    def save_win_settings():
        settings["Language"] = lang_var.get()
        save_settings(settings)
        messagebox.showinfo("Info", translations.get_translation("Settings saved. Restart app for full effect.", settings.get("Language", "en_US")))
        win.destroy()

    tk.Button(win, text=translations.get_translation("Save", settings.get("Language", "en_US")), command=save_win_settings).pack(pady=20)

tk.Label(root, text=translations.get_translation("Select DB File", settings.get("Language", "en_US"))).pack()
tk.Button(root, text=translations.get_translation("Browse File", settings.get("Language", "en_US")), command=browse_file).pack(pady=5)

tk.Label(root, text=translations.get_translation("Select Target Folder", settings.get("Language", "en_US"))).pack()
tk.Button(root, text=translations.get_translation("Browse Folder", settings.get("Language", "en_US")), command=browse_folder).pack(pady=5)

tk.Button(root, text=translations.get_translation("Move File", settings.get("Language", "en_US")), command=move_file).pack(pady=5)
tk.Button(root, text="⚙", command=open_settings).pack(pady=5)

status_text.pack(fill="both", expand=True, pady=10)

root.mainloop()