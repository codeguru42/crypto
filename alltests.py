import unittest

import s1c1
import s1c2
import s1c3
import s1c4


def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(s1c1.TestHexToBase64))
    suite.addTest(loader.loadTestsFromTestCase(s1c2.TestXor))
    suite.addTest(loader.loadTestsFromTestCase(s1c3.TestOneByteXor))
    suite.addTest(loader.loadTestsFromTestCase(s1c4.TestBreakAll))

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
