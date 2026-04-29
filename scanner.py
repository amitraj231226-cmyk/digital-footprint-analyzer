def analyze(target):
    print(f"\nAnalyzing {target}...\n")

    risks = []

    if "@" in target:
        risks.append("Email format detected")

    if len(target) < 8:
        risks.append("Weak identifier length")

    score = 100 - (len(risks) * 20)

    print("Risk Score:", score)

    for risk in risks:
        print("[!] ", risk)