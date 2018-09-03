# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type

import ctypes

class VSMSequenceData(ctypes.Structure):
    _fields_ = [("SamplingRate", ctypes.c_int),
                ("MaxNumTracks", ctypes.c_ulong),
                ("maxundocount", ctypes.c_ulong)]
