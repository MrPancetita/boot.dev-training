# https://www.boot.dev/lessons/f62840e0-ceea-417c-ad20-ed2e94abdde8

def remove_nonints(nums):
    int_nums = []
    for num in nums:
        if type(num) == int:
            int_nums.append(num)
    return int_nums
            
