import re
text = str(input().strip())
pattern = r"\b(\d{4})-(\d{2})-(\d{2})\b"
newOrder = r"\3.\2.\1"
results = re.findall(pattern, text)

textFormated = re.sub(pattern, newOrder, text)
print(textFormated)