import msvcrt
from datetime import datetime

print("🔐 Ethical Keylogger Demo (Windows)")
print("Press keys to log them")
print("Press ESC to stop\n")

with open("key_log.txt", "a") as file:
    file.write("\n--- Logging started at {} ---\n".format(datetime.now()))

    while True:
        key = msvcrt.getch()

        # ESC key
        if key == b'\x1b':
            print("\nLogging stopped.")
            file.write("\n--- Logging stopped ---\n")
            break

        try:
            char = key.decode('utf-8')
            print(char, end="", flush=True)
            file.write(char)
        except:
            file.write("[SPECIAL_KEY]")

        file.flush()
