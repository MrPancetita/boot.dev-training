# https://www.boot.dev/lessons/ddf17bbc-a49c-4a37-85a6-f950a748eca1

def fizzbuzz(start, end):
    ans = []
    for i in range (start, end):
        if i % 3 == 0 and i % 5 == 0:
            ans.append("fizzbuzz")
        elif i % 3 == 0:
            ans.append("fizz")
        elif i % 5 == 0:
            ans.append("buzz")
        else:
            ans.append(i)
    return ans

