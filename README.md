# ErrorEyes-Domain-Scanner
🔍 Erroreyes – Lightweight Subdomain Enumeration Tool A Python-based tool that queries crt.sh certificate logs to discover subdomains associated with a target domain. Perfect for security researchers, bug bounty hunters, and sysadmins conducting reconnaissance.

# Features

✔ Fetches subdomains from crt.sh (public SSL certificate logs)

✔ Filters and validates domains (removes noise, checks syntax)

✔ Saves results to domain.txt (easy for further analysis)

✔ Lightweight, no API keys required

# Installation

```
git clone https://github.com/AbzeeSaminu/ErrorEyes-Domain-Scanner
cd erroreyes
pip install requests
```

# Usage

```
python3 erroreyes.py example.com
```

# Ethical Use

🚨 This tool must only be used on domains you are explicitly authorized to scan. Unauthorized use is illegal and violates ethical security practices.
