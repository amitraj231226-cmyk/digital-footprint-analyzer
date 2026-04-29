import re


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


def save_report(target, target_type, score, risks):
    with open("report.txt", "w") as file:
        file.write("DIGITAL FOOTPRINT REPORT\n")
        file.write("=" * 30 + "\n")
        file.write(f"Target: {target}\n")
        file.write(f"Type: {target_type}\n")
        file.write(f"Risk Score: {score}/100\n\n")

        if risks:
            file.write("Risks:\n")
            for risk in risks:
                file.write(f"- {risk}\n")
        else:
            file.write("No risks detected.\n")


def analyze(target):
    target_type = detect_type(target)

    risks = calculate_risk(target)

    score = max(100 - (len(risks) * 20), 0)

    print(f"\nTarget Type: {target_type}")
    print(f"Risk Score: {score}/100\n")

    if risks:
        print("Potential Risks:")
        for risk in risks:
            print(f"[!] {risk}")
    else:
        print("No obvious risks detected.")

    save_report(target, target_type, score, risks)

    print("\nReport saved as report.txt")