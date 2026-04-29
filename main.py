from scanner import analyze

print("=" * 50)
print("DIGITAL FOOTPRINT ANALYZER V1")
print("=" * 50)

target = input("\nEnter email / username / domain: ")

analyze(target)