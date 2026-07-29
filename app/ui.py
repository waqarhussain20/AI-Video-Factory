import tkinter as tk
from tkinter import ttk, messagebox
from app.controller import generate


def generate_video():
    script = script_box.get("1.0", tk.END).strip()

    if not script:
        messagebox.showwarning(
            "Warning",
            "Please paste your script first!"
        )
        return

    selected_voice = voice.get()
    selected_quality = quality.get()
    selected_language = language.get()
    selected_aspect = aspect.get()

    print("\n========== USER SETTINGS ==========")
    print("Voice:", selected_voice)
    print("Quality:", selected_quality)
    print("Language:", selected_language)
    print("Aspect:", selected_aspect)
    print("===================================")

    generate(
        script=script,
        voice=selected_voice,
        quality=selected_quality,
        language=selected_language,
        aspect=selected_aspect
    )

    status.config(text="Status: Video Generated ✅")


def run_app():
    global script_box, status
    global voice, quality, language, aspect

    root = tk.Tk()
    root.title("AI VIDEO FACTORY")
    root.geometry("1000x700")
    root.configure(bg="#f4f4f4")

    # =========================
    # Title
    # =========================

    title = tk.Label(
        root,
        text="AI VIDEO FACTORY",
        font=("Segoe UI", 22, "bold"),
        bg="#f4f4f4"
    )
    title.pack(pady=15)

    # =========================
    # Script
    # =========================

    tk.Label(
        root,
        text="Paste Your Script",
        font=("Segoe UI", 11, "bold"),
        bg="#f4f4f4"
    ).pack()

    script_box = tk.Text(
        root,
        width=100,
        height=15,
        font=("Segoe UI", 10)
    )
    script_box.pack(pady=10)

    # =========================
    # Options
    # =========================

    options = tk.Frame(root, bg="#f4f4f4")
    options.pack(pady=10)

    # =========================
    # Voice
    # =========================

    tk.Label(
        options,
        text="Voice",
        bg="#f4f4f4"
    ).grid(row=0, column=0, padx=10)

    voice = ttk.Combobox(
        options,
        values=[
            "Male",
            "Female"
        ],
        width=15,
        state="readonly"
    )

    voice.current(0)
    voice.grid(row=1, column=0)

    # =========================
    # Quality
    # =========================

    tk.Label(
        options,
        text="Quality",
        bg="#f4f4f4"
    ).grid(row=0, column=1, padx=20)

    quality = ttk.Combobox(
        options,
        values=[
            "Fast",
            "High"
        ],
        width=15,
        state="readonly"
    )

    quality.current(0)
    quality.grid(row=1, column=1)

    # =========================
    # Language
    # =========================

    tk.Label(
        options,
        text="Language",
        bg="#f4f4f4"
    ).grid(row=0, column=2, padx=20)

    language = ttk.Combobox(
        options,
        values=[
            "🇺🇸 English",
            "🇵🇰 Urdu",
            "🇪🇸 Spanish"
        ],
        width=18,
        state="readonly"
    )

    language.current(0)
    language.grid(row=1, column=2)

    # =========================
    # Aspect Ratio
    # =========================

    tk.Label(
        options,
        text="Aspect Ratio",
        bg="#f4f4f4"
    ).grid(row=0, column=3, padx=20)

    aspect = ttk.Combobox(
        options,
        values=[
            "16:9 YouTube",
            "9:16 Shorts"
        ],
        width=18,
        state="readonly"
    )

    aspect.current(0)
    aspect.grid(row=1, column=3)

    # =========================
    # Progress
    # =========================

    progress = ttk.Progressbar(
        root,
        length=500,
        mode="determinate"
    )
    progress.pack(pady=20)

    # =========================
    # Generate Button
    # =========================

    ttk.Button(
        root,
        text="🚀 Generate Video",
        command=generate_video
    ).pack()

    # =========================
    # Status
    # =========================

    status = tk.Label(
        root,
        text="Status: Ready",
        bg="#f4f4f4",
        fg="blue",
        font=("Segoe UI", 10)
    )
    status.pack(pady=15)

    root.mainloop()