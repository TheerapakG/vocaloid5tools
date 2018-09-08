# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type

import ctypes
import csharptypes
import os

path = "vocaloid editor path: "

def load_vsstyle():
    """
    [DllImport("vsstyle", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool StyleManager_destroy(IntPtr styleManagerHandle);

    [DllImport("vsstyle", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr StyleManager_appID(IntPtr styleManagerHandle);

    [DllImport("vsstyle", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr StyleManager_systemStyleDirPath(IntPtr styleManagerHandle);

    [DllImport("vsstyle", CallingConvention = CallingConvention.Cdecl)]
    private static extern VSStyleError StyleManager_readSystemStyles(IntPtr styleManagerHandle);

    [DllImport("vsstyle", CallingConvention = CallingConvention.Cdecl)]
    private static extern UIntPtr StyleManager_numSystemStyleCreationResult(IntPtr styleManagerHandle);

    [DllImport("vsstyle", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr StyleManager_systemStyleCreationResult(IntPtr styleManagerHandle, UIntPtr size_t_index);

    [DllImport("vsstyle", CallingConvention = CallingConvention.Cdecl)]
    private static extern UIntPtr StyleManager_numSystemStyle(IntPtr styleManagerHandle);

    [DllImport("vsstyle", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr StyleManager_systemStyle(IntPtr styleManagerHandle, UIntPtr size_t_index);

    [DllImport("vsstyle", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool StyleManager_hasSystemStyle(IntPtr styleManagerHandle, IntPtr systemStyleHandle);

    [DllImport("vsstyle", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr StyleManager_userStyleDirPath(IntPtr styleManagerHandle);

    [DllImport("vsstyle", CallingConvention = CallingConvention.Cdecl)]
    private static extern VSStyleError StyleManager_readUserStyles(IntPtr styleManagerHandle);

    [DllImport("vsstyle", CallingConvention = CallingConvention.Cdecl)]
    private static extern UIntPtr StyleManager_numUserStyleCreationResult(IntPtr styleManagerHandle);

    [DllImport("vsstyle", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr StyleManager_userStyleCreationResult(IntPtr styleManagerHandle, UIntPtr size_t_index);

    [DllImport("vsstyle", CallingConvention = CallingConvention.Cdecl)]
    private static extern UIntPtr StyleManager_numUserStyle(IntPtr styleManagerHandle);

    [DllImport("vsstyle", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr StyleManager_userStyle(IntPtr styleManagerHandle, UIntPtr size_t_index);

    [DllImport("vsstyle", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool StyleManager_hasUserStyle(IntPtr styleManagerHandle, IntPtr userStyleHandle);

    [DllImport("vsstyle", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr StyleManager_createMutableStyle(IntPtr styleManagerHandle);

    [DllImport("vsstyle", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool StyleManager_hasMutableStyle(IntPtr styleManagerHandle, IntPtr mutableStyleHandle);
    """
    pass

def load_vsstyle_path():
    global vsstyle
    os.chdir(path)
    vsstyle = ctypes.cdll.LoadLibrary("vsstyle.dll")
    load_vsstyle()

def load_vsstyle_dll(vsstyledll):
    global vsstyle
    vsstyle = vsstyledll
    load_vsstyle()
    
