# https://leetcode.com/problems/reorder-data-in-log-files/description/

from typing import List


def reorderLogFiles(self, logs: List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # 식별자를 제외하는 [1:]로 정렬을 한다.
    # 만약 로그가 같다면 [0]로 식별자를 정렬한다
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits
