def reverseStr(s: list) -> None:
    left, right = 0, len(s) -1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1



reverseStr(["h", "e", "l", "l", "o"])