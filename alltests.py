import unittest

import set1.c1
import set1.c2
import set1.c3
import set1.c4
import set1.c5
import set1.c6
import viginere


def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromModule(set1.c1))
    suite.addTest(loader.loadTestsFromModule(set1.c2))
    suite.addTest(loader.loadTestsFromModule(set1.c3))
    suite.addTest(loader.loadTestsFromModule(set1.c4))
    suite.addTest(loader.loadTestsFromModule(set1.c5))
    suite.addTest(loader.loadTestsFromModule(set1.c6))
    suite.addTest(loader.loadTestsFromModule(viginere))

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
