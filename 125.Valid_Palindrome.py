
def isPalindrome(s):
    final_string = ""
    for i in s:
        if i.isalnum():
            final_string+=i.lower()
    print(final_string[::-1])
    return True if final_string == final_string[::-1] else False


print(isPalindrome("My name, is, Archana"))


