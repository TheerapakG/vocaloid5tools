# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type

import enum

class VDMError(enum.IntEnum):
    NotAny = 0
    OutOfMemory = 1
    FailedToLoadModule = 2
    ExportedSymbolNotFound = 3
    InvalidAppID = 4
    FailedToInitSetting = 5
    FailedToOpenSystemSetting = 6
    DatabaseKeyNotFound = 7
    InvalidComponent = 8
    UninstalledComponent = 9
    InvalidCompID = 10
    VoiceBankNotFound = 11
    ExpDBPathNotFound = 12
    InvalidVibratoTemplateType = 13
    ActivationInfoNotFound = 14
