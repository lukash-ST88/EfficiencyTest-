# эффективность O(n^2)
def selection_sort(lst: list) -> list:
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst


# максимальная эффективность O(n^2), минимальная эффективность O(n), средняя эффективность O(n^2)
def insertion_sort(lst: list) -> list:
    for i in range(1, len(lst)):
        for j in range(i, 0, -1):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
            else:
                break
    return lst


# максимальная эффективность O(n^2), минимальная эффективность O(n), средняя эффективность O(n^2)
def bubble_sort(lst: list) -> list:
    for i in range(len(lst)):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


# эффективность O(n * log(n))
def merge_sort(lst: list) -> list:
    def merge_list(a, b):
        c = []
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if a[i] > b[j]:
                c.append(b[j])
                j += 1
            else:
                c.append(a[i])
                i += 1
        c += a[i:] + b[j:]
        return c

    N = len(lst) // 2
    l1 = lst[:N]
    l2 = lst[N:]

    if len(l1) > 1:
        l1 = merge_sort(l1)
    if len(l2) > 1:
        l2 = merge_sort(l2)
    return merge_list(l1, l2)


# максимальная эффективность O(n^2), минимальная эффективность O(n * log(n)), средняя эффективность O(n * log(n))
def quick_sort(lst: list) -> list:
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[0]
        less = [i for i in lst[1:] if i <= pivot]
        greater = [i for i in lst[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
