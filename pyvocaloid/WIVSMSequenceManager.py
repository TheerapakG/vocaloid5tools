import ctypes
import csharptypes
import os

import VSMResult
 
path = "vocaloid editor path: "
 
def load_vsm():
    global VIS_VSM_WIVSMSequenceManager_lastError
    VIS_VSM_WIVSMSequenceManager_lastError = vsm[]
    VIS_VSM_WIVSMSequenceManager_lastError.argtypes = [csharptypes.IntPtr]
    VIS_VSM_WIVSMSequenceManager_lastError.restype = ctypes.c_int
 
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
