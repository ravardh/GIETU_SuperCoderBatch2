def pattern_search(text, pattern):
    occurrences = []
    start = 0
    while True:
        start = text.find(pattern, start)
        if start == -1:
            break
        occurrences.append(start)
        start += 1
    return occurrences

text = input("Enter the text: ")
pattern = input("Enter the pattern to search for: ")

positions = pattern_search(text, pattern)

if positions:
    print("Pattern found at positions:", positions)
else:
    print("Pattern not found in the text.")
