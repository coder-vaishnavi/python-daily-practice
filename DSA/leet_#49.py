strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

d = {}

for word in strs:
    # Sort the word and convert it back to a string
    key = "".join(sorted(word))

    # Create a new list if the key doesn't exist
    if key not in d:
        d[key] = []

    # Add the original word to its group
    d[key].append(word)

# Print the grouped anagrams
print(list(d.values()))