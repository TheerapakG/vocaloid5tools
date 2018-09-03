# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type

import ctypes
import csharptypes
import os

import DSEManager
import DSEResult

path = "vocaloid editor path: "

def load_dse():
    global VIS_DSE_CreateManager
    VIS_DSE_CreateManager = dse[1]
    VIS_DSE_CreateManager.argtypes = []
    VIS_DSE_CreateManager.restype = csharptypes.IntPtr
    global VIS_DSE_DestroyManager
    VIS_DSE_DestroyManager = dse[2]
    VIS_DSE_DestroyManager.argtypes = [csharptypes.IntPtr]
    global VIS_DSE_HasManager
    VIS_DSE_HasManager = dse[10]
    VIS_DSE_HasManager.argtypes = [csharptypes.IntPtr]
    VIS_DSE_HasManager.restype = ctypes.c_bool
    global VIS_DSE_InitializeManager
    VIS_DSE_InitializeManager = dse[11]
    VIS_DSE_InitializeManager.argtypes = [csharptypes.IntPtr, csharptypes.IntPtr]
    VIS_DSE_InitializeManager.restype = ctypes.c_int
    global VIS_DSE_TerminateManager
    VIS_DSE_TerminateManager = dse[13]
    VIS_DSE_TerminateManager.argtypes = [csharptypes.IntPtr]
    VIS_DSE_TerminateManager.restype = ctypes.c_int

def load_dse_path():
    global dse
    os.chdir(path)
    dse = ctypes.cdll.LoadLibrary("dse.dll")
    load_dse()
    DSEManager.load_dse_dll(dse)

def load_dse_dll(dsedll):
    global dse
    dse = dsedll
    load_dse()
    DSEManager.load_dse_dll(dse)

class DSEManagerIF:

    def VIS_DSE_CreateManager():
        global VIS_DSE_CreateManager
        return VIS_DSE_CreateManager()

    def VIS_DSE_DestroyManager(pDSEManager):
        global VIS_DSE_DestroyManager
        return VIS_DSE_DestroyManager(pDSEManager)

    def VIS_DSE_HasManager(pDSEManager):
        global VIS_DSE_HasManager
        return VIS_DSE_HasManager(pDSEManager)

    def VIS_DSE_InitializeManager(pDSEManager, pDatabaseManager):
        global VIS_DSE_InitializeManager
        return VIS_DSE_InitializeManager(pDSEManager, pDatabaseManager)

    def VIS_DSE_TerminateManager(pDSEManager):
        global VIS_DSE_TerminateManager
        return VIS_DSE_TerminateManager(pDSEManager)

    def CreateManager(databaseManager):
        if(databaseManager == None):
            return None
        manager = csharptypes.IntPtr(DSEManagerIF.VIS_DSE_CreateManager())
        if(manager == csharptypes.IntPtr.Zero):
            return None
        if(DSEManagerIF.VIS_DSE_InitializeManager(manager, databaseManager.IntPtr()) != DSEResult.DSEResult.Successful):
            return None
        return DSEManager.DSEManager(manager)

    def HasManager(dseManager):
        if(dseManager != None):
            return DSEManagerIF.VIS_DSE_HasManager(dseManager.IntPtr())
        return False

    def DestroyManager(dseManager):
        if(dseManager == null):
            return
        if(DSEManagerIF.VIS_DSE_TerminateManager(dseManager.IntPtr()) != DSEResult.DSEResult.Successful):
            raise csharptypes.ApplicationException("DSEマネージャーの終了処理に失敗しました")
        DSEManagerIF.VIS_DSE_DestroyManager(dseManager.IntPtr())

if __name__ == '__main__':
    path = input(path)
    load_dse_path()
