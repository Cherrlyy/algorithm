def reverseStr(s: list) -> None:
    left, right = 0, len(s) -1
    while left < right: # 단순 숫자 이용해 for문 돌리기보다 유리함
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1



reverseStr(["h", "e", "l", "l", "o"])