import os
import sys
import tkinter as tk
import json
# Configuration
args = sys.argv[1:]

root = tk.Tk()
root.title("MonikA.I. Submod")
root.geometry("900x500")
root.configure(background='#333333')


def get_input():
    global GAME_PATH
    global WEBUI_PATH
    global USE_TTS
    global LAUNCH_YOURSELF
    global LAUNCH_YOURSELF_WEBUI
    global USE_ACTIONS
    global TTS_MODEL
    global USE_SPEECH_RECOGNITION
    global VOICE_SAMPLE_TORTOISE
    global VOICE_SAMPLE_COQUI
    USE_TTS = use_tts.get()
    GAME_PATH = game_path.get()
    WEBUI_PATH = webui_path.get()
    LAUNCH_YOURSELF = launch_yourself.get()
    LAUNCH_YOURSELF_WEBUI = launch_yourself_webui.get()
    USE_ACTIONS = use_actions.get()
    TTS_MODEL = tts_model.get()
    USE_SPEECH_RECOGNITION = use_speech_recognition.get()
    VOICE_SAMPLE_TORTOISE = voice_sample_tortoise.get()
    VOICE_SAMPLE_COQUI = voice_sample_coqui.get()
    root.destroy()


other_frame = tk.LabelFrame(
    root,
    bg='#333333',
    text="General Settings",
    fg='white',
    font=("Helvetica", 16)
)
other_frame.grid(row=5, column=0)

use_tts = tk.StringVar()
game_path = tk.StringVar()
webui_path = tk.StringVar()
launch_yourself = tk.StringVar()
launch_yourself_webui = tk.StringVar()
use_actions = tk.StringVar()
tts_model = tk.StringVar()
use_speech_recognition = tk.StringVar()
voice_sample_tortoise = tk.StringVar()
voice_sample_coqui = tk.StringVar()
character_json = tk.StringVar()

# General Settings
tk.Label(other_frame, text="Game Path", bg='#333333', fg='white').grid(row=1, column=0)
tk.Label(other_frame, text="Launch Yourself", bg='#333333', fg='white').grid(row=1, column=3)
tk.Label(other_frame, text="Use Actions", bg='#333333', fg='white').grid(row=2, column=0)
tk.Label(other_frame, text="Use TTS", bg='#333333', fg='white').grid(row=3, column=0)
tk.Label(other_frame, text="TTS model", bg='#333333', fg='white').grid(row=3, column=3)
tk.Label(other_frame, text="Use Speech Recognition", bg='#333333', fg='white').grid(row=6, column=0)
tk.Label(other_frame, text="Voice Sample (Tortoise)", bg='#333333', fg='white').grid(row=7, column=0)
tk.Label(other_frame, text="Voice Sample (Your TTS)", bg='#333333', fg='white').grid(row=7, column=3)
tk.Label(other_frame, text="WebUI Path", bg='#333333', fg='white').grid(row=9, column=0)
tk.Label(other_frame, text="Launch Yourself", bg='#333333', fg='white').grid(row=9, column=3)

# Textual Inputs
tk.Entry(other_frame, textvariable=game_path, width=25).grid(row=1, column=1)
tk.Entry(other_frame, textvariable=webui_path, width=25).grid(row=9, column=1)

tts_menu = tk.OptionMenu(other_frame, tts_model, "Your TTS", "Tortoise TTS")
tts_menu.config(bg='white', fg='black')
tts_menu.grid(row=3, column=4)

all_voices_tortoise = os.listdir("tortoise_audios")
all_voices_tortoise = [x for x in all_voices_tortoise if not x.endswith(".txt")]
voice_menu = tk.OptionMenu(other_frame, voice_sample_tortoise, *all_voices_tortoise)
voice_menu.config(bg='white', fg='black')
voice_menu.grid(row=8, column=1)

all_voices_coquiai = os.listdir("coquiai_audios")
all_voices_coquiai = [x for x in all_voices_coquiai if x.endswith(".wav")]
if len(all_voices_coquiai) == 0:
    all_voices_coquiai = ["No voices found"]
voice_menu = tk.OptionMenu(other_frame, voice_sample_coqui, *all_voices_coquiai)
voice_menu.config(bg='white', fg='black')
voice_menu.grid(row=8, column=4)

aspect_params = {
    "bg": '#333333',
    "activeforeground": 'white',
    "fg": 'white',
    "activebackground": "#333333",
    "selectcolor": '#333333'
}

