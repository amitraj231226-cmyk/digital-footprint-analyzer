import re


def detect_type(target):
    if "@" in target:
        return "Email"
    elif "." in target:
        return "Domain"
    else:
        return "Username"


def calculate_risk(target):
    risks = []

    if len(target) < 8:
        risks.append("Target is too short")

    if target.islower():
        risks.append("No uppercase characters")

    if target.isalpha():
        risks.append("No numbers or symbols")

    return risks


def analyze(target):
    target_type = detect_type(target)

    print(f"\nTarget Type: {target_type}")

    risks = calculate_risk(target)

    score = max(100 - (len(risks) * 20), 0)

    print(f"Risk Score: {score}/100\n")

    if risks:
        print("Potential Risks Found:")
        for risk in risks:
            print(f"[!] {risk}")
    else:
        print("No obvious risks detected.")