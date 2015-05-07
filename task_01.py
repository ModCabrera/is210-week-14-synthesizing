#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fibonacci Sequence Generator"""

def xfibo(count):
    """Fibonacci Sequence Generator
    Args:
        iterator (int) = Placeholder for count of sequence iteration attempts.
        lasnum (int) = Last number in the sequence.
        currnum (int) = Current number in the sequence
        count (int) = The number of Fibonnaci Numbers.
    Examples:
        >>> for i in xfibo(5):
        ...     print i
        0
        1
        1
        2
        3
    """
    iterator = 0
    lastnum, curnum = 0, 1
    while iterator < count:
        iterator += 1
        yield lastnum
        curnum = lastnum+curnum
        iterator += 1
        yield curnum
        lastnum = lastnum+curnum
