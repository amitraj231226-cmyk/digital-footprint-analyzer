import re
import requests


def detect_type(target):
    if re.match(r"[^@]+@[^@]+\.[^@]+", target):
        return "Email"
    elif "." in target:
        return "Domain"
    else:
        return "Username"


def calculate_risk(target):
    risks = []

    if len(target) < 8:
        risks.append("Too short")

    if target.islower():
        risks.append("No uppercase letters")

    if target.isalpha():
        risks.append("No numbers or symbols")

    return risks


def check_username(target):
    sites = {
        "GitHub": f"https://github.com/{target}",
        "Reddit": f"https://www.reddit.com/user/{target}"
    }

    results = {}

    for site, url in sites.items():
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                results[site] = "Found"
            else:
                results[site] = "Not Found"
        except:
            results[site] = "Error"

    return results

def check_security_headers(domain):
    headers_to_check = [
        "Content-Security-Policy",
        "X-Frame-Options",
        "Strict-Transport-Security",
        "X-Content-Type-Options"
    ]

    results = {}

    try:
        response = requests.get(f"https://{domain}", timeout=5)

        for header in headers_to_check:
            if header in response.headers:
                results[header] = "Present"
            else:
                results[header] = "Missing"

    except:
        results["Error"] = "Could not analyze domain"

    return results


def save_report(target, target_type, score, risks, platform_results):
    with open("report.txt", "w") as file:
        file.write("DIGITAL FOOTPRINT REPORT\n")
        file.write("=" * 30 + "\n")
        file.write(f"Target: {target}\n")
        file.write(f"Type: {target_type}\n")
        file.write(f"Risk Score: {score}/100\n\n")

        file.write("Platform Check:\n")
        for site, result in platform_results.items():
            file.write(f"{site}: {result}\n")


def analyze(target):
    target_type = detect_type(target)

    risks = calculate_risk(target)

    score = max(100 - (len(risks) * 20), 0)

    print(f"\nTarget Type: {target_type}")
    print(f"Risk Score: {score}/100\n")

    platform_results = {}

    if target_type == "Username":
        platform_results = check_username(target)

        print("Platform Presence:")
        for site, result in platform_results.items():
            print(f"{site}: {result}")

    elif target_type == "Domain":
        platform_results = check_security_headers(target)

        print("Security Headers:")
        for header, result in platform_results.items():
            print(f"{header}: {result}")

    save_report(target, target_type, score, risks, platform_results)

    print("\nReport saved as report.txt")