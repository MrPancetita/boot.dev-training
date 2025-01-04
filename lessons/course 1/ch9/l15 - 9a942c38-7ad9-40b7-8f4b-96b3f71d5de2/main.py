# https://www.boot.dev/lessons/9a942c38-7ad9-40b7-8f4b-96b3f71d5de2

def find_max(nums):
    max_so_far = float("-inf")
    for num in nums:
        max_so_far = num if num > max_so_far else max_so_far
    return max_so_far
