def isomorphic_strings(s,t):
    l1,l2 = [], []
    for i in range(0, len(s)):
        l1.append(s.count(s[i]))
        l2.append(t.count(t[i]))

    return l1 == l2


print(isomorphic_strings("bar", "foo"))