class StyleManager:
    
    _cppObjPtr = csharptypes.IntPtr.Zero

    def IntPtr(obj):
        return obj._cppObjPtr

    def __init__(self, pManager):
        if(type(pManager) is csharptypes.IntPtr):
            if (pManager == csharptypes.IntPtr.Zero):
                raise csharptypes.ArgumentException("アンマネージオブジェクトではない")
            self._cppObjPtr = pManager
        else if(type(pManager) is StyleManager):
            manager = pManager
            if (manager == None):
                raise csharptypes.ArgumentNullException("オブジェクトがnull")
            self._cppObjPtr = manager._cppObjPtr
        else:
            raise csharptypes.MultiTypeException("StyleManager.__init__")
            
    """
    
    public string AppID
    {
      get
      {
        return Marshal.PtrToStringUni(StyleManager.StyleManager_appID(this._cppObjPtr));
      }
    }

    public string SystemStyleDirPath
    {
      get
      {
        return Marshal.PtrToStringUni(StyleManager.StyleManager_systemStyleDirPath(this._cppObjPtr));
      }
    }

    public ulong NumSystemStyleCreationResult
    {
      get
      {
        UIntPtr num = StyleManager.StyleManager_numSystemStyleCreationResult(this._cppObjPtr);
        if (UIntPtr.Size != 4)
          return num.ToUInt64();
        return (ulong) num.ToUInt32();
      }
    }

    public ulong NumSystemStyle
    {
      get
      {
        UIntPtr num = StyleManager.StyleManager_numSystemStyle(this._cppObjPtr);
        if (UIntPtr.Size != 4)
          return num.ToUInt64();
        return (ulong) num.ToUInt32();
      }
    }

    public string UserStyleDirPath
    {
      get
      {
        return Marshal.PtrToStringUni(StyleManager.StyleManager_userStyleDirPath(this._cppObjPtr));
      }
    }

    public ulong NumUserStyleCreationResult
    {
      get
      {
        UIntPtr num = StyleManager.StyleManager_numUserStyleCreationResult(this._cppObjPtr);
        if (UIntPtr.Size != 4)
          return num.ToUInt64();
        return (ulong) num.ToUInt32();
      }
    }

    public ulong NumUserStyle
    {
      get
      {
        UIntPtr num = StyleManager.StyleManager_numUserStyle(this._cppObjPtr);
        if (UIntPtr.Size != 4)
          return num.ToUInt64();
        return (ulong) num.ToUInt32();
      }
    }

    public bool Destroy()
    {
      return StyleManager.StyleManager_destroy(this._cppObjPtr);
    }

    public StyleCreationResult SystemStyleCreationResult(ulong index)
    {
      return new StyleCreationResult(StyleManager.StyleManager_systemStyleCreationResult(this._cppObjPtr, (UIntPtr) index));
    }

    public VSStyleError ReadSystemStyles()
    {
      return StyleManager.StyleManager_readSystemStyles(this._cppObjPtr);
    }

    public SystemStyle SystemStyle(ulong index)
    {
      return new SystemStyle(StyleManager.StyleManager_systemStyle(this._cppObjPtr, (UIntPtr) index));
    }

    public bool HasSystemStyle(SystemStyle systemStyle)
    {
      return StyleManager.StyleManager_hasSystemStyle(this._cppObjPtr, (IntPtr) ((Style) systemStyle));
    }

    public VSStyleError ReadUserStyles()
    {
      return StyleManager.StyleManager_readUserStyles(this._cppObjPtr);
    }

    public StyleCreationResult UserStyleCreationResult(ulong index)
    {
      return new StyleCreationResult(StyleManager.StyleManager_userStyleCreationResult(this._cppObjPtr, (UIntPtr) index));
    }

    public UserStyle UserStyle(ulong index)
    {
      return new UserStyle(StyleManager.StyleManager_userStyle(this._cppObjPtr, (UIntPtr) index));
    }

    public bool HasUserStyle(UserStyle userStyle)
    {
      return StyleManager.StyleManager_hasUserStyle(this._cppObjPtr, (IntPtr) ((Style) userStyle));
    }

    public MutableStyle CreateMutableStyle()
    {
      return new MutableStyle(StyleManager.StyleManager_createMutableStyle(this._cppObjPtr));
    }

    public bool HasMutableStyle(MutableStyle mutableStyle)
    {
      return StyleManager.StyleManager_hasMutableStyle(this._cppObjPtr, (IntPtr) ((Style) mutableStyle));
    }

    public List<Style> GetAllStyles()
    {
      List<Style> styleList = new List<Style>();
      ulong numSystemStyle = this.NumSystemStyle;
      for (ulong index = 0; index < numSystemStyle; ++index)
      {
        if (this.SystemStyle(index) == null)
          return (List<Style>) null;
        styleList.Add((Style) this.SystemStyle(index));
      }
      ulong numUserStyle = this.NumUserStyle;
      for (ulong index = 0; index < numUserStyle; ++index)
      {
        if (this.UserStyle(index) == null)
          return (List<Style>) null;
        styleList.Add((Style) this.UserStyle(index));
      }
      return styleList;
    }

    public List<Style> SearchStyleByWordWithStyleList(List<Style> styleList, string searchWord)
    {
      if (styleList == null)
        return (List<Style>) null;
      List<Style> styleList1 = styleList;
      if (searchWord == null)
        return (List<Style>) null;
      searchWord = searchWord.ToLower();
      searchWord = searchWord.Replace("　", " ");
      searchWord = searchWord.Trim();
      string str1 = searchWord;
      char[] chArray = new char[1]{ ' ' };
      foreach (string str2 in str1.Split(chArray))
      {
        for (int index = styleList1.Count - 1; 0 <= index; --index)
        {
          Style style = styleList1[index];
          if (style == null)
            return (List<Style>) null;
          if (string.IsNullOrEmpty(style.Name))
            return (List<Style>) null;
          if (!style.Name.ToLower().Contains(str2))
            styleList1.RemoveAt(index);
        }
      }
      return styleList1;
    }

    public List<Style> SearchStyleByWord(string searchWord)
    {
      if (searchWord == null)
        return (List<Style>) null;
      List<Style> allStyles = this.GetAllStyles();
      if (allStyles == null)
        return (List<Style>) null;
      return this.SearchStyleByWordWithStyleList(allStyles, searchWord);
    }

    public List<Style> SearchStyleByTagWithStyleList(List<Style> styleList, List<string> genreTags, List<string> subGenreTags, List<string> colorTags)
    {
      if (styleList == null)
        return (List<Style>) null;
      List<Style> styleList1 = styleList;
      if (genreTags == null)
        return (List<Style>) null;
      if (subGenreTags == null)
        return (List<Style>) null;
      if (colorTags == null)
        return (List<Style>) null;
      foreach (string genreTag in genreTags)
      {
        if (genreTag == null)
          return (List<Style>) null;
        for (int index1 = styleList1.Count - 1; 0 <= index1; --index1)
        {
          Style style = styleList1[index1];
          if (style == null)
            return (List<Style>) null;
          bool flag = false;
          ulong numGenre = style.NumGenre;
          for (ulong index2 = 0; index2 < numGenre; ++index2)
          {
            if (genreTag == style.Genre(index2))
            {
              flag = true;
              break;
            }
          }
          if (!flag)
            styleList1.RemoveAt(index1);
        }
      }
      foreach (string subGenreTag in subGenreTags)
      {
        if (subGenreTag == null)
          return (List<Style>) null;
        for (int index1 = styleList1.Count - 1; 0 <= index1; --index1)
        {
          Style style = styleList1[index1];
          if (style == null)
            return (List<Style>) null;
          bool flag = false;
          ulong numSubGenre = style.NumSubGenre;
          for (ulong index2 = 0; index2 < numSubGenre; ++index2)
          {
            if (subGenreTag == style.SubGenre(index2))
            {
              flag = true;
              break;
            }
          }
          if (!flag)
            styleList1.RemoveAt(index1);
        }
      }
      foreach (string colorTag in colorTags)
      {
        if (colorTag == null)
          return (List<Style>) null;
        for (int index1 = styleList1.Count - 1; 0 <= index1; --index1)
        {
          Style style = styleList1[index1];
          if (style == null)
            return (List<Style>) null;
          bool flag = false;
          ulong numColor = style.NumColor;
          for (ulong index2 = 0; index2 < numColor; ++index2)
          {
            if (colorTag == style.Color(index2))
            {
              flag = true;
              break;
            }
          }
          if (!flag)
            styleList1.RemoveAt(index1);
        }
      }
      return styleList1;
    }

    public List<Style> SearchStyleByTag(List<string> genreTags, List<string> subGenreTags, List<string> colorTags)
    {
      if (genreTags == null)
        return (List<Style>) null;
      if (subGenreTags == null)
        return (List<Style>) null;
      if (colorTags == null)
        return (List<Style>) null;
      List<Style> allStyles = this.GetAllStyles();
      if (allStyles == null)
        return (List<Style>) null;
      return this.SearchStyleByTagWithStyleList(allStyles, genreTags, subGenreTags, colorTags);
    }
    """
