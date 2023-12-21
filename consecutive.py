from typing import *
from icecream import ic
class Solution:
    def isPossible(self, nums: List[int]) -> bool:


        def iter_group() -> Iterator[tuple[int, int]]:
            """
            iterates over groups of consecutive numbers so [1, 1, 1, 2, 2, 3, 3, 3, 3] would yield
            [(1, 3), (2, 2), (3, 4)]
            """
            i = 0
            count = 0
            cur = nums[0]
            while i < len(nums):
                if cur == nums[i]:
                    count += 1
                else:
                    yield cur, count
                    cur = nums[i]
                    count = 1
                i += 1
            yield cur, count

        prev = 0
        len_1 = 0
        len_2 = 0
        len_3 = 0
        for num, count in iter_group():
            if num - 1 != prev:
                if len_1 > 0 or len_2 > 0:
                    # ic("here")
                    return False
                len_1 = count
                len_2 = 0
                len_3 = 0
            else:
                if count < len_1 + len_2:
                    # ic("here2")
                    return False
                new_len_1 = max(0, count - (len_1 + len_2 + len_3))
                new_len_2 = len_1
                new_len_3 = count - (new_len_1 + new_len_2)
                len_1, len_2, len_3 = new_len_1, new_len_2, new_len_3
            prev = num
            # ic(num, count)
            # ic(len_1, len_2, len_3)
        return len_1 == 0 and len_2 == 0

# nums = [1,2,3,4,4,5]
nums = [1,2,3,3,4,5]
print(Solution().isPossible(nums))







