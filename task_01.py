#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module that returns actual date"""
import datetime

CURDATE = None


def get_current_date():
    """Return the date for today.
    Arg:
        None

    Returns:
        datetime.date.today() : Todays date.

    Examples:
        >>> get_current_date()
        datetime.date(2015, 3, 31)
    """
    return datetime.date.today()

if __name__ == '__main__':
    CURDATE = get_current_date()
