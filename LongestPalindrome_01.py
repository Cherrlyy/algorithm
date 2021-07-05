def logestPalindrome(s: str) -> str:
    def expand(left: int, right: int) -> str:
        while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
            left -= 1
            right += 1
        return s[left + 1:right - 1]

    if len(s) < 2 or s == s[::-1]:
        return s
    result = ''
    for i in range(len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key = len)
    return result



print(logestPalindrome("babadls"))
# max 함수 (key - function : 무엇으로 최대값을 따질 건지 목적어)