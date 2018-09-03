# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type

import enum

class VSMSamplingRate(enum.IntEnum):
    _44100 = 44100
    _48000 = 48000
    _96000 = 96000
