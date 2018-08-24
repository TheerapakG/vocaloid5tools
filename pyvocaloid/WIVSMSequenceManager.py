import ctypes
import csharptypes
import os

import VSMResult
 
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
    VIS_VSM_WIVSMSequenceManager_createSequence.argtypes = [csharptypes.IntPtr, “pointer struct VSMSequenceData”]
    VIS_VSM_WIVSMSequenceManager_createSequence.restype = csharptypes.IntPtr
    global VIS_VSM_WIVSMSequenceManager_openSequence
    VIS_VSM_WIVSMSequenceManager_openSequence = vsm[449]
    VIS_VSM_WIVSMSequenceManager_openSequence.argtypes = [csharptypes.LPWStr, csharptypes.LPWStr, “pointer struct VSMSequenceData”]
    VIS_VSM_WIVSMSequenceManager_openSequence.restype = csharptypes.IntPtr

def load_vsm_path():
    global vsm
    os.chdir(path)
    vsm = ctypes.cdll.LoadLibrary("vsm.dll")
    load_vsm()
    DatabaseManager.load_vsm_dll(vsm)
 
def load_vsm_dll(vsmdll):
    global vsm
    vsm = vsmdll
    load_vsm()
    DatabaseManager.load_vsm_dll(vsm)
 
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

    def VIS_VSM_WIVSMSequenceManager_createSequence(cppobjptr, sequenceData):
        global VIS_VSM_WIVSMSequenceManager_createSequence
        return VIS_VSM_WIVSMSequenceManager_createSequence(cppobjptr, sequenceData)

    def VIS_VSM_WIVSMSequenceManager_openSequence(filePath, vsqxSchemaDirPath, sequenceData):
        global VIS_VSM_WIVSMSequenceManager_openSequence
        return VIS_VSM_WIVSMSequenceManager_openSequence(filePath, vsqxSchemaDirPath, sequenceData)
