import time
import random
import threading
from game_data import data

VS = """
                                            ██╗   ██╗███████╗
                                            ██║   ██║██╔════╝
                                            ██║   ██║███████╗
                                            ╚██╗ ██╔╝╚════██║
                                            ╚████╔╝ ███████║
                                            ╚═══╝  ╚══════╝             
"""

user_input_storage = []
input_received_event = threading.Event()

START_INDEX1, START_INDEX2 = random.randint(0, 44), random.randint(0, 44)

def get_user_input():
    """Function to run in a separate thread to get user input."""
    try:
        user_choice = input("> ").upper()
        user_input_storage.append(user_choice)
        input_received_event.set()
    except EOFError:
        pass

def countdown(seconds: int):
    """
    Presents a live timer and waits for user input within the alloted time.
    Returns the user's choice or an empty string if time runs out.
    """
    global user_input_storage
    user_input_storage = []
    input_received_event.clear()

    input_thread = threading.Thread(target=get_user_input)
    input_thread.daemon = True
    input_thread.start()

    start_time = time.time()

    print()

    while time.time() - start_time < seconds:
        if input_received_event.is_set():
            break

        remaining_time = seconds - int(time.time() - start_time)
        if remaining_time < 0:
            remaining_time = 0
        
        mins, secs = divmod(remaining_time, 60)
        timer_display = f"Time left: {mins:02d}:{secs:02d}"
        print(timer_display, end="\r", flush=True)
        time.sleep(0.1)

    if input_received_event.is_set() and user_input_storage:
        input_thread.join(timeout=0.1)
        return user_input_storage[0]
    else:
        print("\nTime's up!                ")
        return ""

def get_correct_choice(entry1: dict, entry2: dict) -> str:
    return "A" if entry1["follower_count"] > entry2["follower_count"] else "B"  

def play_round(countdown_time, index1=START_INDEX1, index2=START_INDEX2) -> bool:
    entry1 = data[index1]
    entry2 = data[index2]
    correct_choice = get_correct_choice(entry1, entry2)
    print()
    if entry1['name'][0] not in "aeiou":
        print(f"Compare A: {entry1['name'].upper()}, a {entry1['description']} from {entry1['country']}.".center(100))
    else:
        print(f"Compare A: {entry1['name'].upper()}, an {entry1['description']} from {entry1['country']}.".center(100))
    
    print()
    print(VS.center(100))
    print()

    if entry2['name'][0] not in "aeiou":
        print(f"Against B: {entry2['name'].upper()}, a {entry2['description']} from {entry2['country']}.".center(100))
    else:
        print(f"Against B: {entry2['name'].upper()}, an {entry2['description']} from {entry2['country']}.".center(100))

    print()
    print("Who has more followers?", end=" ")
    user_choice = countdown(countdown_time)
    

    if user_choice == correct_choice:
        print("Correct!".center(100))
        return True
    elif user_choice == "":
        print("Time's up! You didn/t make a choice.".center(100))
        return False
    else:
        print("Wrong.".center(100))
        return False
