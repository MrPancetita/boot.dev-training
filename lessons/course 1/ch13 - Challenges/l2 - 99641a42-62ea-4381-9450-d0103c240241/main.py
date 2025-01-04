# https://www.boot.dev/lessons/99641a42-62ea-4381-9450-d0103c240241

def find_min(nums):
    min_num = float('inf')
    for num in nums:
        if num < min_num:
            min_num = num
    return min_num
