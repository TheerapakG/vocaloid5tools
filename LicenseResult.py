# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type

import enum

class LicenseResult(enum.IntEnum):
    Undefined = 0
    Trial = 1
    Expired = 2
    InvalidTrialKey = 3
    InvalidKey = 4
    InvalidSerialNumber = 5
    InvalidComponent = 6
    ExpiredKey = 7
    ValidExpiryKey = 8
    NoError = 9
