# https://leetcode.com/problems/reverse-string/description/

from typing import List


# 투포인터
def reverseString(self, s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


# 파이썬 다운 방식
def reverseString2(self, s: List[str]) -> None:
    s.reverse()
