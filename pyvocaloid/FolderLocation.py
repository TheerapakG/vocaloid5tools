# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type

import os

class FolderLocation:
    PathSystemData = os.environ["CommonProgramFiles"] + "\\VOCALOID5"
    PathUserData = os.environ["ApplicationData"] + "\\VOCALOID5"

    fNameApp = "VOCALOID5"
    fNameStylePreset = "StylePreset"
    fNameMedia = "Media"
    fNameMidiEffect = "MIDIEffect"
    fNameSingingSkill = "SingingSkill"
    fNameRobotVoice = "RobotVoice"
    fNameVoicelib = "Voicelib"
    fNameAttackReleaselib = "AttackReleaselib"
    fNameExplib = "Explib"
    fNameResource = "Resource"
    fNameVoice = "Voice"
    fNameAttackRelease = "AttackRelease"
    fNameIcon = "Icon"
    fNamePreview = "Preview"
    fNameUdic = "Udic"
    fNameShortcut = "Shortcut"
    fNameContentsList = "Contents"

FolderLocation.PathSystemStylePreset = FolderLocation.PathSystemData + "\\StylePreset"
FolderLocation.PathSystemMedia = FolderLocation.PathSystemData + "\\Media"
FolderLocation.PathSystemMESingingSkill = FolderLocation.PathSystemData + "\\MIDIEffect" + "\\SingingSkill"
FolderLocation.PathSystemMERobotVoice = FolderLocation.PathSystemData + "\\MIDIEffect" + "\\RobotVoice"
FolderLocation.PathSystemVoicelib = FolderLocation.PathSystemData + "\\Voicelib"
FolderLocation.PathSystemAttackReleaselib = FolderLocation.PathSystemData + "\\AttackReleaselib"
FolderLocation.PathSystemExplib = FolderLocation.PathSystemData + "\\Explib"
FolderLocation.PathSystemRscVoice = FolderLocation.PathSystemData + "\\Resource" + "\\Voice"
FolderLocation.PathSystemRscARIcon = FolderLocation.PathSystemData + "\\Resource" + "\\AttackRelease" + "\\Icon"
FolderLocation.PathSystemRscARPreview = FolderLocation.PathSystemData + "\\Resource" + "\\AttackRelease" + "\\Preview"

FolderLocation.PathUserStylePreset = FolderLocation.PathUserData + "\\StylePreset"
FolderLocation.PathUserMedia = FolderLocation.PathUserData + "\\Media"
FolderLocation.PathUserMESingingSkill = FolderLocation.PathUserData + "\\MIDIEffect" + "\\SingingSkill"
FolderLocation.PathUserUdic = FolderLocation.PathUserData + "\\Udic"
FolderLocation.PathUserShortcut = FolderLocation.PathUserData + "\\Shortcut"
FolderLocation.PathUserContentsList = FolderLocation.PathUserData + "\\Contents"