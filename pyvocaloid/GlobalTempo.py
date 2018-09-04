# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type

import ctypes
import csharptypes
import os

path = "vocaloid editor path: "

def load_vsm():
    """
    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_isGlobalTempoEnabled(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_enableGlobalTempo(IntPtr cppobjptr, [MarshalAs(UnmanagedType.U1)] bool enable);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern int VIS_VSM_WIVSMSequence_globalTempo(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_setGlobalTempo(IntPtr cppobjptr, int value);
    """
    pass

def load_vsm_path():
    global vsm
    os.chdir(path)
    vsm = ctypes.cdll.LoadLibrary("vsm.dll")
    load_vsm()
 
def load_vsm_dll(vsmdll):
    global vsm
    vsm = vsmdll
    load_vsm()
    
class GlobalTempo:
    
    _sequence = csharptypes.IntPtr.Zero

    def __init__(self, sequence):
        if (sequence == csharptypes.IntPtr.Zero):
            raise csharptypes.ArgumentNullException("nameof (sequence)")
        self._sequence = sequence

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    """
    public bool IsEnabled
    {
      get
      {
        return GlobalTempo.VIS_VSM_WIVSMSequence_isGlobalTempoEnabled(this._sequence);
      }
      set
      {
        if (!GlobalTempo.VIS_VSM_WIVSMSequence_enableGlobalTempo(this._sequence, value))
          throw new ArgumentException("null or invalid", "_sequence");
      }
    }

    public int Value
    {
      get
      {
        int num = GlobalTempo.VIS_VSM_WIVSMSequence_globalTempo(this._sequence);
        if (num != int.MinValue)
          return num;
        throw new ArgumentException("null or invalid", "_sequence");
      }
      set
      {
        if (GlobalTempo.VIS_VSM_WIVSMSequence_setGlobalTempo(this._sequence, value))
          return;
        if (value < WIVSMTempo.MinValue || WIVSMTempo.MaxValue < value)
          throw new ArgumentOutOfRangeException(nameof (value));
        throw new ArgumentException("null or invalid", "_sequence");
      }
    }
    """
