"""
Word Occurrences
Estimate: 20 min
Actual: 27 min
"""

word_to_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1
sorted_words = sorted(word for word in word_to_count)
max_word_length = max(len(word) for word in word_to_count)
for word in sorted_words:
    print(f"{word:{max_word_length}} : {word_to_count[word]}")
