def reverseStr(s: list) -> None:
    s[:] = s[::-1]
    print(s[:])



reverseStr(["h", "e", "l", "l", "o"])