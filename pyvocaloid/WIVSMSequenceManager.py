#WIVSMSequence.WIVSMSequence
#WIVSMClipboard.WIVSMClipboard

import ctypes
import csharptypes
import os

import WVSMModuleIF
import VSMResult

import VSMSequenceData
 
path = "vocaloid editor path: "
 
def load_vsm():
    global VIS_VSM_WIVSMSequenceManager_lastError
    VIS_VSM_WIVSMSequenceManager_lastError = vsm[445]
    VIS_VSM_WIVSMSequenceManager_lastError.argtypes = [csharptypes.IntPtr]
    VIS_VSM_WIVSMSequenceManager_lastError.restype = ctypes.c_int
    global VIS_VSM_WIVSMSequenceManager_destroy
    VIS_VSM_WIVSMSequenceManager_destroy = vsm[442]
    VIS_VSM_WIVSMSequenceManager_destroy.argtypes = [csharptypes.IntPtr]
    VIS_VSM_WIVSMSequenceManager_destroy.restype = ctypes.c_bool
    global VIS_VSM_WIVSMSequenceManager_createSequence
    VIS_VSM_WIVSMSequenceManager_createSequence = vsm[440]
    VIS_VSM_WIVSMSequenceManager_createSequence.argtypes = [csharptypes.IntPtr, ctypes.POINTER(VSMSequenceData.VSMSequenceData)]
    VIS_VSM_WIVSMSequenceManager_createSequence.restype = csharptypes.IntPtr
    global VIS_VSM_WIVSMSequenceManager_openSequence
    VIS_VSM_WIVSMSequenceManager_openSequence = vsm[449]
    VIS_VSM_WIVSMSequenceManager_openSequence.argtypes = [csharptypes.IntPtr, csharptypes.LPWStr, ctypes.POINTER(VSMSequenceData.VSMSequenceData)]
    VIS_VSM_WIVSMSequenceManager_openSequence.restype = csharptypes.IntPtr
    global VIS_VSM_WIVSMSequenceManager_openLegacySequence
    VIS_VSM_WIVSMSequenceManager_openLegacySequence = vsm[448]
    VIS_VSM_WIVSMSequenceManager_openLegacySequence.argtypes = [csharptypes.IntPtr, csharptypes.LPWStr, ctypes.POINTER(VSMSequenceData.VSMSequenceData), ctypes.c_uint, ctypes.c_bool]
    VIS_VSM_WIVSMSequenceManager_openLegacySequence.restype = csharptypes.IntPtr
    global VIS_VSM_WIVSMSequenceManager_lastErrorVsqParser
    VIS_VSM_WIVSMSequenceManager_lastErrorVsqParser = vsm[447]
    VIS_VSM_WIVSMSequenceManager_lastErrorVsqParser.argtypes = [csharptypes.IntPtr]
    VIS_VSM_WIVSMSequenceManager_lastErrorVsqParser.restype = ctypes.c_uint
    global VIS_VSM_WIVSMSequenceManager_lastErrorMessageVsqParser
    VIS_VSM_WIVSMSequenceManager_lastErrorMessageVsqParser = vsm[446]
    VIS_VSM_WIVSMSequenceManager_lastErrorMessageVsqParser.argtypes = [csharptypes.IntPtr]
    VIS_VSM_WIVSMSequenceManager_lastErrorMessageVsqParser.restype = csharptypes.IntPtr
    global VIS_VSM_WIVSMSequenceManager_hasSequence
    VIS_VSM_WIVSMSequenceManager_hasSequence = vsm[444]
    VIS_VSM_WIVSMSequenceManager_hasSequence.argtypes = [csharptypes.IntPtr, csharptypes.IntPtr]
    VIS_VSM_WIVSMSequenceManager_hasSequence.restype = ctypes.c_bool
    global VIS_VSM_WIVSMSequenceManager_createClipboard
    VIS_VSM_WIVSMSequenceManager_createClipboard = vsm[439]
    VIS_VSM_WIVSMSequenceManager_createClipboard.argtypes = [csharptypes.IntPtr]
    VIS_VSM_WIVSMSequenceManager_createClipboard.restype = csharptypes.IntPtr
    global VIS_VSM_WIVSMSequenceManager_databaseManager
    VIS_VSM_WIVSMSequenceManager_databaseManager = vsm[441]
    VIS_VSM_WIVSMSequenceManager_databaseManager.argtypes = [csharptypes.IntPtr]
    VIS_VSM_WIVSMSequenceManager_databaseManager.restype = csharptypes.IntPtr
    global VIS_VSM_WIVSMSequenceManager_setDatabaseManager
    VIS_VSM_WIVSMSequenceManager_setDatabaseManager = vsm[451]
    VIS_VSM_WIVSMSequenceManager_setDatabaseManager.argtypes = [csharptypes.IntPtr, csharptypes.IntPtr]
    global VIS_VSM_WIVSMSequenceManager_dseManager
    VIS_VSM_WIVSMSequenceManager_dseManager = vsm[443]
    VIS_VSM_WIVSMSequenceManager_dseManager.argtypes = [csharptypes.IntPtr]
    VIS_VSM_WIVSMSequenceManager_dseManager.restype = csharptypes.IntPtr
    global VIS_VSM_WIVSMSequenceManager_setDSEManager
    VIS_VSM_WIVSMSequenceManager_setDSEManager = vsm[450]
    VIS_VSM_WIVSMSequenceManager_setDSEManager.argtypes = [csharptypes.IntPtr, csharptypes.IntPtr]

