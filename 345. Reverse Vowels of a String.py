

def reverse_vowels_of_string(s):

    l = 0
    r = len(s) - 1
    vowels = ['a', 'e', 'i', 'o', 'u']
    st = list(s)
    while l < r:
        if st[l] in vowels and st[r] in vowels:
            st[l], st[r] = st[r], st[l]
            l = l + 1
            r = r - 1
        elif st[l] not in vowels:
            l+=1
        elif st[r] not in vowels:
            r-=1

    return "".join(st)


print(reverse_vowels_of_string("leetcode"))