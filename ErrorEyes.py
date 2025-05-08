import requests
import sys
import re

def fetch_identities(domain):
    url = f"https://crt.sh/?Identity={domain}&match=LIKE&output=json"
    try:
        print(f"[>] Querying crt.sh for '{domain}' ...")
        response = requests.get(url, timeout=60) 
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"[!] Error querying crt.sh: {e}")
        sys.exit(1)

    try:
        data = response.json()
    except ValueError:
        print("[!] Failed to parse JSON response from crt.sh")
        sys.exit(1)

    identities = set()

    for entry in data:
        name_value = entry.get('name_value', '')
        for item in name_value.splitlines():
            item = item.strip().lower()
            if is_valid_domain(item):
                identities.add(item)

    return sorted(identities)

def is_valid_domain(domain):
    # Allow subdomains + TLD (basic validation)
    return re.match(r"^(?:[a-zA-Z0-9_\-]+\.)+[a-zA-Z]{2,}$", domain) is not None

def save_to_file(subdomains, filename="domain.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for sub in subdomains:
                f.write(sub + "\n")
        print(f"[+] {len(subdomains)} unique subdomains saved to {filename}")
    except IOError as e:
        print(f"[!] Error saving to file: {e}")

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} example.com")
        sys.exit(1)

    domain = sys.argv[1].lower()

    if not is_valid_domain(domain):
        print("[!] Invalid domain format.")
        sys.exit(1)

    identities = fetch_identities(domain)

    if identities:
        print(f"[+] Found {len(identities)} unique subdomains:\n")
        for identity in identities:
            print(identity)
        save_to_file(identities)
    else:
        print("[*] No matching identities found.")

if __name__ == "__main__":
    main()
