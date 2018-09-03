# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type

import ctypes

IntPtr = ctypes.c_void_p
IntPtr.Zero = ctypes.c_void_p(0)

UIntPtr = ctypes.c_void_p
UIntPtr.Zero = ctypes.c_void_p(0)

LPWStr = ctypes.c_wchar_p

class ArgumentException(ValueError):
    pass

class ArgumentNullException(ValueError):
    pass

class ApplicationException(BaseException):
    pass
