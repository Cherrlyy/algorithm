import collections

def isPalindrome(s: str) -> bool:
    strs = collections.deque()
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop() != strs.popleft():
            return False

    return True

s = input("")
is_bool = isPalindrome(s)
print(is_bool)