import ctypes
import csharptypes
from contextlib import contextmanager
import datetime

import LicenseResult
import enum

path = "vocaloid editor path: "

def load_dse():
    global VIS_DSE_GetCompIDFromLicense
    VIS_DSE_GetCompIDFromLicense = dse[3]
    VIS_DSE_GetCompIDFromLicense.argtypes = [csharptypes.IntPtr]
    VIS_DSE_GetCompIDFromLicense.restype = csharptypes.IntPtr
    global VIS_DSE_GetCompNameFromLicense
    VIS_DSE_GetCompNameFromLicense = dse[4]
    VIS_DSE_GetCompNameFromLicense.argtypes = [csharptypes.IntPtr]
    VIS_DSE_GetCompNameFromLicense.restype = csharptypes.IntPtr
    global VIS_DSE_GetResultFromLicense
    VIS_DSE_GetResultFromLicense = dse[9]
    VIS_DSE_GetResultFromLicense.argtypes = [csharptypes.IntPtr]
    VIS_DSE_GetResultFromLicense.restype = ctypes.c_int
    global VIS_DSE_GetExpiryDateFromLicense
    VIS_DSE_GetExpiryDateFromLicense = dse[7]
    VIS_DSE_GetExpiryDateFromLicense.argtypes = [csharptypes.IntPtr]
    VIS_DSE_GetExpiryDateFromLicense.restype = ctypes.c_long
    global VIS_DSE_GetCompVersionFromLicense
    VIS_DSE_GetCompVersionFromLicense = dse[6]
    VIS_DSE_GetCompVersionFromLicense.argtypes = [csharptypes.IntPtr, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
    VIS_DSE_GetCompVersionFromLicense.restype = ctypes.c_bool
    global VIS_DSE_GetCompTypeFromLicense
    VIS_DSE_GetCompTypeFromLicense = dse[5]
    VIS_DSE_GetCompTypeFromLicense.argtypes = [csharptypes.IntPtr]
    VIS_DSE_GetCompTypeFromLicense.restype = ctypes.c_int

def load_dse_path():
    global dse
    dse = ctypes.cdll.LoadLibrary(path+"\\dse.dll")
    load_dse()

def load_dse_dll(dsedll):
    global dse
    dse = dsedll
    load_dse()

class License:

    _dseLicense = csharptypes.IntPtr.Zero

    def VIS_DSE_GetCompIDFromLicense(dseLicense):
        global VIS_DSE_GetCompIDFromLicense
        return VIS_DSE_GetCompIDFromLicense(dseLicense)

    def VIS_DSE_GetCompNameFromLicense(dseLicense):
        global VIS_DSE_GetCompNameFromLicense
        return VIS_DSE_GetCompNameFromLicense(dseLicense)

    def VIS_DSE_GetResultFromLicense(dseLicense):
        global VIS_DSE_GetResultFromLicense
        return VIS_DSE_GetResultFromLicense(dseLicense)

    def VIS_DSE_GetExpiryDateFromLicense(dseLicense):
        global VIS_DSE_GetExpiryDateFromLicense
        return VIS_DSE_GetExpiryDateFromLicense(dseLicense)

    def VIS_DSE_GetCompVersionFromLicense(dseManager, major_p, minor_p, revision_p):
        global VIS_DSE_GetCompVersionFromLicense
        return VIS_DSE_GetCompVersionFromLicense(dseManager, major_p, minor_p, revision_p)

    def VIS_DSE_GetCompTypeFromLicense(dseLicense):
        global VIS_DSE_GetCompTypeFromLicense
        return VIS_DSE_GetCompTypeFromLicense(dseLicense)
    
    class Version(ctypes.Structure):
        _fields_ = [("Major", ctypes.c_int),
                    ("Minor", ctypes.c_int),
                    ("Revision", ctypes.c_int)]
        
    class Type(enum.IntEnum):
        Undefined = 0
        Application = 1
        Voice = 2

    def __init__(self, dseLicenseCPointer):
        if(dseLicenseCPointer == csharptypes.IntPtr.Zero):
            raise csharptypes.ArgumentNullException("supposedly: nameof (dseLicenseCPointer)")
        self._dseLicense = dseLicenseCPointer
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        DatabaseManager.VDM_DatabaseManager_destroy(self._dseLicense)
        self._dseLicense = csharptypes.IntPtr.Zero

    def get_CompID(self):
        return ctypes.cast(License.VIS_DSE_GetCompIDFromLicense(self._dseLicense), c_char_p).value

    CompID = property(get_CompID)

    def get_CompName(self):
        return ctypes.cast(License.VIS_DSE_GetCompNameFromLicense(self._dseLicense), c_char_p).value

    CompName = property(get_CompName)

    def get_CompVersion(self):
        version = License.Version(-1, -1, -1)
        License.VIS_DSE_GetCompVersionFromLicense(self._dseLicense, ctypes.cast(version.Major, ctypes.c_void_p), ctypes.cast(version.Minor, ctypes.c_void_p), ctypes.cast(version.Revision, ctypes.c_void_p))
        return version

    CompVersion = property(get_CompVersion)

    def get_CompType(self):
        compTypeFromLicense = License.VIS_DSE_GetCompTypeFromLicense(self._dseLicense)
        if (compTypeFromLicense >= 0):
            return License.Type(compTypeFromLicense)
        raise ApplicationException("Invalid return value from VIS_DSE_GetCompTypeFromLicense()")

    CompType = property(get_CompType)

    def get_Result(self):
        return License.VIS_DSE_GetResultFromLicense(self._dseLicense)

    Result = property(get_Result)

    def get_ExpiryDate(self):
        return datetime.datetime(1970, 1, 1, tzinfo = datetime.timezone(datetime.timedelta())) + datetime.timedelta(days = (License.VIS_DSE_GetExpiryDateFromLicense(self._dseLicense) / 3600*24)).astimezone()

    ExpiryDate = property(get_ExpiryDate)

if __name__ == '__main__':
    path = input(path)
    load_vdm_path()
