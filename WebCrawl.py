import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_links(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [urljoin(url, a["href"]) for a in soup.find_all("a", href=True)]
        return links
    except requests.RequestException:
        return []

def check_security_headers(url):
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers
        missing_headers = []
        required_headers = ["X-Content-Type-Options", "Strict-Transport-Security"]
        for header in required_headers:
            if header not in headers:
                missing_headers.append(header)
        return missing_headers
    except requests.RequestException:
        return []

def check_outdated_software(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        outdated_versions = []
        for meta in soup.find_all("meta"):
            if meta.get("name") == "generator" and meta.get("content"):
                outdated_versions.append(meta["content"])
        server_header = response.headers.get("Server", "")
        if server_header:
            outdated_versions.append(server_header)
        return outdated_versions
    except requests.RequestException:
        return []

def check_insecure_forms(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        issues = []
        for form in soup.find_all("form"):
            if not form.get("action"):
                issues.append("Form missing action attribute")
            if form.get("method", "GET").upper() == "GET":
                issues.append("Form using GET instead of POST")
        return issues
    except requests.RequestException:
        return []

def generate_report(url):
   
    print(f"VULNERABILITY SCAN REPORT FOR {url}:")
    
    missing_headers = check_security_headers(url)
    if missing_headers:
        print(f"- MISSING HTTP SECURITY HEADERS: {', '.join(missing_headers)}")
    
    outdated_software = check_outdated_software(url)
    if outdated_software:
        print(f"- OUTDATED SOFTWARE VERSION DETECTED: {', '.join(outdated_software)}")
    
    insecure_forms = check_insecure_forms(url)
    for form_issue in insecure_forms:
        print(f"- FORM SECURITY ISSUE: {form_issue}")
    
    extracted_links = extract_links(url)
    if extracted_links:
        print("- EXTRACTED LINKS:")
        for link in extracted_links:
            print(f"  - {link}")

def main():
    target_url = input("Input:\nA URL TO SCAN (E.G., HTTPS://EXAMPLE.COM): ")
    generate_report(target_url)

if __name__ == "__main__":
    main()
