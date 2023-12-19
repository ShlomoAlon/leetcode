from __future__ import annotations
from typing import *


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        max_y = len(img)
        max_x = len(img[0])
        result = [[0] * max_x for _ in range(max_y)]

        def directions(i, j) -> Iterator[int]:
            for y in range(i - 1, i + 2):
                for x in range(j - 1, j + 2):
                    if 0 <= y < max_y and 0 <= x < max_x:
                        yield img[y][x]

        for y in range(max_y):
            for x in range(max_x):
                count = 0
                total = 0
                print(y, x)
                for value in directions(y, x):
                    print(value)
                    count += 1
                    total += value
                result[y][x] = total // count

        return result


img = [[1,1,1],[1,0,1],[1,1,1]]
img = [[100,200,100],[200,50,200],[100,200,100]]
print(Solution().imageSmoother(img))