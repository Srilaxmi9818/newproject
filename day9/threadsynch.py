import threading

# Define a condition for synchronization
condition = threading.Condition()

# Variable to track the current number
current_number = 1

def print_odd_numbers():
    global current_number
    while current_number <= 9:
        with condition:
            if current_number % 2 == 0:  # If the number is even, wait
                condition.wait()
            print(current_number)
            current_number += 1
            condition.notify()  # Notify the other thread

def print_even_numbers():
    global current_number
    while current_number <= 10:
        with condition:
            if current_number % 2 == 1:  # If the number is odd, wait
                condition.wait()
            print(current_number)
            current_number += 1
            condition.notify()  # Notify the other thread

# Create threads
thread_odd = threading.Thread(target=print_odd_numbers)
thread_even = threading.Thread(target=print_even_numbers)

# Start threads
thread_odd.start()
thread_even.start()

# Wait for threads to finish
thread_odd.join()
thread_even.join()

print("Numbers printed successfully.")
