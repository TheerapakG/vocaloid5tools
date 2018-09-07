# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type

#StyleManager.StyleManager

import ctypes
import csharptypes

import VSStyleError

path = "vocaloid editor path: "

def load_vsstyle():
    global Module_createStyleManager
    Module_createStyleManager = vsstyle[13]
    Module_createStyleManager.argtypes = [csharptypes.LPWStr, csharptypes.LPWStr, csharptypes.LPWStr, ctypes.c_void_p]
    VIS_VSM_WVSMModuleIF_createManager.restype = csharptypes.IntPtr
    """
    [DllImport("vsstyle", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool Module_hasStyleManager(IntPtr manager);
    """

def load_vsstyle_path():
    global vsstyle
    os.chdir(path)
    vsm = ctypes.cdll.LoadLibrary("vsstyle.dll")
    load_vsstyle()

def load_vsm_dll(vsstyledll):
    global vsstyle
    vsstyle = vsstyledll
    load_vsstyle()
    
class StyleManagerIF:
    
    def VIS_VSM_WVSMModuleIF_createManager(appId, systemStyleDirPath, userStyleDirPath, result_p):
        global VIS_VSM_WVSMModuleIF_createManager
        result_p = ctypes.cast(result_p, ctypes.c_void_p)
        temp = VIS_VSM_WVSMModuleIF_createManager(appId, systemStyleDirPath, userStyleDirPath, result_p)
        return temp
    
    def CreateStyleManager(appID, systemStyleDirPath, userStyleDirPath, result_p)
        result_p.value = VSStyleError.VSStyleError.NotAny;
        try:
            ctypes.cast(result_p, ctypes.c_void_p)
            styleManager = StyleManager.StyleManager(StyleManagerIF.Module_createStyleManager(appID, systemStyleDirPath, userStyleDirPath, result_p))
            if (result_p.value != VSStyleError.VSStyleError.NotAny):
                return None
            else:
                return styleManager
        except:
            return None

    """
    public static bool HasStyleManager(StyleManager manager)
    {
      if (manager == null)
        return false;
      return StyleManagerIF.Module_hasStyleManager((IntPtr) manager);
    """
