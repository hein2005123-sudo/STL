import os
import time
import hashlib

def clear():
    os.system('clear')

def logo():
    print("\033[1;32m[*] STL PRIVATE BYPASS SYSTEM v3.5\033[0m")
    print("\033[1;33m[!] YOUR DEVICE ID: F0A90BD125\033[0m")
    print("\033[1;37m----------------------------------------\033[0m")

def generate_logic(mac):
    # This is a placeholder logic
    clean_mac = mac.replace(":", "").upper()
    results = []
    for i in range(1, 7):
        seed = f"{clean_mac}{i}"
        v = str(int(hashlib.md5(seed.encode()).hexdigest(), 16))[-6:]
        results.append(v)
    return results

def main():
    clear()
    logo()
    key = input("\033[1;36m[?] ENTER ACCESS KEY: \033[0m")
    
    if key == "ALADDIN":
        print("\033[1;32m[+] ACCESS GRANTED!\033[0m")
        time.sleep(1)
        mac = input("\033[1;37mEnter Router MAC: \033[0m")
        print("\nChecking database...")
        time.sleep(1.5)
        codes = generate_logic(mac)
        for i, c in enumerate(codes, 1):
            print(f"Voucher {i}: {c}")
    else:
        print("\033[1;31m[X] ACCESS DENIED: INVALID KEY.\033[0m")

if __name__ == "__main__":
    main()

