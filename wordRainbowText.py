import time
import sys

colors = [
    "\033[91m",  # Red
    "\033[93m",  # Yellow
    "\033[92m",  # Green
    "\033[96m",  # Cyan
    "\033[94m",  # Blue
    "\033[95m"   # Magenta
]

reset_color = "\033[0m"

text = "Try this next"

for shift in range(50):  # Move colors along the text
    output = ""
    for idx, char in enumerate(text):
        color = colors[(shift + idx) % len(colors)]
        output += color + char
    sys.stdout.write(output + reset_color + "\r")
    sys.stdout.flush()
    time.sleep(0.1)