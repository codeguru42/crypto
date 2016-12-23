import unittest
import s1c1

def suite():
  suite = unittest.TestSuite()
  loader = unittest.TestLoader()
  suite.addTest(loader.loadTestsFromTestCase(s1c1.TestHexToBase64))

  return suite

if __name__ == '__main__':
  runner = unittest.TextTestRunner()
  runner.run(suite())
