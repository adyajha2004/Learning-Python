import time
import sys

# defining colors
colors = [
    "\033[91m",  # Red
    "\033[93m",  # Yellow
    "\033[92m",  # Green
    "\033[96m",  # Cyan
    "\033[94m",  # Blue
    "\033[95m"   # Magenta
]
white = "\033[37m"
reset = "\033[0m"

# choosing text to print
text = "Can you do this in python??"

# loop to change color
for j in range(100):
    i = j % len(colors)
    sys.stdout.write(colors[i] + text + reset + "\r")
    sys.stdout.flush()
    time.sleep(0.2)

# final white print
sys.stdout.write(white + text + reset + "\r")