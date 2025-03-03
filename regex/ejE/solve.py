import re

# añadir ?:
text = str(input().strip())
pattern = r"\b(C\/|Calle) ([A-ZÑ][a-zñ]*),? +([Nn]º? ?)?(\d+), +(\d{5})\b"

results = re.findall(pattern, text)

for result in results:
    output = (f"{result[4]}-{result[1]}-{result[3]}")
    print(output)



