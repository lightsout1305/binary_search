"""
Basic binary search function, it takes list of elements and a searched element as positional arguments
PS: It looks only for elements that are present in the list
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

