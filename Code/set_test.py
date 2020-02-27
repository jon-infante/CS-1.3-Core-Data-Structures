from set import HashSet
import unittest

class SetTest(unittest.TestCase):

    def test_init(self):
        elements = ['A', 'B', 'C']
        set = HashSet(elements)
        assert set.size is 3

    def test_size(self):
        elements = ['A', 'B', 'C', 'D', 'E']
        set = HashSet(elements)
        assert set.size is 5

    def test_contains(self):
        elements = ['P', 'C', 'X', 'U']
        set = HashSet(elements)
        assert set.contains('P') is True
        assert set.contains('C') is True
        assert set.contains('U') is True
        assert set.contains('D') is False
        assert set.contains('J') is False

    def test_add(self):
        elements = ['J', 'K']
        set = HashSet(elements)
        set.add('P')
        set.add('E')
        with self.assertRaises(KeyError):
            set.add('K')  # Element already exists
        with self.assertRaises(KeyError):
            set.add('E')  # Element already exists
        assert set.size is 4
        assert set.contains('P') is True
        assert set.contains('E') is True

    def test_remove(self):
        elements = ['U', '8', 'Q', 'D']
        set = HashSet(elements)
        with self.assertRaises(KeyError):
            set.remove('K')  # Element doesn't exist
        with self.assertRaises(KeyError):
            set.remove('0')  # Element doesn't exist
        set.remove('U')
        set.remove('Q')
        assert set.contains('U') is False
        assert set.contains('Q') is False
        with self.assertRaises(KeyError):
            set.remove('Q')  # Element doesn't exist anymore
    




if __name__ == '__main__':
    unittest.main()
