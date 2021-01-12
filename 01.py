def isPalindrome(s: list) -> bool:
    if len(s) <= 1:
        return True
    print(s[0] + ", " + s[-1] + " is " , s[0] == s[-1])
    # print(strs[0] == strs[-1])
    return (s[0] == s[-1]) & isPalindrome(s[1:-1])

s = input("")
strs = []

for char in s:
    if char.isalnum():
        strs.append(char.lower())
is_bool = isPalindrome(strs)
print(is_bool)