import unittest

import set1.c1
import set1.c2
import set1.c3
import set1.c4
import set1.c5
import set1.c6
import set2.c9
import set2.c10
import viginere


def suite():
    s = unittest.TestSuite()
    loader = unittest.TestLoader()
    s.addTest(loader.loadTestsFromModule(set1.c1))
    s.addTest(loader.loadTestsFromModule(set1.c2))
    s.addTest(loader.loadTestsFromModule(set1.c3))
    s.addTest(loader.loadTestsFromModule(set1.c4))
    s.addTest(loader.loadTestsFromModule(set1.c5))
    s.addTest(loader.loadTestsFromModule(set1.c6))

    s.addTest(loader.loadTestsFromModule(set2.c9))
    s.addTest(loader.loadTestsFromModule(set2.c10))

    s.addTest(loader.loadTestsFromModule(viginere))

    return s


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
