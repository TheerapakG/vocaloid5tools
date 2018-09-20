# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type

import ctypes
import csharptypes

path = "vocaloid editor path: "

def load_vlc():
    global VIS_VLC_LuaControllerIF_create
    VIS_VLC_LuaControllerIF_create = vmm[1]
    VIS_VLC_LuaControllerIF_create.argtypes = []
    VIS_VLC_LuaControllerIF_create.restype = csharptypes.IntPtr
    global VIS_VLC_LuaControllerIF_open
    VIS_VLC_LuaControllerIF_open = vmm[6]
    VIS_VLC_LuaControllerIF_open.argtypes = [csharptypes.IntPtr, csharptypes.LPWStr]
    VIS_VLC_LuaControllerIF_open.restype = ctypes.c_bool
    global VIS_VLC_LuaControllerIF_createController
    VIS_VLC_LuaControllerIF_createController = vmm[2]
    VIS_VLC_LuaControllerIF_createController.argtypes = [csharptypes.IntPtr, csharptypes.LPWStr]
    VIS_VLC_LuaControllerIF_createController.restype = csharptypes.IntPtr

def load_vlc_path():
    global vlc
    os.chdir(path)
    vlc = ctypes.cdll.LoadLibrary("vlc.dll")
    load_vlc()

def load_vmm_dll(vlc):
    global vlc
    vlc = vlcdll
    load_vlc()

class LuaControllerIF:
    
    _cppObjPtr = csharptypes.IntPtr.Zero
    LuaModuleName = "vlc.dll"

    def VIS_VLC_LuaControllerIF_create():
        global VIS_VLC_LuaControllerIF_create
        return VIS_VLC_LuaControllerIF_create()
"""
    [DllImport("vlc", CallingConvention = CallingConvention.Cdecl)]
    private static extern void VIS_VLC_LuaControllerIF_destroy(IntPtr cppobjptr);
"""
    def VIS_VLC_LuaControllerIF_open(cppobjptr, dirPath):
        global VIS_VLC_LuaControllerIF_open
        return VIS_VLC_LuaControllerIF_open(cppobjptr, dirPath)
    
    def VIS_VLC_LuaControllerIF_createController(cppobjptr, appID):
        global VIS_VLC_LuaControllerIF_createController
        return VIS_VLC_LuaControllerIF_createController(cppobjptr, appID)
""""
    [DllImport("vlc", CallingConvention = CallingConvention.Cdecl)]
    private static extern void VIS_VLC_LuaControllerIF_destroyController(IntPtr cppobjptr, IntPtr controller);

    [DllImport("vlc", CallingConvention = CallingConvention.Cdecl)]
    private static extern VLCResult VIS_VLC_LuaControllerIF_lastError(IntPtr cppobjptr);

    public static explicit operator IntPtr(LuaControllerIF obj)
    {
      return obj._cppObjPtr;
    }
"""
    def __init__(self):
        self._cppObjPtr = LuaControllerIF.VIS_VLC_LuaControllerIF_create()
"""
    public void Dispose()
    {
      LuaControllerIF.VIS_VLC_LuaControllerIF_destroy(this._cppObjPtr);
      this._cppObjPtr = IntPtr.Zero;
      GC.SuppressFinalize((object) this);
    }

    ~LuaControllerIF()
    {
      LuaControllerIF.VIS_VLC_LuaControllerIF_destroy(this._cppObjPtr);
      this._cppObjPtr = IntPtr.Zero;
    }

    public VLCResult LastError
    {
      get
      {
        return LuaControllerIF.VIS_VLC_LuaControllerIF_lastError(this._cppObjPtr);
      }
    }

    public bool Open(string dirPath)
    {
      return LuaControllerIF.VIS_VLC_LuaControllerIF_open(this._cppObjPtr, dirPath);
    }

    public LuaController CreateController(string appID)
    {
      IntPtr controller = LuaControllerIF.VIS_VLC_LuaControllerIF_createController(this._cppObjPtr, appID);
      if (!(controller == IntPtr.Zero))
        return new LuaController(controller);
      return (LuaController) null;
    }

    public void DestroyController(LuaController controller)
    {
      if (controller == null)
        return;
      LuaControllerIF.VIS_VLC_LuaControllerIF_destroyController(this._cppObjPtr, (IntPtr) controller);
    }
  }
"""
