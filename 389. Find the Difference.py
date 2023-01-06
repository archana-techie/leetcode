

def string_difference(s,t):
    if s:
        return t[s.index(s[len(s) -1]) + 1 : ]
    return t


print(string_difference("", "abcd"))