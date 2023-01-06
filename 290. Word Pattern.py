
def word_pattern(pattern,s):
    d = {}
    words = s.split(' ')
    if len(words) != len(pattern) or len(set(words)) != len(set(pattern)):
        return False
    for i in range(0, len(pattern)):
        if pattern[i] in d:
            if d[pattern[i]] != words[i]:
                return False
        else:
            d[pattern[i]] = words[i]

    return True


print(word_pattern("abba", "dog cat try dog"))