import tkinter as tk
import threading
from assistant_core import speak, listen_voice, process_command

# ---------- Functions ----------

def start_voice():
    status_label.config(text="🎤 Listening...", fg="#ff9800")
    threading.Thread(target=voice_command).start()

def voice_command():
    command = listen_voice()
    if command:
        entry.delete(0, tk.END)
        entry.insert(0, command)
        handle_command(command)
    else:
        status_label.config(text="❌ Voice not detected", fg="red")

def text_command():
    command = entry.get().lower()
    handle_command(command)

def handle_command(command):
    response = process_command(command)
    if response == "exit":
        speak("Goodbye")
        app.destroy()
    else:
        output_label.config(text=response)
        speak(response)
        status_label.config(text="✅ Ready", fg="#4caf50")

# ---------- GUI Design ----------

app = tk.Tk()
app.title("SARA – Hybrid AI Assistant")
app.geometry("500x380")
app.configure(bg="#1e1e2f")
app.resizable(False, False)

# Header
header = tk.Label(
    app,
    text="🤖 SARA AI ASSISTANT",
    font=("Segoe UI", 18, "bold"),
    bg="#673ab7",
    fg="white",
    pady=10
)
header.pack(fill="x")

# Subtitle
sub = tk.Label(
    app,
    text="Voice + Text Hybrid System",
    font=("Segoe UI", 11),
    bg="#1e1e2f",
    fg="#bbbbbb"
)
sub.pack(pady=10)

# Entry box
entry = tk.Entry(
    app,
    font=("Segoe UI", 12),
    width=40,
    bd=0,
    relief="flat"
)
entry.pack(pady=10, ipady=6)

# Buttons frame
btn_frame = tk.Frame(app, bg="#1e1e2f")
btn_frame.pack(pady=10)

voice_btn = tk.Button(
    btn_frame,
    text="🎤 Speak",
    font=("Segoe UI", 11, "bold"),
    bg="#ff9800",
    fg="white",
    width=14,
    bd=0,
    command=start_voice
)
voice_btn.grid(row=0, column=0, padx=10)

text_btn = tk.Button(
    btn_frame,
    text="⌨️ Submit",
    font=("Segoe UI", 11, "bold"),
    bg="#03a9f4",
    fg="white",
    width=14,
    bd=0,
    command=text_command
)
text_btn.grid(row=0, column=1, padx=10)

# Output box
output_label = tk.Label(
    app,
    text="👋 Hello! I am SARA.",
    font=("Segoe UI", 12),
    bg="#2a2a40",
    fg="white",
    wraplength=460,
    pady=15
)
output_label.pack(fill="x", padx=20, pady=15)

# Status bar
status_label = tk.Label(
    app,
    text="✅ Ready",
    font=("Segoe UI", 10),
    bg="#1e1e2f",
    fg="#4caf50"
)
status_label.pack(side="bottom", pady=10)

app.mainloop()
