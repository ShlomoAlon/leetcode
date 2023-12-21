"""
https://leetcode.com/problems/minimum-money-required-before-transactions/description/
You are given a 0-indexed 2D integer array transactions, where transactions[i] = [costi, cashbacki].

The array describes transactions, where each transaction must be completed exactly once in some order.
At any given moment, you have a certain amount of money. In order to complete transaction i
, money >= costi must hold true. After performing a transaction, money becomes money - costi + cashbacki.

Return the minimum amount of money required before any transaction so that all of the transactions can be completed
 regardless of the order of the transactions.
"""
from functools import cmp_to_key
from typing import *


class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:

        def compare(a: List[int], b: List[int]) -> int:
            # print("comparing", a, b)
            total_result_a = a[1] - a[0]
            total_result_b = b[1] - b[0]
            # if the result of running both transactions are negative, we want the one with the lower cashback first
            if total_result_a < 0 and total_result_b < 0:
                result = b[1] - a[1]
                return result
            # if the result of running both transactions are positive, we want the one with the larger cost first
            elif total_result_a > 0 and total_result_b > 0:
                # print("here2")
                return a[0] - b[0]
            else:
                # print("here3")
                # we want the one with the negative result first
                return total_result_b - total_result_a

            # we want positive cashback to before negative cashback

        transactions.sort(# key=cmp_to_key(compare),
            key=cmp_to_key(compare), reverse=True)
        minimum = 0
        current_money = 0
        for cost, cashback in transactions:
            print("cost:", cost, "cashback:", cashback)
            current_money -= cost
            # print("current_money before cashback:", current_money)
            minimum = min(minimum, current_money)
            current_money += cashback  # print("current_money after cashback:", current_money)
        return minimum * -1


# transactions = [[2,1],[5,0],[4,2]]
transactions = [[3, 0], [0, 3]]
print(Solution().minimumMoney(transactions))
