#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import sys
import socket

def banner():
    print("""
    ========================================
       somesites - v0.3
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
    s.settimeout(2.0)
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
    while True: # This loop keeps the program running
        print("\nMain Menu: [1] HTML Scan [2] Port Scan [e] Exit")
        choice = input("Choose mode: ")

        if choice == '1':
            target = input("Enter Website URL: ")
            scan_website(target)
        elif choice == '2':
            target = input("Enter IP or Domain: ")
            # This try-except block prevents the crash
            try:
                port = int(input("Enter Port to scan: "))
                scan_port(target, port)
            except ValueError:
                print("[-] Error: Port must be a number!")
        elif choice.lower() == 'e':
            print("[!] Exiting...")
            break
        else:
            print("[-] Invalid choice.")