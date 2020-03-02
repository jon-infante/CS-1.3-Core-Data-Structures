from hashtable import HashTable

class HashSet(object):

    def __init__(self, elements=None):
        """Initialize a new empty set structure, and add each element
        if a sequence is given."""
        self.hash = HashTable()
        self.size = 0
        if elements is not None:
            for item in elements:
                self.add(item)

    def size(self):
        """Property that tracks the number of elements in constant time.
        Time Complexity: O(1)"""
        return self.size

    def contains(self, element):
        """Return a boolean indicating whether element is in this set.
        Time Complexity: O(1) avg. from getting the hash value and traversing that bucket."""
        return self.hash.contains(element)

    def add(self, element):
        """Add element to this set, if not present already, else raise KeyError.
        Time Complexity: O(1) avg., worst being O(n) when we have to resize."""
        if self.contains(element):
            raise KeyError(f'Cannot add element to set again: {element}')
        else:
            self.hash.set(element, element)
            self.size += 1

    def remove(self, element):
        """Remove element from this set, if present, or else raise KeyError.
        Time Complexity: O(1) avg. from getting the hash value and traversing that bucket,
        and worst is O(n) if we have to resize smaller."""
        if not self.contains(element):
            raise KeyError(f'Element does not exist in the set: {element}')
        else:
            self.hash.delete(element)
            self.size -= 1

    def union(self, other_set):
        """Return a new set that is the union of this set and other_set.
        Time Complexity: O(n1 + n2)"""
        new_set = HashSet()
        for element in self.hash.values():
            new_set.add(element)
        #Adds remaining other_set elements
        for element in other_set.hash.values():
            if not new_set.contains(element):
                new_set.add(element)

        return new_set

    def intersection(self, other_set):
        """Return a new set that is the intersection of this set and other_set.
        Time Complexity: O(n)"""
        new_set = HashSet()
        for element in self.hash.values():
            if other_set.contains(element):
                new_set.add(element)

        return new_set

    def difference(self, other_set):
        """Return a new set that is the difference of this set and other_set.
        Time Complexity: O(n1 + n2)"""
        new_set = HashSet()
        for element in self.hash.values():
            new_set.add(element)
        #Removes intersected elements
        for element in other_set.hash.values():
            if new_set.contains(element):
                new_set.remove(element)

        return new_set

    def is_subset(self, other_set):
        """Return a boolean indicating whether other_set is a subset of this set.
        Time Complexity: O(n)"""
        var = 0
        #Checking if the first set is greater, would never be a subset
        if self.size > other_set.size:
            return False

        for element in other_set.hash.values():
            if self.contains(element):
                var += 1

        return self.size == var


def test_set():
    elements = ['A', 'B', 'D', 'F']
    elements2 = ['A', 'B', 'D', 'F', 'G', 'H']
    set = HashSet(elements)
    set2 = HashSet(elements2)
    # print(set.union(set2).hash.values())
    # print(set.intersection(set2).hash.values())
    # print(set.difference(set2).hash.values())
    print(set.is_subset(set2))


if __name__ == '__main__':
    test_set()
