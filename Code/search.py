#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_recursive(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    """Incrementing index until item is found in the array iteratively.

        array: list
        item: str

        Best case running time: O(1) if the item is at the beginning of the array.
        Worst case running time: O(n) if the item is last in the array.
        """
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    """Incrementing index until item is found in the array recursively.

        array: list
        item: str

        Best case running time: O(1) if the item is at the beginning of the array.
        Worst case running time: O(n) if the item is last in the array.
        """
    if index > (len(array) - 1):
        return None

    if item == array[index]:
        return index
    else:
        return linear_search_recursive(array, item, index+1)


    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_recursive(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    """Searches through a sorted array and navigates through it iteratively using
    binary search.
    Best case running time: O(1) if the item is in the middle of the array.
    Worst case running time: O(logn) if the item is last in the binary search.
    """
    min = 0
    max = len(array) - 1
    while max >= min:
        target = (max + min) // 2
        if item > array[target]:
            min = target + 1
        elif item < array[target]:
            max = target - 1
        else:
            return target

    return None
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    """Searches through a sorted array and navigates through it recursively using
    binary search.
    Best case running time: O(1) if the item is in the middle of the array.
    Worst case running time: O(logn) if the item is last in the binary search.
    """
    if left == None:
        left = 0
        right = len(array) - 1
    if right >= left:
        target = (right + left) // 2
        if item > array[target]:
            return binary_search_recursive(array, item, target+1, right)
        elif item < array[target]:
            return binary_search_recursive(array, item, left, target-1)
        else:
            return target

    return None
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

if __name__ == '__main__':
    names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
    print(binary_search_iterative(names, 'Winnie'))
