import json
import time
import pyautogui
import keyboard
import threading
import pygetwindow as gw
from pynput import mouse

windows = gw.getWindowsWithTitle("Rise of Kingdoms")
if windows:
    win = windows[0]
    win.activate()  # Pastikan game window aktif dan focus
    print("Window game diaktifkan!")
else:
    print("Window game tidak ditemukan, cek nama window-nya.")

recording = []
is_recording = False
save_file = 'macro.json'
loop_playback = False  # Flag untuk looping playback

def on_click(x, y, button, pressed):
    if is_recording and pressed:
        timestamp = time.time()
        recording.append({'type': 'click', 'x': x, 'y': y, 'time': timestamp})

def on_move(x, y):
    if is_recording:
        timestamp = time.time()
        recording.append({'type': 'move', 'x': x, 'y': y, 'time': timestamp})
7
def record_mouse():
    global is_recording, recording
    recording.clear()
    is_recording = True
    print("🎥 Rekaman dimulai. Tekan '9' untuk stop dan simpan.")

    with mouse.Listener(on_click=on_click, on_move=on_move) as listener:
        keyboard.wait('9')
        is_recording = False
        listener.stop()

    if recording:
        base_time = recording[0]['time']
        for action in recording:
            action['time'] -= base_time

        with open(save_file, 'w') as f:
            json.dump(recording, f, indent=4)
        print(f"✅ Rekaman disimpan ke '{save_file}'")
    else:
        print("❌ Tidak ada aktivitas terekam.")

def playback_loop():
    global loop_playback
    try:
        with open(save_file, 'r') as f:
            actions = json.load(f)
    except FileNotFoundError:
        print(f"❌ File '{save_file}' tidak ditemukan.")
        return

    print("▶️ Playback berulang dimulai. Tekan '7' untuk berhenti.")
    loop_playback = True
    while loop_playback:
        last_time = 0
        for action in actions:
            if not loop_playback:
                break
            delay = action['time'] - last_time
            time.sleep(delay)
            if action['type'] == 'move':
                pyautogui.moveTo(action['x'], action['y'])
            elif action['type'] == 'click':
                pyautogui.click(action['x'], action['y'])
            last_time = action['time']
    print("⛔ Playback berhenti.")

def stop_loop():
    global loop_playback
    loop_playback = False

# Main loop
print("🔧 Tekan:")
print("  [8] Mulai rekam")
print("  [9] Stop & simpan")
print("  [0] Mulai playback loop")
print("  [7] Stop playback loop")

while True:
    if keyboard.is_pressed('8'):
        record_mouse()
        time.sleep(1)
    elif keyboard.is_pressed('0'):
        threading.Thread(target=playback_loop, daemon=True).start()
        time.sleep(1)
    elif keyboard.is_pressed('7'):
        stop_loop()
        time.sleep(0.5)
