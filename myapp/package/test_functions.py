import unittest
import functions 

class test_package(unittest.TestCase):
    def test_add(self):
        assert functions.add(0,1) == 1
        
        


