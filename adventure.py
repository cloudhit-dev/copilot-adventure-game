import time
import sys

def slow_print(text, speed=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def show_banner():
    print(r"""
  __   __  _______  __   __  _______  __   __  _______  __   __
 |  |_|  ||       ||  |_|  ||       ||  |_|  ||       ||  | |  |
 |       ||   _   ||       ||   _   ||       ||    ___||  |_|  |
 |       ||  | |  ||       ||  | |  ||       ||   |___ |       |
 |       ||  |_|  ||       ||  |_|  ||       ||    ___||_     _|
 | ||_|| ||       || ||_|| ||       || ||_|| ||   |___   |   |  
 |_|   |_||_______||_|   |_||_______||_|   |_||_______|  |___|  

   [ MEGACORP INFILTRATION SYSTEM - BOOT SEQUENCE ]
   [ STATUS: ONLINE ]
   [ NETWORK: SECURE NODE 7 ]
""")


def main_menu():
    show_banner()
    slow_print(">>> WELCOME, OPERATOR. INITIATING MISSION PROFILE...")
    while True:
        print("\n--- MAIN MENU ---")
        print("1) START MISSION")
        print("2) BRIEFING")
        print("3) QUIT")

        choice = input("Select an option (1/2/3): ").strip()
        if choice == "1":
            start_game()
            break
        elif choice == "2":
            briefing()
        elif choice == "3":
            slow_print(">>> TERMINATING SESSION. STAY HIDDEN.")
            break
        else:
            slow_print(">>> INVALID COMMAND. ENTER 1, 2, OR 3.")


def briefing():
    slow_print("\n>>> MISSION BRIEFING:")
    slow_print("You are in the basement of the Megacorp Tower.")
    slow_print("Your objective is to infiltrate the Penthouse and steal the Omega Files.")
    slow_print("Use stealth, obtain the Level 4 Keycard, and outsmart the Sentinel AI.")
    slow_print("Good luck, operative.")


# Inventory to track progress
inventory = {"keycard": False, "virus_uploaded": False}

def start_game():
    slow_print("\n>>> OPERATIVE, you are in the basement of the Megacorp Tower.")
    slow_print(">>> Objective: Steal the 'Omega Files' from the Penthouse.")
    basement()

def basement():
    slow_print("\n[BASEMENT HUB]")
    slow_print("You see a 'SECURITY ROOM' to your left and an 'ELEVATOR' to your right.")
    choice = input("Where do you go? (security/elevator): ").lower()

    if "security" in choice:
        security_room()
    elif "elevator" in choice:
        elevator_lobby()
    else:
        slow_print(">>> ERROR: Command not recognized.")
        basement()

def security_room():
    slow_print("\n[SECURITY ROOM]")
    if not inventory["keycard"]:
        slow_print("A guard is sleeping at the desk. A GOLDEN KEYCARD glitters in his pocket.")
        action = input("Do you 'STEAL' the card or 'LEAVE'? ").lower()
        if "steal" in action:
            slow_print(">>> SUCCESS: You obtained the Level 4 Keycard.")
            inventory["keycard"] = True
            security_room()
        else:
            basement()
    else:
        slow_print("The room is empty. Nothing else to do here.")
        basement()

def elevator_lobby():
    slow_print("\n[ELEVATOR LOBBY]")
    slow_print("The elevator requires a Level 4 Keycard to reach the Penthouse.")
    
    if inventory["keycard"]:
        slow_print(">>> KEYCARD ACCEPTED. Ascending to the Penthouse...")
        time.sleep(2)
        penthouse()
    else:
        slow_print(">>> ACCESS DENIED. You need a keycard.")
        slow_print("Maybe check the Security Room?")
        basement()

def penthouse():
    slow_print("\n[PENTHOUSE - FINAL FLOOR]")
    slow_print("The Omega Files are protected by a 'SENTINEL AI'.")
    slow_print("The AI speaks: 'Identify yourself or be deleted.'")
    print("1. Try to HACK the terminal.")
    print("2. Use a DISTRACTION (Set off fire alarm).")
    print("3. Try to TALK your way out.")

    choice = input("Choose your move (1/2/3): ")

    if choice == "1":
        slow_print("\n>>> HACKING...")
        time.sleep(2)
        slow_print("The AI is too fast! It traces your IP and locks you in. MISSION FAILED.")
        play_again()
    elif choice == "2":
        slow_print("\n>>> ALARM TRIGGERED!")
        slow_print("The AI is busy handling the sprinklers. You grab the files!")
        slow_print("CONGRATULATIONS, OPERATIVE. YOU ARE A LEGEND.")
        play_again()
    elif choice == "3":
        slow_print("\n'I am your creator,' you lie.")
        slow_print("The AI pauses... 'Verification required. What is 12 * 12?'")
        ans = input("Answer: ")
        if ans == "144":
            slow_print(">>> IDENTITY VERIFIED. Files released. YOU WIN!")
        else:
            slow_print(">>> LIAR detected. Defense turrets activated. GAME OVER.")
        play_again()

def play_again():
    res = input("\nRestart Mission? (y/n): ")
    if res.lower() == "y":
        inventory["keycard"] = False
        start_game()
    else:
        slow_print(">>> LOGGING OFF. STAY SAFE IN THE REAL WORLD.")

if __name__ == "__main__":
    main_menu()