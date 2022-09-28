import unittest

from .. import hello_world

class TestHelloWorld(unittest.TestCase):
    
    def test_hello_world(self):
        hello_world()

if __name__ == '__main__':
    unittest.main()