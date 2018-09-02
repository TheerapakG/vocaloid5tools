import ctypes

class VSMSequenceData(ctypes.Structure):
    _fields_ = [("SamplingRate", ctypes.c_int),
                ("MaxNumTracks", ctypes.c_ulong),
                ("maxundocount", ctypes.c_ulong)]
