#!/usr/bin/env python3

""" Module to test exercise3.py """

__author__ = "Peymon & Haoran"
__email__ = "Payran@payran.com"

__copyright__ = "2014 PayRan"
__license__ = "MIT License"

__status__ = "Prototype"

import pytest
from exercise3 import decide_rps


def test_checksum():
    """
    Inputs that are the correct format and length
    """
    assert decide_rps("Rock", "Paper") == 2
    assert decide_rps("Scissors", "Scissors") == 0
    assert decide_rps("Rock", "Scissors") == 1
    # other tests
    assert decide_rps("Paper", "Rock") == 1
    assert decide_rps("Paper", "Paper") == 0


def test_input():
    """
    Inputs that are the incorrect format and length
    """
    with pytest.raises(TypeError):
        decide_rps(23, 34)
        decide_rps([2], [56])

    with pytest.raises(ValueError):
        decide_rps("paper", "rocks")
        decide_rps("rock", "papers")
