"""
https://leetcode.com/problems/student-attendance-record-ii/description/

An attendance record for a student can be represented as a string where each character signifies whether the student was
 absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
Any student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Given an integer n, return the number of possible attendance records of length n that make a student eligible for an
attendance award. The answer may be very large, so return it modulo 109 + 7.
"""


class Solution:
    def checkRecord(self, n: int) -> int:
        """
        There are a couple of different things we must track.
        1. The number of absences we've had. This can either be zero or 1.
        2. The number of lates we have just seen. This can be zero, 1, or 2.
        Together this gives us 6 states.

        We can represent this as a 2d array where the rows are the number of absences and the columns are the number of
        lates. Where each section of the array represents the number of ways we can get to that state.
        """
        # we start with 1 way to get to 0 absences and 0 lates and no other ways (this is the default state since when
        # n = 0, we have no way of the student being absent or late)
        array = \
            [[1, 0, 0],  # 0 absences
             [0, 0, 0]]  # 1 absence

        for _ in range(n):
            # this is padded with 0's, so we can do the math without worrying about out of bounds errors
            new_array = \
                [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]
            for absences in range(2):
                for lates in range(3):
                    # P: keeps number of absences the same, and lates to 0
                    # L: keeps number of absences the same, and increments lates
                    # A: increments number of absences, and sets lates to 0

                    # P: keeps number of absences the same, and lates to 0
                    new_array[absences][0] += array[absences][lates]
                    # L: keeps number of absences the same, and increments lates
                    new_array[absences][lates + 1] += array[absences][lates]
                    # A: increments' number of absences, and sets lates to 0
                    # print(new_array)
                    new_array[absences + 1][0] += array[absences][lates]
            # we unpad the array
            array = [[x % (10 ** 9 + 7) for x in row[:3]] for row in new_array[:2]]
        return sum(sum(row) for row in array) % (10 ** 9 + 7)


n = 10101
print(Solution().checkRecord(n))
