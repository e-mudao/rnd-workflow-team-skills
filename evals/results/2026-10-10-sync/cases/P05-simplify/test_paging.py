import unittest
from paging import page_size

class PagingTests(unittest.TestCase):
    def test_default(self):
        self.assertEqual(page_size(), 50)
        self.assertEqual(page_size(None), 50)
    def test_explicit(self):
        self.assertEqual(page_size(7), 7)

if __name__ == "__main__":
    unittest.main()
