
def canConstruct(ransomNote: str, magazine: str) -> bool:
    for s in ransomNote:
        if ransomNote.count(s) > magazine.count(s):
            return False
    return True


print(canConstruct("asd", "affgghsttd"))