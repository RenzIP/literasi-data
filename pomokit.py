import pyautogui # pip install pyautogui
import threading
import time
import keyboard  # pip install keyboard

# Variabel kontrol
running = True

def mouse_loop():
    global running
    while running:
        # Gerakan zig-zag
        pyautogui.moveRel(100, 0, duration=0.2)
        pyautogui.moveRel(0, 100, duration=0.2)
        pyautogui.moveRel(-100, 0, duration=0.2)
        pyautogui.moveRel(0, -100, duration=0.2)
        time.sleep(0.1)  # Sedikit jeda

def hotkey_listener():
    global running
    keyboard.wait('esc')  # Tunggu hingga tombol ESC ditekan
    print("\n[!] ESC ditekan. Program dihentikan.")
    running = False

# Jalankan listener di thread terpisah
threading.Thread(target=hotkey_listener, daemon=True).start()

# Mulai loop mouse
print("Gerakan mouse dimulai. Tekan 'ESC' untuk berhenti.")
mouse_loop()
