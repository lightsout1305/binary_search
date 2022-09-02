"""
Basic binary search function
"""


def binary_search(lst, tgt):
    start = 0
    end = len(lst)
    steps = 0
    lst.sort()

    while start <= end:
        print(f'Step: {steps} {str(lst[start:end + 1])}')
        steps += 1
        middle = (start + end) // 2

        if tgt == lst[middle]:
            return f'Found element {middle}'
        elif tgt < lst[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return -1


binary_search([22, 23321, 1, 23, 7, 9, 10], 9)
