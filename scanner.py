#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import sys
import socket

def banner():
    print("""
    ========================================
       somesites - Version 0.2
       Created by: Demon Coder
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
            print("\n[+] HTML Structure retrieved:")
            print("-" * 40)
            print(soup.prettify())
            print("-" * 40)
            print("\n[!] Scan complete.")
        else:
            print(f"[-] Failed with status code: {response.status_code}")

    except Exception as e:
        print(f"[-] Error: {e}")

def scan_port(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2.0)
    try:
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        else:
            print(f"[-] Port {port} is CLOSED")
    except Exception as e:
        print(f"[-] Error scanning port {port}: {e}")
    finally:
        s.close()

if __name__ == "__main__":
    banner()
    choice = input("Choose mode: [1] HTML Scan [2] Port Scan: ")

    if choice == '1':
        if len(sys.argv) > 1:
            scan_website(sys.argv[1])
        else:
            target = input("Enter Website URL: ")
            scan_website(target)
    elif choice == '2':
        target = input("Enter IP or Domain: ")
        port = int(input("Enter Port to scan: "))
        scan_port(target, port)
    else:
        print("[-] Invalid choice.")
#then press ctrl + o then enter then ctrl + x and type "chmod +x scanner.py then type ln -sf $HOME/scanner.py$PREFIX/bin/somesites
