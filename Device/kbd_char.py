import evdev

# Open the device file for the keyboard
device = evdev.InputDevice('/dev/input/by-id/usb-0513_0318-event-kbd')

# Decode the event code into a key symbol
def decode_event(event):
    return evdev.ecodes.KEY[event.code]

# Read events from the keyboard
for event in device.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        key = decode_event(event)
        print(key)
