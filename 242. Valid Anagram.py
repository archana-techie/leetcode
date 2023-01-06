def valid_anagram(s,t):
    s1 = []
    s2 = []
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        s1.append(s[i])
        s2.append(t[i])
    return sorted(s1) == sorted(s2)


print(valid_anagram("anagram", "nagaram"))