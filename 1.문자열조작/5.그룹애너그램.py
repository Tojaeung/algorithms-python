# https://leetcode.com/problems/group-anagrams/description/

import collections
from typing import List

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    """
    anagrams = {}
    존재하지 않는 키를 삽입하려고 할때 KeyError
    get()를 사용해서 찾으려고 해도 문제
    그래서, collections.defaultdict(list)를 사용
    """
    anagrams = collections.defaultdict(list)

    for word in strs:
        # split -> 문자열을 배열로
        # join -> 배열을 문자열로
        anagrams["".join(sorted(word))].append(word)

    return list(anagrams.values())
