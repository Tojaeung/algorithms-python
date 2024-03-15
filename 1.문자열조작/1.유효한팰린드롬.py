# https://leetcode.com/problems/valid-palindrome/description/

import collections
import re
from typing import Deque


s = input("문자열을 입력하시오 : ")


# 리스트 사용 (304ms)
def isPalindrome1(self, s: str) -> bool:
    # 문자만 정제 (숫자, 특수문자 제외)
    strs = []
    for char in s:
        if char.isalnum():  # 문자 구분
            strs.append(char.lower())  # 소문자

    # 펠린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True


# 데크 사용 (64ms)
def isPalindrome2(self, s: str) -> bool:
    # 문자만 정제 (숫자, 특수문자 제외)
    strs: Deque = collections.deque()
    for char in s:
        if char.isalnum():  # 문자 구분
            strs.append(char.lower())  # 소문자

    # 펠린드롬 여부 판별
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True


# 슬라이싱 사용 (36ms)
def isPalindrome3(self, s: str) -> bool:
    s = s.lower()

    """
    [0-9] 모든 숫자
    [a-z] 모든 소문자
    [A-Z] 모든 대문자
    [a-zA-Z] 모든 알파벳
    ^ 반대(not)
    """
    s = re.sub("[^a-z0-9]", "", s)  # [^a-z0-9]: 모든 소문자, 모든 숫자 아닌 나머지...

    return s == s[::-1]  # 거꾸로 뒤집기
