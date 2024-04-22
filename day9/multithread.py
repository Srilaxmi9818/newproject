import threading
import time

def countdown(timer_name, seconds):
    print(f"{timer_name} started.")
    while seconds > 0:
        print(f"{timer_name}: {seconds} seconds remaining.")
        time.sleep(1)
        seconds -= 1
    print(f"{timer_name} finished.")

# Define the countdown times
time1 = 10
time2 = 20

# Create threads for each countdown timer
thread1 = threading.Thread(target=countdown, args=("Timer 1", time1))
thread2 = threading.Thread(target=countdown, args=("Timer 2", time2))

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both timers finished.")
