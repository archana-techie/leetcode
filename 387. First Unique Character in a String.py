

def first_unique(s):
    # unique = {}
    # seen = []
    #
    # for i in range(len(s)):
    #     if s[i] not in unique and s[i] not in seen:
    #         unique[s[i]] = i
    #         seen.append(s[i])
    #     else:
    #         unique.pop(s[i], None)
    # if unique:
    #     return min(list(unique.values()))
    # return -1

    # or


    freq = {}
    for i in s:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    for i in s:
        if freq[i] == 1:
            return s.index(i)
    return -1


print(first_unique("aadadaad"))