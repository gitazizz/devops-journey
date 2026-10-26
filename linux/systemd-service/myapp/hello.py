import time

while True:
    try:
        print("Mon premier service sur linux!")
        time.sleep(5)
    except KeyboardInterrupt:
        print()
        break