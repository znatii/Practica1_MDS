import re
text = str(input().strip())
pattern = "\\b\\d{4}\\b"
results = re.findall(pattern, text)
for match in results:
    print(match)