import pymem
import time
import tkinter as tk
import pygame
import threading
import keyboard
from PIL import Image, ImageTk
from tkinter import messagebox

pygame.mixer.init()

initial_sound = "initial_sound.mp3"
toggle_sound = "toggle_sound.mp3"
deactivation_sound = "deactivation_sound.mp3"

exe_name = "pop3.exe"

health_address = 0x0FA80030
sandtanks_address = 0x0FB80A88
#slowmotion_address = 0x0FB80A88
#recall_address = 0x0FB80A88

cheats_enabled = {"health": False, "sandtanks": False, "slowmotion": False, "recall": False}

drag_data = {"x": 0, "y": 0, "dragging": False}

def modify_values():
    try:
        pm = pymem.Pymem(exe_name)
    except pymem.exception.ProcessNotFound:
        messagebox.showerror("Error", "Game not found! Please start the game first.")
        return

    while True:
        try:
            if cheats_enabled["health"]:
                pm.write_int(health_address, 400)
            if cheats_enabled["sandtanks"]:
                pm.write_int(sandtanks_address, 6)
            if cheats_enabled["slowmotion"]:
                pm.write_int(slowmotion_address, 6)
            if cheats_enabled["recall"]:
                pm.write_int(recall_address, 6)
        except Exception as e:
            print(f"Error modifying values: {e}")
        time.sleep(0.1)

def toggle_cheat(cheat_name):
    cheats_enabled[cheat_name] = not cheats_enabled[cheat_name]
    state = "Enabled" if cheats_enabled[cheat_name] else "Disabled"
    print(f"{cheat_name.capitalize()} {state}")

    # Play activation or deactivation sound
    try:
        if cheats_enabled[cheat_name]:
            pygame.mixer.music.load(toggle_sound)
        else:
            pygame.mixer.music.load(deactivation_sound)

        pygame.mixer.music.play()
    except pygame.error as e:
        print(f"Error playing sound: {e}")

def disable_all():
    for cheat in cheats_enabled:
        cheats_enabled[cheat] = False
    print("All cheats disabled")
    try:
        pygame.mixer.music.load(deactivation_sound)
        pygame.mixer.music.play()
    except pygame.error as e:
        print(f"Error playing sound: {e}")

def listen_for_keys():
    while True:
        try:
            if keyboard.is_pressed('F1'):
                toggle_cheat("health")
                time.sleep(0.3)  # Debounce
            elif keyboard.is_pressed('F2'):
                toggle_cheat("sandtanks")
                time.sleep(0.3)
            elif keyboard.is_pressed('F3'):
                toggle_cheat("slowmotion")
                time.sleep(0.3)
            elif keyboard.is_pressed('F4'):
                toggle_cheat("recall")
                time.sleep(0.3)
            elif keyboard.is_pressed('end'):
                disable_all()
                time.sleep(0.3)
        except Exception as e:
            print(f"Error listening for keys: {e}")

def start_drag(event):
    drag_data["x"] = event.x_root
    drag_data["y"] = event.y_root
    drag_data["dragging"] = True

def on_drag(event):
    if drag_data["dragging"]:
        x = root.winfo_x() + (event.x_root - drag_data["x"])
        y = root.winfo_y() + (event.y_root - drag_data["y"])
        root.geometry(f"+{x}+{y}")
        drag_data["x"] = event.x_root
        drag_data["y"] = event.y_root

def stop_drag(event):
    drag_data["dragging"] = False

def close_window():
    root.quit()

root = tk.Tk()
root.geometry("256x357")  # Window size
root.overrideredirect(True)  # Remove default title bar and border
root.attributes('-alpha', 0.9)  # Slightly transparent window (85% opacity)

canvas = tk.Canvas(root, width=256, height=357, highlightthickness=0, borderwidth=0)
canvas.pack()

# Load and set the background image (replace 'background.png' with your image path)
try:
    bg_image = Image.open("background.png")  # Update with your background image path
    bg_image = bg_image.resize((256, 357), Image.Resampling.LANCZOS)  # Adjusted size to match window
    bg_photo = ImageTk.PhotoImage(bg_image)
    canvas.create_image(128, 178.5, image=bg_photo)  # Center the image (256/2, 357/2)
except Exception as e:
    print(f"Error loading background image: {e}")

quit_button = tk.Button(canvas, text="quit", command=close_window, bg="#F44336", fg="white",
                        font=("Arial", 9, "bold"), width=6, height=1, activebackground="#F44336", highlightthickness=0)
quit_button.place(x=203, y=332)  # Position in the bottom-right corner

root.bind("<Button-1>", start_drag)
root.bind("<B1-Motion>", on_drag)
root.bind("<ButtonRelease-1>", stop_drag)

# Play the initial sound at the start of the program
try:
    pygame.mixer.music.load(initial_sound)
    pygame.mixer.music.play()
except pygame.error as e:
    print(f"Error playing initial sound: {e}")

# Start the modification in a separate thread
thread = threading.Thread(target=modify_values, daemon=True)
thread.start()

# Start the key listening thread
keyboard_thread = threading.Thread(target=listen_for_keys, daemon=True)
keyboard_thread.start()

root.mainloop()
