# https://leetcode.com/problems/most-common-word/description/

import collections
import re
from typing import List

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]


# 딕셔너리 사용
def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    words = [
        word
        for word in re.sub(r"[^\w]", " ", paragraph).lower().split()
        if word not in banned
    ]

    # 딕셔너리 Value 기본값 0
    counts = collections.defaultdict(int)
    for word in words:
        counts[word] += 1

    # 왜 오류??
    return max(counts, key=counts.get)  # type: ignore


# Counter 객체 사용
def mostCommonWord2(self, paragraph: str, banned: List[str]) -> str:
    words = [
        word
        for word in re.sub(r"[^\w]", " ", paragraph).lower().split()
        if word not in banned
    ]

    counts = collections.Counter(words)

    # most_common(1): 가장 흔한 word
    # [0][0]: [('ball', 2)] 2번
    return counts.most_common(1)[0][0]
