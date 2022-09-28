import sys
import unittest

sys.path.append('..')
from hello_world import hello_world

class TestHelloWorld(unittest.TestCase):
    
    def test_hello_world(self):
        hello_world()
