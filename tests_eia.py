# lint-amnesty, pylint: disable=missing-module-docstring

import unittest

from eia import *


class Test_Eia(unittest.TestCase):
    """ tests for  EIA"""

    def test_Eia(self):
        # Test cases. All of these should return True
        self.assertTrue(iseia(100))        # 100 ohm resistor is EIA
        self.assertFalse(iseia(101))    # 101 is not
        self.assertFalse(iseia(100.3))  # Floating point close to EIA is not EIA
        self.assertTrue(iseia(100.001))    # But within floating point error is
        self.assertTrue(iseia(1e5))        # We handle big numbers well
        self.assertTrue(iseia(2200))       # We handle middle-of-the-list well
        # We can handle 1% components correctly; 2.2k is EIA24, but not EIA48.
        self.assertFalse(iseia(2200, (E48, E96, E192)))
        self.assertTrue(iseia(5490e2, (E48, E96, E192)))
        self.assertTrue(iseia(2200))
        self.assertFalse(iseia(5490e2))
        self.assertTrue(iseia(1e-5))      # We handle little numbers well
        self.assertFalse(iseia("Hello"))  # Junk handled okay
        self.assertFalse(iseia(float('NaN')))
        self.assertFalse(iseia(-1))
        self.assertFalse(iseia(iseia))
        self.assertFalse(iseia(float('Inf')))
        self.assertTrue(iseia(0))  # Corner case. 0 is a standard resistor value.
