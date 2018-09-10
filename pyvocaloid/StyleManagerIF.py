# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type

import ctypes
import csharptypes

import VSStyleError
import StyleManager

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
    vsstyle = ctypes.cdll.LoadLibrary("vsstyle.dll")
    load_vsstyle()
    StyleManager.load_vsstyle_dll(vsstyle)

def load_vsstyle_dll(vsstyledll):
    global vsstyle
    vsstyle = vsstyledll
    load_vsstyle()
    StyleManager.load_vsstyle_dll(vsstyle)
    
class StyleManagerIF:
    
    def Module_createStyleManager(appId, systemStyleDirPath, userStyleDirPath, result_p):
        global Module_createStyleManager
        result_p = ctypes.cast(result_p, ctypes.c_void_p)
        temp = Module_createStyleManager(appId, systemStyleDirPath, userStyleDirPath, result_p)
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
