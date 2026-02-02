import tkinter as tk
from tkinter import ttk, messagebox

from speech_to_text import speech_to_text
from translator import translate_text
from text_to_speech import text_to_speech
from speaker_recognition import speaker_recognition

# ---------------- UI FUNCTIONS ---------------- #

def record_speech():
    status.set("Listening...")
    text = speech_to_text()
    recognized_text.set(text)
    status.set("Speech recognized successfully")

def translate_text_ui():
    if not recognized_text.get():
        messagebox.showwarning("Warning", "Please record speech first")
        return

    lang_code = languages[language_choice.get()]
    translated = translate_text(recognized_text.get(), lang_code)
    translated_text.set(translated)
    status.set("Translation completed")

def play_audio():
    if not translated_text.get():
        messagebox.showwarning("Warning", "No translated text available")
        return
    text_to_speech(translated_text.get())
    status.set("Playing audio output")

def verify_speaker():
    result = speaker_recognition()
    messagebox.showinfo("Speaker Verification", result)
    status.set("Speaker verification completed")

# ---------------- MAIN UI ---------------- #

root = tk.Tk()
root.title("Multi-Language Speech Application")
root.geometry("600x500")
root.configure(bg="#f4f6f8")

# Variables
recognized_text = tk.StringVar()
translated_text = tk.StringVar()
status = tk.StringVar(value="Ready")

languages = {
    "Hindi": "hi",
    "English": "en",
    "French": "fr",
    "Japanese": "ja",
    "Spanish": "es"
}

language_choice = tk.StringVar(value="Hindi")

# ---------------- UI COMPONENTS ---------------- #

tk.Label(
    root,
    text="Speech Translation Application",
    font=("Arial", 18, "bold"),
    bg="#f4f6f8"
).pack(pady=10)

# Recognized Text
tk.Label(root, text="Recognized Text").pack()
tk.Entry(root, textvariable=recognized_text, width=70).pack(pady=5)

# Buttons
tk.Button(root, text="🎙 Speak", width=20, command=record_speech).pack(pady=5)

# Language Selection
tk.Label(root, text="Select Target Language").pack()
ttk.Combobox(
    root,
    textvariable=language_choice,
    values=list(languages.keys()),
    state="readonly"
).pack(pady=5)

tk.Button(root, text="🌐 Translate", width=20, command=translate_text_ui).pack(pady=5)

# Translated Text
tk.Label(root, text="Translated Text").pack()
tk.Entry(root, textvariable=translated_text, width=70).pack(pady=5)

tk.Button(root, text="🔊 Play Audio", width=20, command=play_audio).pack(pady=5)

tk.Button(root, text="🧑‍💼 Verify Speaker", width=20, command=verify_speaker).pack(pady=5)

# Status Bar
tk.Label(
    root,
    textvariable=status,
    relief="sunken",
    anchor="w"
).pack(fill="x", side="bottom")

root.mainloop()
