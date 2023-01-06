def isSubsequence(s: str, t: str) -> bool:
    i = 0
    if not s:
        return True
    for j in range(len(t)):
        if i >= len(s):
            return False
        if s[i] == t[j]:
            if i == len(s) - 1:
                return True
            i += 1
    return False

print(isSubsequence("abc", "ajhbjjjc"))