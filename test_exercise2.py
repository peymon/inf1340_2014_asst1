#!/usr/bin/env python3

""" Module to test exercise2.py """

__author__ = 'Peymon & Haoran'
__email__ = "Payran@payran.com"

__copyright__ = "2014 PayRan"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import pytest
from exercise2 import checksum


def test_checksum():
    """
    Inputs that are the correct format and length
    """
    assert checksum("786936224306") is True
    assert checksum("085392132225") is True
    assert checksum("717951000841") is False
    # other tests
    assert checksum("982437435435") is False
    assert checksum("922432635435") is False


def test_input():
    """
    Inputs that are the incorrect format and length
    """
    with pytest.raises(TypeError):
        checksum(1.0)
        checksum(786936224306)
        checksum(upccode)

    with pytest.raises(ValueError):
        checksum("1")
        checksum("1234567890")

        # other tests
        checksum("12343453389X")
        checksum("12343C53389X")


# add functions for any other tests
def test_zero():
    assert checksum("000000000000") is False