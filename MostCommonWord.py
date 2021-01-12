import re
import collections

def mostCommonWord(paragraph: str, banned = list) -> str:
    words = [x for x in re.sub("[^A-Za-z0-9]", " ", paragraph.lower()).split() if x not in banned]
    counter = collections.Counter(words)
    return counter.most_common(1)[0][0]


print(mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))