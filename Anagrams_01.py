import collections

def groupAnagrams(strs: list) -> list:
    anagrams = collections.defaultdict(list)
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return anagrams.values()

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))