import unittest

import s1c1
import s1c2
import s1c3
import s1c4
import s1c5
import viginere


def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromModule(s1c1))
    suite.addTest(loader.loadTestsFromModule(s1c2))
    suite.addTest(loader.loadTestsFromModule(s1c3))
    suite.addTest(loader.loadTestsFromModule(s1c4))
    suite.addTest(loader.loadTestsFromModule(s1c5))
    suite.addTest(loader.loadTestsFromModule(viginere))

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
