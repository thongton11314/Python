import unittest

class TestCase(unittest.TestCase):

    def testFunction(self):
        self.assertAlmostEqual(''.join(map(str, list(filter(lambda char: char in ['a', 'e', 'o', 'i', 'u'], "azcbobobegghakl")))), "aooea")

unittest.main()