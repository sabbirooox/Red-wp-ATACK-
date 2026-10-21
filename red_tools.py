import os
import sys
import time
import random

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    os.system("pip install colorama")
    from colorama import Fore, Style, init
    init(autoreset=True)

# গ্লোবাল ভেরিয়েবল
target_number = "Not Set"
attack_type = "Not Set"
attack_limit = "Unlimited"

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def show_banner():
    clear_screen()
    print(Fore.RED + "==================================================")
    print(Fore.RED + Style.BRIGHT + "  ____  _____ ____     _____ ___   ___  _     ____  ")
    print(Fore.RED + Style.BRIGHT + " |  _ \| ____|  _ \   |_   _/ _ \ / _ \| |   / ___| ")
    print(Fore.RED + Style.BRIGHT + " | |_) |  _| | | | |    | || | | | | | | |   \___ \ ")
    print(Fore.RED + Style.BRIGHT + " |  _ <| |___| |_| |    | || |_| | |_| | |___ ___) |")
    print(Fore.RED + Style.BRIGHT + " |_| \_\_____|____/     |_| \___/ \___/|_____|____/ ")
    print(Fore.RED + "==================================================")
    print(Fore.MAGENTA + Style.BRIGHT + "         DEVELOPER BY SABBIR ØX  ☠️")
    print(Fore.RED + "==================================================")
    print("")

def show_menu():
    print(Fore.CYAN + f"[1] " + Fore.WHITE + f"TARGET NUMBER (Current: {target_number})")
    print(Fore.CYAN + f"[2] " + Fore.WHITE + f"CRASH ATTACK")
    print(Fore.CYAN + f"[3] " + Fore.WHITE + f"BAND ATTACK")
    print(Fore.CYAN + f"[4] " + Fore.WHITE + f"ATTACK LIMIT (Current: {attack_limit})")
    print(Fore.GREEN + f"[5] " + Fore.WHITE + f"START ATTACK")
    print(Fore.RED + f"[6] " + Fore.WHITE + f"EXIT")
    print(Fore.RED + "==================================================")

def set_attack_type(atype):
    global attack_type
    print(Fore.YELLOW + f"\n[*] Setting Attack Type to: {atype}...")
    time.sleep(1)
    print(Fore.CYAN + f"[*] Initializing {atype} Module...")
    time.sleep(1)
    attack_type = atype
    print(Fore.GREEN + Style.BRIGHT + f"[✓] Success! {atype} is now SET and READY.")
    time.sleep(1.5)

def simulate_attack():
    global target_number, attack_type, attack_limit
    
    if target_number == "Not Set":
        print(Fore.RED + "\n[!] Please set Target Number first (Option 1).")
        time.sleep(2)
        return
    if attack_type == "Not Set":
        print(Fore.RED + "\n[!] Please select Attack Type first (Option 2 or 3).")
        time.sleep(2)
        return

    clear_screen()
    print(Fore.RED + "==================================================")
    print(Fore.YELLOW + f"[*] Target Number : " + Fore.WHITE + target_number)
    print(Fore.YELLOW + f"[*] Attack Type   : " + Fore.WHITE + attack_type)
    print(Fore.YELLOW + f"[*] Attack Limit  : " + Fore.WHITE + str(attack_limit))
    print(Fore.RED + "==================================================")
    
    print(Fore.CYAN + f"[*] Initializing {attack_type}...")
    time.sleep(1)
    print(Fore.CYAN + "[*] Bypassing Security...")
    time.sleep(1)
    print(Fore.CYAN + "[*] Connecting to Remote Servers...")
    time.sleep(1)
    print(Fore.GREEN + "[+] Connection Established!\n")
    time.sleep(0.5)

    success = 0
    failed = 0
    i = 0
    
    try:
        while True:
            i += 1
            time.sleep(0.03)
            
            if attack_limit != "Unlimited":
                if i > int(attack_limit):
                    break
                
            if random.randint(1, 10) <= 8:
                print(Fore.GREEN + f"[{i}] SUCCESS: Sent {attack_type} request to {target_number}")
                success += 1
            else:
                print(Fore.RED + f"[{i}] FAILED : Connection Timeout / Blocked by Server")
                failed += 1
            
        print(Fore.RED + "\n--------------------------------------------------")
        print(Fore.GREEN + Style.BRIGHT + f"[✓] {attack_type} Complete!")
        print(Fore.YELLOW + f"[*] Total Success: {success} | Total Failed: {failed}")
        
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Attack stopped by user.")
        
    input(Fore.YELLOW + "\nPress Enter to return...")

def main():
    global target_number, attack_limit
    while True:
        show_banner()
        show_menu()
        
        choice = input(Fore.YELLOW + "\nSelect an option: " + Fore.WHITE)
        
        if choice == '1':
            target_number = input(Fore.CYAN + "Enter Target Number (e.g., +8801XXXXXXXXX): ").strip()
            print(Fore.GREEN + f"[✓] Target Number Set: {target_number}")
            time.sleep(1)
        elif choice == '2':
            set_attack_type("CRASH ATTACK")
        elif choice == '3':
            set_attack_type("BAND ATTACK")
        elif choice == '4':
            print(Fore.CYAN + f"\n[*] Current Limit: {attack_limit}")
            print(Fore.GREEN + "[1] UNLIMITED")
            print(Fore.GREEN + "[2] Custom Limit")
            sub = input(Fore.WHITE + "Choice: ").strip()
            if sub == '1':
                attack_limit = "Unlimited"
                print(Fore.GREEN + "[✓] Limit Set to UNLIMITED")
                time.sleep(1)
            elif sub == '2':
                try:
                    attack_limit = int(input(Fore.CYAN + "Enter Limit (e.g., 1000): ").strip())
                    print(Fore.GREEN + f"[✓] Limit Set to {attack_limit}")
                    time.sleep(1)
                except ValueError:
                    print(Fore.RED + "[!] Invalid Number.")
                    time.sleep(1)
        elif choice == '5':
            simulate_attack()
        elif choice == '6':
            print(Fore.RED + "Exiting... Goodbye!")
            sys.exit()
        else:
            print(Fore.RED + "Invalid option!")
            time.sleep(1)

if __name__ == "__main__":
    main()
