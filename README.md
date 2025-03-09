Web Security Scanner
WebCrawler
This project is a simple web security scanner that analyses a website for potential vulnerabilities. It checks for missing security headers, outdated software versions, and insecure form configurations, and extracts links from the webpage.

Features

Extracts Links: Find all hyperlinks on the page.

Checks Security Headers: Identifies missing HTTP security headers.

Detects Outdated Software: Scans for outdated software versions from meta tags and server headers.

Finds Insecure Forms: Flags forms that use GET instead of POST or lack an action attribute.

Installation

Prerequisites

Python 3.x

requests library

beautifulsoup4 library

Setup

Clone the repository:

git clone https://github.com/yourusername/web-security-scanner.git
cd web-security-scanner

Install dependencies:

pip install -r requirements.txt

Usage

Run the script and input the target URL when prompted:

python scanner.py

Example Input:

A URL TO SCAN (E.G., HTTPS://EXAMPLE.COM)

Example Output:

VULNERABILITY SCAN REPORT FOR HTTP://EXAMPLE.COM:
- MISSING HTTP SECURITY HEADERS: STRICT-TRANSPORT-SECURITY
- OUTDATED SOFTWARE VERSION DETECTED: APACHE 2.4.6
- FORM SECURITY ISSUE: FORM USING GET INSTEAD OF POST
- EXTRACTED LINKS:
  - https://example.com/about
  - https://example.com/contact

Assumptions & Limitations

The scanner does not perform active penetration testing; it only analyzes publicly available information.

It may not detect all outdated software due to reliance on meta tags and server headers.

It does not verify HTTPS certificate security.
