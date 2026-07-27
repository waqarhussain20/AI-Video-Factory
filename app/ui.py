import tkinter as tk
from tkinter import ttk, messagebox


def generate_video():
    script = script_box.get("1.0", tk.END).strip()

    if not script:
        messagebox.showwarning("Warning", "Please paste your script first!")
        return

    status.config(text="Status: Script Loaded ✅")


def run_app():
    global script_box, status

    root = tk.Tk()
    root.title("AI Video Factory")
    root.geometry("1000x700")
    root.configure(bg="#f2f2f2")

    title = tk.Label(
        root,
        text="AI VIDEO FACTORY",
        font=("Arial", 24, "bold"),
        bg="#f2f2f2"
    )
    title.pack(pady=20)

    tk.Label(
        root,
        text="Paste Your Script",
        font=("Arial", 12),
        bg="#f2f2f2"
    ).pack()

    script_box = tk.Text(
        root,
        width=100,
        height=18,
        font=("Arial", 11)
    )
    script_box.pack(pady=10)

    generate_btn = ttk.Button(
        root,
        text="🚀 Generate Video",
        command=generate_video
    )
    generate_btn.pack(pady=15)

    status = tk.Label(
        root,
        text="Status: Ready",
        font=("Arial", 11),
        bg="#f2f2f2",
        fg="blue"
    )
    status.pack(pady=10)

    root.mainloop()