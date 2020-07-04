data = [0, 3, 4, 4, 4, 4, 6, 7, 9, 11, 12, 16, 22, 31, 32, 43]
target = 7


# Iterative binary search function
def binary_search(data, target):

    first = 0  # first index
    last = len(data) - 1  # last index

    while first <= last:
        # calculate middle index
        mid = (first + last) // 2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            last = mid - 1  # eliminate RHS
        else:
            first = mid + 1  # eliminate LHS
    return None


# tail-recursive binary search function
def binary_search_recursive(data, target, first_index, last_index):

    if first_index > last_index:
        return None
    if first_index <= last_index:
        mid = (first_index + last_index) // 2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            return binary_search_recursive(data, target, first_index, mid - 1)
        else:
            return binary_search_recursive(data, target, mid + 1, last_index)


def countOccurrences(item, data):

    def leftBoundary():
        first = 0  # first index
        last = len(data) - 1  # last index
        print(last)
        while first < last:
            # calculate middle index
            mid = (first + last) // 2
            if data[mid] < item:
                first = mid + 1
            else:
                last = mid
        return first

    def rightBoundary():
        first = 0  # first index
        last = len(data) - 1  # last index

        while first < last:
            # calculate middle index
            mid = (first + last) // 2
            if data[mid] > item:
                last = mid
            else:
                first = mid + 1
        return first

    return rightBoundary() - leftBoundary()


print(countOccurrences(4, data))
print(binary_search(data, target))
print(binary_search_recursive(data, target, 0, len(data) - 1))
