from collections import Counter

with open("File.txt") as f:
    text = f.read().lower().split()

counter = Counter(text)

print("Total words", len(text))
print("Unique words", len(counter))
print("Top 5 common words", counter.most_common(5))