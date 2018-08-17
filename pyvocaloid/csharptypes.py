import ctypes

IntPtr = ctypes.c_void_p
IntPtr.Zero = ctypes.c_void_p(0)

UIntPtr = ctypes.c_void_p
UIntPtr.Zero = ctypes.c_void_p(0)

LPWStr = ctypes.c_wchar_p

class ArgumentException(ValueError):
    pass
