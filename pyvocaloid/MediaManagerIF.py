# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type

import ctypes
import csharptypes

import VMMError
import MediaManager

path = "vocaloid editor path: "

def load_vmm():
    global VIS_VMM_CreateManager
    VIS_VMM_CreateManager = vmm[21]
    VIS_VMM_CreateManager.argtypes = [csharptypes.LPWStr, csharptypes.LPWStr, csharptypes.LPWStr, ctypes.c_void_p]
    VIS_VMM_CreateManager.restype = csharptypes.IntPtr
    """
    [DllImport("vmm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VMM_HasManager(IntPtr manager);
    """

def load_vmm_path():
    global vmm
    os.chdir(path)
    vmm = ctypes.cdll.LoadLibrary("vmm.dll")
    load_vmm()
    MediaManager.load_vmm_dll(vmm)

def load_vmm_dll(vmm):
    global vmm
    vmm = vmmdll
    load_vmm()
    MediaManager.load_vmm_dll(vmm)

class MediaManagerIF:

    def VIS_VMM_CreateManager(appID, systemClipDirPath, userClipDirPath, result_p):
        global VIS_VMM_CreateManager
        result_p = ctypes.cast(result_p, ctypes.c_void_p)
        temp = Module_createStyleManager(appID, systemClipDirPath, userClipDirPath, result_p)
        return temp

    def CreateMediaManager(appID, systemClipDirPath, userClipDirPath, result_p):
        try:
            mediaManager = MediaManager.MediaManager(MediaManagerIF.VIS_VMM_CreateManager(appID, systemClipDirPath, userClipDirPath, result_p))
            if(result != VMMError.VMMError.NotAny):
                return None
            else:
                return mediaManager
        except:
            return None

    """
    public static bool HasMediaManager(MediaManager manager)
    {
      if (manager == null)
        return false;
      return MediaManagerIF.VIS_VMM_HasManager((IntPtr) manager);
    }
    """
