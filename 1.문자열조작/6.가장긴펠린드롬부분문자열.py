# https://leetcode.com/problems/longest-palindromic-substring/description/


def longestPalindrome(s: str) -> str:
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        # left 마이너스 됐으므로 +1 더해서 리턴
        return s[left + 1 : right]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ""
    # range(len(s))해도 결과는 똑같지만 -1함으로써 1번 더 도는거 막을 수 있다.
    for i in range(len(s) - 1):

        # expand(i, i + 1) 짝수 펠린드롬 일때...
        # expand(i, i + 2) 홀수 펠린드롬 일때...
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

    return result
