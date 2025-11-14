# 🔒 Web Security Scanner

A lightweight, modular Python-based web security scanner that performs fundamental vulnerability checks on any public website.  
Designed for learning, cybersecurity practice, and showcasing secure coding + security automation skills.

---

## 🚀 Features

### ✔ HTTPS & TLS Inspection

- Detects if HTTPS is enabled
- Extracts TLS certificate metadata (issuer, validity period, subject)
- Detects broken or misconfigured certificates

### ✔ Security Header Analysis

Automatically checks for the presence of common security headers:

- `Content-Security-Policy`
- `Strict-Transport-Security`
- `X-Frame-Options`
- `X-XSS-Protection`
- `X-Content-Type-Options`

### ✔ Directory Enumeration

Scans for commonly exposed files and directories such as:

- `/admin`
- `/login`
- `/uploads`
- `/backup.zip`
- `robots.txt`, etc.

### ✔ Port Scanning (python-nmap)

Scans commonly used TCP ports like:

- 80, 443, 22, 21, 3306, 8080  
  (Requires Nmap to be installed)

### ✔ JSON Reporting

Automatically generates a structured JSON file containing:

- HTTPS analysis
- Missing headers
- Directory findings
- Port scan results

---

## 🛠️ Tech Stack

- **Python 3**
- `requests`
- `python-nmap`
- `ssl` + `socket`
- JSON output reporting

---

## 📂 Project Structure
