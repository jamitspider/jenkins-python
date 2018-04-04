import unittest
import __main__

class myClassTest(unittest.TestCase):
    
    def test_adding(self):
        
        a = 2
        b = 3
        self.assertEqual(a+b, 4)
        
if __name__ == '__main__':
    suit = unittest.TestLoader().loadTestsFromTestCase(myClassTest)
    unittest.TextTestRunner(verbosity=2).run(suit)