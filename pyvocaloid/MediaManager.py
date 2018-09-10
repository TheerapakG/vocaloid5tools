# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type

import ctypes
import csharptypes
import os

path = "vocaloid editor path: "

def load_vmm():
    global VIS_VMM_destroy
    VIS_VMM_destroy = vmm[55]
    VIS_VMM_destroy.argtypes = [cshrptypes.IntPtr]
    VIS_VMM_destroy.restype = ctypes.c_bool
    """
    [DllImport("vmm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VMM_Manager_appID(IntPtr manager);

    [DllImport("vmm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VMM_Manager_systemClipDirPath(IntPtr manager);

    [DllImport("vmm", CallingConvention = CallingConvention.Cdecl)]
    private static extern VMMError VIS_VMM_Manager_readAllClipFiles(IntPtr manager);

    [DllImport("vmm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VMM_Manager_numSystemClips(IntPtr manager, out UIntPtr numSystemClips);

    [DllImport("vmm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VMM_Manager_systemClip(IntPtr manager, UIntPtr index);

    [DllImport("vmm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VMM_Manager_hasSystemClip(IntPtr manager, IntPtr systemClip);

    [DllImport("vmm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VMM_Manager_userClipDirPath(IntPtr manager);

    [DllImport("vmm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VMM_Manager_numUserClips(IntPtr manager, out UIntPtr numUserClips);

    [DllImport("vmm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VMM_Manager_userClip(IntPtr manager, UIntPtr index);

    [DllImport("vmm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VMM_Manager_hasUserClip(IntPtr manager, IntPtr userClip);

    [DllImport("vmm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VMM_Manager_createMutableClip(IntPtr manager);

    [DllImport("vmm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VMM_Manager_hasMutableClip(IntPtr manager, IntPtr mutableClip);
    """
    pass

def load_vmm_path():
    global vmm
    os.chdir(path)
    vmm = ctypes.cdll.LoadLibrary("vmm.dll")
    load_vmm()

def load_vmm_dll(vmm):
    global vmm
    vmm = vmmdll
    load_vmm()
    StyleManager.load_vmm_dll(vmm)

class MediaManager:

    _cppObjPtr = csharptypes.IntPtr.Zero

    """
    public static explicit operator IntPtr(MediaManager obj)
    {
      return obj._cppObjPtr;
    }
    """
    
    def Dispose(self):
        MediaManager.VIS_VMM_Manager_destroy(self._cppObjPtr)
        self._cppObjPtr = csharptypes.IntPtr.Zero
    
    def __init__(self, pMediaManager):
        if (pMediaManager == csharptypes.IntPtr.Zero):
            raise csharptypes.ArgumentException("アンマネージオブジェクトではない")
        self._cppObjPtr = pMediaManager

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        MediaManager.VIS_VMM_Manager_destroy(self._cppObjPtr)
        self._cppObjPtr = csharptypes.IntPtr.Zero
    
    """
    public string AppID
    {
      get
      {
        return Marshal.PtrToStringUni(MediaManager.VIS_VMM_Manager_appID(this._cppObjPtr));
      }
    }

    public string SystemClipDirPath
    {
      get
      {
        return Marshal.PtrToStringUni(MediaManager.VIS_VMM_Manager_systemClipDirPath(this._cppObjPtr));
      }
    }

    public string UserClipDirPath
    {
      get
      {
        return Marshal.PtrToStringUni(MediaManager.VIS_VMM_Manager_userClipDirPath(this._cppObjPtr));
      }
    }

    public ulong NumSystemClips
    {
      get
      {
        UIntPtr numSystemClips = UIntPtr.Zero;
        if (!MediaManager.VIS_VMM_Manager_numSystemClips(this._cppObjPtr, out numSystemClips))
          return 0;
        if (UIntPtr.Size != 4)
          return numSystemClips.ToUInt64();
        return (ulong) numSystemClips.ToUInt32();
      }
    }

    public ulong NumUserClips
    {
      get
      {
        UIntPtr numUserClips = UIntPtr.Zero;
        if (!MediaManager.VIS_VMM_Manager_numUserClips(this._cppObjPtr, out numUserClips))
          return 0;
        if (UIntPtr.Size != 4)
          return numUserClips.ToUInt64();
        return (ulong) numUserClips.ToUInt32();
      }
    }

    public VMMError ReadAllClipFiles()
    {
      return MediaManager.VIS_VMM_Manager_readAllClipFiles(this._cppObjPtr);
    }

    public SystemClip SystemClip(ulong index)
    {
      return new SystemClip(MediaManager.VIS_VMM_Manager_systemClip(this._cppObjPtr, (UIntPtr) index));
    }

    public bool HasSystemClip(SystemClip systemClip)
    {
      return MediaManager.VIS_VMM_Manager_hasSystemClip(this._cppObjPtr, (IntPtr) ((ClipBase) systemClip));
    }

    public UserClip UserClip(ulong index)
    {
      return new UserClip(MediaManager.VIS_VMM_Manager_userClip(this._cppObjPtr, (UIntPtr) index));
    }

    public bool HasUserClip(UserClip userClip)
    {
      return MediaManager.VIS_VMM_Manager_hasUserClip(this._cppObjPtr, (IntPtr) ((ClipBase) userClip));
    }

    public MutableClip CreateMutableClip()
    {
      IntPtr mutableClip = MediaManager.VIS_VMM_Manager_createMutableClip(this._cppObjPtr);
      if (!(mutableClip == IntPtr.Zero))
        return new MutableClip(mutableClip);
      return (MutableClip) null;
    }

    public bool HasMutableClip(MutableClip mutableClip)
    {
      return MediaManager.VIS_VMM_Manager_hasMutableClip(this._cppObjPtr, (IntPtr) ((ClipBase) mutableClip));
    }
    """
