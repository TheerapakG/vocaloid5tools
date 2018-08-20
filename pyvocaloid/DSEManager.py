import ctypes
import csharptypes

from contextlib import contextmanager
import os

import DSE_License

path = "vocaloid editor path: "

def load_dse():
    global VIS_DSE_NumLicenses
    VIS_DSE_NumLicenses = dse[12]
    VIS_DSE_NumLicenses.argtypes = [csharptypes.IntPtr]
    VIS_DSE_NumLicenses.restype = csharptypes.UIntPtr
    global VIS_DSE_GetLicense
    VIS_DSE_GetLicense = dse[8]
    VIS_DSE_GetLicense.argtypes = [csharptypes.IntPtr, csharptypes.UIntPtr]
    VIS_DSE_GetLicense.restype = csharptypes.IntPtr

def load_dse_path():
    global dse
    os.chdir(path)
    dse = ctypes.cdll.LoadLibrary("dse.dll")
    load_dse()

def load_dse_dll(dsedll):
    global dse
    dse = dsedll
    load_dse()

class DSEManager:

    _cppObjPtr = csharptypes.IntPtr.Zero

    def VIS_DSE_NumLicenses(dseManager):
        global VIS_DSE_NumLicenses
        return VIS_DSE_NumLicenses(dseManager)

    def VIS_DSE_GetLicense(dseManager, index):
        global VIS_DSE_GetLicense
        return VIS_DSE_GetLicense(dseManager, index)

    def IntPtr(self):
        return self._cppObjPtr

    def __init__(self, pDSEManager):
        if(pDSEManager == csharptypes.IntPtr.Zero):
            raise csharptypes.ArgumentException("アンマネージオブジェクトではない")
        self._cppObjPtr = pDSEManager
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        DatabaseManager.VDM_DatabaseManager_destroy(self._cppObjPtr)
        self._cppObjPtr = csharptypes.IntPtr.Zero

    def get_NumLicenses(self):
        num = DSEManager.VIS_DSE_NumLicenses(self._cppObjPtr)
        return num
    
    NumLicenses = property(get_NumLicenses)

    def GetLicense(self, index):
        _license = DSEManager.VIS_DSE_GetLicense(self._cppObjPtr, ctypes.cast(index, csharptypes.UIntPtr))
        if(not (_license == csharptypes.IntPtr.Zero)):
            return DSE_License.License(_license)
        return None

    def GetLicenses(self):
        licenseList = list()
        for index in range(0, self.NumLicenses):
            _license = self.GetLicense(index)
            if(_license != None):
                licenseList.append(_license)
        return licenseList

if __name__ == '__main__':
    path = input(path)
    load_dse_path()
