import unittest


class TestHammingDistance(unittest.TestCase):
    def testCase(self):
        str1 = 'this is a test'
        str2 = 'wokka wokka!!!'
        expected = 37
        self.assertEqual(expected, hamming_distance(str1, str2))


if __name__ == "__main__":
    unittest.main()
