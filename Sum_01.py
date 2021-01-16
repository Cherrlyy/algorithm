def twoSum(l: list, t: int) -> list:
    for i in range(len(l)):
        for c in range(i + 1, len(l)):
            if l[i] + l[c] == t:
                return [i, c]

print(twoSum([2, 7, 11, 15], 9))