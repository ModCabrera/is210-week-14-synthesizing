#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Function fibo uses List Comprehension and returns Fibonacci list."""

import task_01


def fibo(count):
    """Returns List of Fibonacci Numbers returned by task_01.xfibo().
    Args:
        None
    """
    return [item for item in task_01.xfibo(count)]
