# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type

import enum

class VSStyleError(enum.IntEnum):
    NotAny = 0
    InvalidArguments = 1
    InvalidHandle = 2
    OutOfMemory = 3
    ParentNotFound = 4
    TargetNotFound = 5
    UnmanagedObject = 6
    PathNotFound = 7
    FailedToOpenFile = 8
    FailedToRemoveFile = 9
    FailedToOverwriteFile = 10
    FailedToLoadModule = 11
    SymbolNotFound = 12
    ModuleNotLoaded = 13
    InvalidAppID = 14
    InvalidSysStyleDir = 15
    InvalidUserStyleDir = 16
    SDFFailedToParseJson = 17
    SDFInvalidStyle = 18
    SDFValueNotFound = 19
    SDFInvalidValue = 20
    SDFValueIsEmpty = 21
    SDFDuplicatedID = 22
    SDFEffectsNotFound = 23
    SDFInvalidStyleID = 24
    SDFInvalidStyleName = 25
    SDFInvalidJsonDoc = 26
    SDFInvalidFilterObj = 27
    SDFInvalidAudioEffectsObj = 28
    SDFInvalidAudioEffectObj = 29
    DuplicatedName = 30