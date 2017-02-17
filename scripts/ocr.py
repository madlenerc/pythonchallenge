# level 2
from collections import Counter

with open('../data/ocr.txt') as f:
    text = f.read()
    c = Counter(text)
    print(c.most_common())