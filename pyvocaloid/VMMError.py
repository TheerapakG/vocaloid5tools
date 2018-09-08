# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type

import enum

class VMMError(enum.IntEnum):
    NotAny = 0
    OutOfMemory = 1
    InvalidArgument = 2
    ModuleNotFound = 3
    FailedToLoadModule = 4
    SymbolNotFound = 5
    InvalidAppID = 6
    SysClipDirNotFound = 7
    FailedToCreateDir = 8
    UserClipDirNotFound = 9
    EmptyName = 10
    DuplicatedName = 11
    UnmanagedObject = 12
    PartNotFound = 13
    WavFileNotFound = 14
    FailedToCopyFile = 15
    FailedToOpenFile = 16
    FailedToSaveMutableClip = 17
    EmptyVoiceBankID = 18
    InvalidLangID = 19
