def countSegments(s: str) -> int:
    count = 0
    flag = 0
    s += ' '
    for i in range(len(s) - 1):
        if s[i] != ' ' and s[i + 1] == ' ':
            count += 1
    return count


print(countSegments("hello, hi"))