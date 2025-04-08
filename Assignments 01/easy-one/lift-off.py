import time
import sys


def lift_off():
    """Countdown from 10 to 1 before launching."""
    for num in range(10, 0, -1):
        print(f"\rTik Tik: {num} ", end="", flush=True)
        time.sleep(1)

    print("\n🚀 Lift off!")


lift_off()
