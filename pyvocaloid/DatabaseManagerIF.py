import ctypes
import csharptypes
import os

import DatabaseManager
import VDMError

path = "vocaloid editor path: "

def load_vdm():
    global VDM_createDatabaseManager
    VDM_createDatabaseManager = vdm[1]
    VDM_createDatabaseManager.argtypes = [csharptypes.LPWStr, csharptypes.LPWStr, ctypes.c_void_p]
    VDM_createDatabaseManager.restype = csharptypes.IntPtr
    global VDM_hasDatabaseManager
    VDM_hasDatabaseManager = vdm[86]
    VDM_hasDatabaseManager.argtypes = [csharptypes.IntPtr]
    VDM_hasDatabaseManager.restype = ctypes.c_bool

def load_vdm_path():
    global vdm
    os.chdir(path)
    vdm = ctypes.cdll.LoadLibrary("vdm.dll")
    load_vdm()
    DatabaseManager.load_vdm_dll(vdm)

def load_vdm_dll(vdmdll):
    global vdm
    vdm = vdmdll
    load_vdm()
    DatabaseManager.load_vdm_dll(vdm)

class DatabaseManagerIF:

    def VDM_createDatabaseManager(appID, expDBDirPath, result_p):
        global VDM_createDatabaseManager
        return VDM_createDatabaseManager(appID, expDBDirPath, result_p)

    def VDM_hasDatabaseManager(manager):
        global VDM_hasDatabaseManager
        return VDM_hasDatabaseManager(manager)

    def CreateDatabaseManager(appID, result_p):
        expDBDirPath = os.environ["CommonProgramFiles"] + "\\VOCALOID5\\Explib"
        if(expDBDirPath == None):
            return None
        elif(expDBDirPath == ""):
            return None
        try:
            databaseManager = DatabaseManager.DatabaseManager(DatabaseManagerIF.VDM_createDatabaseManager(appID, expDBDirPath, result_p))
            if(result_p.contents.value != VDMError.VDMError.NotAny):
                return None
            else:
                return databaseManager
        except:
            return None

    def HasDatabaseManager(manager):
        if(manager == None):
            return False
        return DatabaseManagerIF.VDM_hasDatabaseManager(manager.IntPtr())

if __name__ == '__main__':
    path = input(path)
    load_vdm_path()
