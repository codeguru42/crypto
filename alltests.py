import unittest
import s1c1
import s1c2

def suite():
  suite = unittest.TestSuite()
  loader = unittest.TestLoader()
  suite.addTest(loader.loadTestsFromTestCase(s1c1.TestHexToBase64))
  suite.addTest(loader.loadTestsFromTestCase(s1c2.TestXor))

  return suite

if __name__ == '__main__':
  runner = unittest.TextTestRunner()
  runner.run(suite())
