import ctypes
import csharptypes

import VSMError
import WIVSMSequenceManager

path = "vocaloid editor path: "

def load_vsm():
    global VIS_VSM_WVSMModuleIF_createManager
    VIS_VSM_WVSMModuleIF_createManager = vsm[649]
    VIS_VSM_WVSMModuleIF_createManager.argtypes = [csharptypes.LPWStr]
    VIS_VSM_WVSMModuleIF_createManager.restype = csharptypes.IntPtr
    global VIS_VSM_WVSMModuleIF_hasManager
    VIS_VSM_WVSMModuleIF_hasManager = vsm[650]
    VIS_VSM_WVSMModuleIF_hasManager.argtypes = [csharptypes.IntPtr]
    VIS_VSM_WVSMModuleIF_hasManager.restype = ctypes.c_bool
    global VIS_VSM_WVSMModuleIF_lastError
    VIS_VSM_WVSMModuleIF_lastError = vsm[651]
    VIS_VSM_WVSMModuleIF_lastError.argtypes = []
    VIS_VSM_WVSMModuleIF_lastError.restype = ctypes.c_int

def load_vsm_path():
    global vsm
    os.chdir(path)
    vsm = ctypes.cdll.LoadLibrary("vsm.dll")
    load_vsm()
    WIVSMSequenceManager.load_vsm_dll(vsm)

def load_vsm_dll(vsmdll):
    global vsm
    vsm = vsmdll
    load_vsm()
    WIVSMSequenceManager.load_vsm_dll(vsm)

class WVSMModuleIF:

    _managers = dict()

    def VIS_VSM_WVSMModuleIF_createManager(appId):
        global VIS_VSM_WVSMModuleIF_createManager
        return VIS_VSM_WVSMModuleIF_createManager(appId)

    def VIS_VSM_WVSMModuleIF_hasManager(pSequenceManager):
        global VIS_VSM_WVSMModuleIF_hasManager
        return VIS_VSM_WVSMModuleIF_hasManager(pSequenceManager)

    def VIS_VSM_WVSMModuleIF_lastError():
        global VIS_VSM_WVSMModuleIF_lastError
        return VIS_VSM_WVSMModuleIF_lastError()

    def CreateManager(appID):
        if(appID == None):
            return None
        if(appID == ""):
            return None
        if(appid in WVSMModuleIF._managers):
            return WIVSMSequenceManager(WVSMModuleIF._managers[appID], False)
        manager = WVSMModuleIF.VIS_VSM_WVSMModuleIF_createManager(appID)
        if (manager == csharptypes.IntPtr.Zero):
            return None
        WVSMModuleIF._managers[appID] = manager
        return WIVSMSequenceManager(manager, True)

    def HasManager(sequenceManager):
        if (sequenceManager == csharptypes.IntPtr.Zero):
            return False
        return WVSMModuleIF.VIS_VSM_WVSMModuleIF_hasManager(sequenceManager)

    def LastError():
        return WVSMModuleIF.VIS_VSM_WVSMModuleIF_lastError()
    

if(__name__ == "__main__"):
    path = input(path)
    load_vsm_path()