tk.Radiobutton(other_frame, text="Yes", variable=launch_yourself, value=True, **aspect_params).grid(row=1, column=4)
tk.Radiobutton(other_frame, text="No", variable=launch_yourself, value=False, **aspect_params).grid(row=1, column=5)

tk.Radiobutton(other_frame, text="Yes", variable=use_actions, value=True, **aspect_params).grid(row=2, column=1)
tk.Radiobutton(other_frame, text="No", variable=use_actions, value=False, **aspect_params).grid(row=2, column=2)

tk.Radiobutton(other_frame, text="Yes", variable=use_tts, value=True, **aspect_params).grid(row=3, column=1)
tk.Radiobutton(other_frame, text="No", variable=use_tts, value=False, **aspect_params).grid(row=3, column=2)

tk.Radiobutton(other_frame, text="Yes", variable=use_speech_recognition, value=True, **aspect_params).grid(row=6, column=1)
tk.Radiobutton(other_frame, text="No", variable=use_speech_recognition, value=False, **aspect_params).grid(row=6, column=2)

tk.Radiobutton(other_frame, text="Yes", variable=launch_yourself_webui, value=True, **aspect_params).grid(row=9, column=4)
tk.Radiobutton(other_frame, text="No", variable=launch_yourself_webui, value=False, **aspect_params).grid(row=9, column=5)

button = tk.Button(root, text="Submit", command=get_input, bg='#FF3399', fg='white')
button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

if not os.path.exists("config.json"):
    # Set default values
    launch_yourself.set(0)
    launch_yourself_webui.set(0)
    use_tts.set(0)
    use_actions.set(0)
    tts_model.set("Your TTS")
    use_speech_recognition.set(0)
    voice_sample_tortoise.set("Choose a Tortoise voice sample")
    voice_sample_coqui.set("Choose a YourTTS voice sample")
else:
    with open("config.json", "r") as f:
        config = json.load(f)
    GAME_PATH = config["GAME_PATH"]
    WEBUI_PATH = config["WEBUI_PATH"]
    USE_TTS = config["USE_TTS"]
    LAUNCH_YOURSELF = config["LAUNCH_YOURSELF"]
    LAUNCH_YOURSELF_WEBUI = config["LAUNCH_YOURSELF"]
    USE_ACTIONS = config["USE_ACTIONS"]
    TTS_MODEL = config["TTS_MODEL"]
    USE_SPEECH_RECOGNITION = config["USE_SPEECH_RECOGNITION"]
    VOICE_SAMPLE_TORTOISE = config["VOICE_SAMPLE_TORTOISE"]
    VOICE_SAMPLE_COQUI = config["VOICE_SAMPLE_COQUI"]
    # Set saved values
    launch_yourself.set(LAUNCH_YOURSELF)
    launch_yourself_webui.set(LAUNCH_YOURSELF_WEBUI)
    use_tts.set(USE_TTS)
    use_actions.set(USE_ACTIONS)
    tts_model.set(TTS_MODEL)
    use_speech_recognition.set(USE_SPEECH_RECOGNITION)
    voice_sample_tortoise.set(VOICE_SAMPLE_TORTOISE)
    voice_sample_coqui.set(VOICE_SAMPLE_COQUI)


def on_closing():
    root.destroy()
    raise SystemExit


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()

# Convert string to int (0 or 1, False or True)
USE_TTS = int(USE_TTS)
LAUNCH_YOURSELF = int(LAUNCH_YOURSELF)
LAUNCH_YOURSELF_WEBUI = int(LAUNCH_YOURSELF_WEBUI)
USE_ACTIONS = int(USE_ACTIONS)
USE_SPEECH_RECOGNITION = int(USE_SPEECH_RECOGNITION)

CONFIG = {
    "GAME_PATH": GAME_PATH,
    "WEBUI_PATH": WEBUI_PATH,
    "USE_TTS": USE_TTS,
    "LAUNCH_YOURSELF": LAUNCH_YOURSELF,
    "LAUNCH_YOURSELF_WEBUI": LAUNCH_YOURSELF_WEBUI,
    "USE_ACTIONS": USE_ACTIONS,
    "TTS_MODEL": TTS_MODEL,
    "USE_SPEECH_RECOGNITION": USE_SPEECH_RECOGNITION,
    "VOICE_SAMPLE_TORTOISE": VOICE_SAMPLE_TORTOISE,
    "VOICE_SAMPLE_COQUI": VOICE_SAMPLE_COQUI,
}

with open("config.json", "w") as f:
    json.dump(CONFIG, f)