def load_vsm_path():
    global vsm
    os.chdir(path)
    vsm = ctypes.cdll.LoadLibrary("vsm.dll")
    load_vsm()
 
def load_vsm_dll(vsmdll):
    global vsm
    vsm = vsmdll
    load_vsm()
 
class WIVSMSequenceManager:

    VSQ_ERROR_BASE = 2198274048
    VSQ_ERROR_LASTERRORVSQPARSER = WIVSMSequenceManager.VSQ_ERROR_BASE

    _cppObjPtr = csharptypes.IntPtr.Zero
 
    def VIS_VSM_WIVSMSequenceManager_lastError(cppobjptr):
        global VIS_VSM_WIVSMSequenceManager_lastError
        return VIS_VSM_WIVSMSequenceManager_lastError(cppobjptr)

    def VIS_VSM_WIVSMSequenceManager_destroy(cppobjptr):
        global VIS_VSM_WIVSMSequenceManager_destroy
        return VIS_VSM_WIVSMSequenceManager_destroy(cppobjptr)

    def VIS_VSM_WIVSMSequenceManager_createSequence(cppobjptr, sequenceData_p):
        global VIS_VSM_WIVSMSequenceManager_createSequence
        return VIS_VSM_WIVSMSequenceManager_createSequence(cppobjptr, sequenceData_p)

    def VIS_VSM_WIVSMSequenceManager_openSequence(filePath, vsqxSchemaDirPath, sequenceData_p):
        global VIS_VSM_WIVSMSequenceManager_openSequence
        return VIS_VSM_WIVSMSequenceManager_openSequence(filePath, vsqxSchemaDirPath, sequenceData_p)

    def VIS_VSM_WIVSMSequenceManager_openLegacySequence(cppobjptr, path, sequenceData_p, codePage, channelAsTrack):
        global VIS_VSM_WIVSMSequenceManager_openLegacySequence
        return VIS_VSM_WIVSMSequenceManager_openLegacySequence(cppobjptr, path, sequenceData_p, codePage, channelAsTrack)

    def VIS_VSM_WIVSMSequenceManager_lastErrorVsqParser(cppobjptr):
        global VIS_VSM_WIVSMSequenceManager_lastErrorVsqParser
        return VIS_VSM_WIVSMSequenceManager_lastErrorVsqParser(cppobjptr)

    def VIS_VSM_WIVSMSequenceManager_lastErrorMessageVsqParser(cppobjptr):
        global VIS_VSM_WIVSMSequenceManager_lastErrorMessageVsqParser
        return VIS_VSM_WIVSMSequenceManager_lastErrorMessageVsqParser(cppobjptr)

    def VIS_VSM_WIVSMSequenceManager_hasSequence(cppobjptr, sequence):
        global VIS_VSM_WIVSMSequenceManager_hasSequence
        return VIS_VSM_WIVSMSequenceManager_hasSequence(cppobjptr, sequence)

    def VIS_VSM_WIVSMSequenceManager_createClipboard(cppobjptr):
        global VIS_VSM_WIVSMSequenceManager_createClipboard
        return VIS_VSM_WIVSMSequenceManager_createClipboard(cppobjptr)

    def VIS_VSM_WIVSMSequenceManager_databaseManager(cppobjptr):
        global VIS_VSM_WIVSMSequenceManager_databaseManager
        return VIS_VSM_WIVSMSequenceManager_databaseManager(cppobjptr)

    def VIS_VSM_WIVSMSequenceManager_setDatabaseManager(cppobjptr, databaseManager):
        global VIS_VSM_WIVSMSequenceManager_setDatabaseManager
        return VIS_VSM_WIVSMSequenceManager_setDatabaseManager(cppobjptr, databaseManager)

    def VIS_VSM_WIVSMSequenceManager_dseManager(cppobjptr):
        global VIS_VSM_WIVSMSequenceManager_dseManager
        return VIS_VSM_WIVSMSequenceManager_dseManager(cppobjptr)

    def VIS_VSM_WIVSMSequenceManager_setDSEManager(cppobjptr, dseManager):
        global VIS_VSM_WIVSMSequenceManager_setDSEManager
        return VIS_VSM_WIVSMSequenceManager_setDSEManager(cppobjptr, dseManager)

    def IntPtr(obj):
        return obj._cppObjPtr

    def Equals(self, obj):
        if (obj == None):
            return False
        try:
            wivsmSequenceManager = type(self)(obj)
        except (TypeError, ValueError) as e:
            return False
        if (wivsmSequenceManager == None):
            return False
        return self._cppObjPtr == wivsmSequenceManager._cppObjPtr

    def GetHashCode(self):
        return self._cppObjPtr

    def Dispose(self, *args):
        if(len(args) == 0):
            self.Dispose(True)
            return
        if(len(args) == 1):
            if(disposing):
                num = 1
            else:
                num = 0
            if(self._isCreateUnmanagedObj):
                if(self._cppObjPtr != IntPtr.Zero):
                    if (not WIVSMSequenceManager.VIS_VSM_WIVSMSequenceManager_destroy(self._cppObjPtr)):
                        raise csharptypes.ApplicationException("シーケンスマネージャーの破棄に失敗した")
                    WVSMModuleIF.WVSMModuleIF.RemoveManager(self)
                    self._cppObjPtr = csharptypes.IntPtr.Zero
                self._isCreateUnmanagedObj = False
            else:
                self._cppObjPtr = csharptypes.IntPtr.Zero

    def __init__(self, pSeqMgr, isCreateUnmanagedObj = False):
        if (pSeqMgr == csharptypes.IntPtr.Zero):
            raise csharptypes.ArgumentException("アンマネージオブジェクトではない")
        self._isCreateUnmanagedObj = isCreateUnmanagedObj
        self._cppObjPtr = pSeqMgr

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.Dispose(False)
        
    def get_LastError(self):
        return WIVSMSequenceManager.VIS_VSM_WIVSMSequenceManager_lastError(self._cppObjPtr)

    LastError = property(get_LastError)

    def get_LastErrorVsqParser(self):
        return WIVSMSequenceManager.VIS_VSM_WIVSMSequenceManager_lastErrorVsqParser(self._cppObjPtr)

    LastErrorVsqParser = property(get_LastErrorVsqParser)

    def get_LastErrorMessageVsqParser(self):
        return ctypes.cast(WIVSMSequenceManager.VIS_VSM_WIVSMSequenceManager_lastErrorMessageVsqParser(self._cppObjPtr),ctypes.c_wchar_p).value

    LastErrorMessageVsqParser = property(get_LastErrorMessageVsqParser)

    def CreateSequence(self, sequenceData):
        sequence = WIVSMSequenceManager.VIS_VSM_WIVSMSequenceManager_createSequence(self._cppObjPtr, ctypes.pointer(sequenceData))
        if(not (sequence == csharptypes.IntPtr.Zero)):
            return WIVSMSequence.WIVSMSequence(sequence, True)
        return None

    def OpenSequence(self, filePath, vsqxSchemaDirPath, sequenceData):
        if (((filepath == None) or (filepath == "")) or ((vsqxSchemaDirPath == None) or (vsqxSchemaDirPath == ""))):
            return None
        pSequence = WIVSMSequenceManager.VIS_VSM_WIVSMSequenceManager_openSequence(self._cppObjPtr, filePath, vsqxSchemaDirPath, ctypes.pointer(sequenceData))
        if (!(pSequence == csharptypes.IntPtr.Zero)):
            return WIVSMSequence.WIVSMSequence(pSequence, True)
        return None

    def OpenLegacySequence(self, path, sequenceData, codePage, channelAsTrack):
        if (((path == None) or (path == ""))):
            return None
        pSequence = WIVSMSequenceManager.VIS_VSM_WIVSMSequenceManager_openLegacySequence(self._cppObjPtr, path, ctypes.pointer(sequenceData), codePage, channelAsTrack)
        if (!(pSequence == csharptypes.IntPtr.Zero)):
            return WIVSMSequence.WIVSMSequence(pSequence, True)
        return None

    def HasSequence(self, pSeq):
        if (pSeq == IntPtr.Zero):
            return False
        return WIVSMSequenceManager.VIS_VSM_WIVSMSequenceManager_hasSequence(self._cppObjPtr, pSeq)

    def CreateClipboard(self):
        clipboard = WIVSMSequenceManager.VIS_VSM_WIVSMSequenceManager_createClipboard(self._cppObjPtr);
        if (!(clipboard == csharptypes.IntPtr.Zero)):
            return WIVSMClipboard.WIVSMClipboard(clipboard)
        return None

    def SetDatabaseManager(self, databaseManager):
        if (databaseManager == None):
            return
        WIVSMSequenceManager.VIS_VSM_WIVSMSequenceManager_setDatabaseManager(self._cppObjPtr, databaseManager.IntPtr())

    def SetDSEManager(self, dseManager):
        if (dseManager == None):
            return
        WIVSMSequenceManager.VIS_VSM_WIVSMSequenceManager_setDSEManager(self._cppObjPtr, dseManager.IntPtr())
        
