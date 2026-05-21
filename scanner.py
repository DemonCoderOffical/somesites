import requests
from bs4 import BeautifulSoup
import sys

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

if __name__ == "__main__":
    if len(sys.argv) > 1:
        scan_website(sys.argv[1])
    else:
        target = input("Enter Website URL to scan: ")
        scan_website(target)
#then press ctrl + o then enter then ctrl + x and type "chmod +x scanner.py then type ln -sf $HOME/scanner.py$PREFIX/bin/somesites
