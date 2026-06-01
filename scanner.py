#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import socket

def banner():
    print("""
    ========================================
       somesites - v1.0
       Author: Demon Coder
    ========================================
    """)

def scan_website(url):
    try:
        if not url.startswith('http'):
            url = 'https://' + url
        print(f"\n[!] Connecting to: {url}...")
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print("[+] Connection successful!")
            soup = BeautifulSoup(response.text, 'html.parser')
            print("\n[+] HTML Structure retrieved:\n" + "-" * 40)
            print(soup.prettify())
            print("-" * 40)
        else:
            print(f"[-] Failed with status code: {response.status_code}")
    except Exception as e:
        print(f"[-] Error: {e}")

def scan_port(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0)
    try:
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        else:
            print(f"[-] Port {port} is CLOSED")
    except Exception as e:
        print(f"[-] Error: {e}")
    finally:
        s.close()

if __name__ == "__main__":
    banner()
    # List of common ports for the 'top' feature
    COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 3389, 8080]

    while True:
        print("\nMain Menu: [1] HTML Scan [2] Port Scan [e] Exit")
        choice = input("Choose mode: ")

        if choice == '1':
            target = input("Enter Website URL: ")
            scan_website(target)

        elif choice == '2':
            target = input("Enter IP or Domain: ")
            print("Enter command (or type 'help' for examples):")
            cmd = input(f"{target} >> ").lower()

            if cmd == 'help':
                print("\n--- Scan Help Menu ---")
                print("1. Range scan: from [start] to [end] (e.g., from 1 to 100)")
                print("2. Top ports: top [number] (e.g., top 10)")
                print("3. Single port: just type the port number (e.g., 80)")

            elif "from" in cmd and "to" in cmd:
                try:
                    parts = cmd.split()
                    start = int(parts[1])
                    end = int(parts[3])
                    print(f"[*] Scanning {target} from port {start} to {end}...")
                    for p in range(start, end + 1):
                        scan_port(target, p)
                except:
                    print("[-] Invalid range format. Use: from 1 to 10")

            elif "top" in cmd:
                try:
                    count = int(cmd.split()[1])
                    print(f"[*] Scanning {target} for top {count} ports...")
                    for p in COMMON_PORTS[:count]:
                        scan_port(target, p)
                except:
                    print("[-] Invalid top format. Use: top 10")

            else:
                try:
                    port = int(cmd)
                    scan_port(target, port)
                except:
                    print("[-] Invalid input. Type 'help' for more info.")

        elif choice.lower() == 'e':
            print("[!] Exiting...")
            break
        else:
            print("[-] Invalid choice.")
#then type chmod +x scanner.py then type ln -sf $HOME/somesites$PREFIX/bin/scanner.py
