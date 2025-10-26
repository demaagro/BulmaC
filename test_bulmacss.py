# test_bulmacss.py
"""
Tests for BulmaCSS module.
"""

import unittest
from bulmacss import BulmaCSS

class TestBulmaCSS(unittest.TestCase):
    """Test cases for BulmaCSS class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BulmaCSS()
        self.assertIsInstance(instance, BulmaCSS)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BulmaCSS()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
