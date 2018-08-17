#VoiceBank
#VibratoBank
#DvqmDB
#XSynthGroup

import ctypes
import csharptypes
from contextlib import contextmanager

path = "vocaloid editor path: "

def load_vdm():
    global VDM_hasDatabaseManager
    VDM_hasDatabaseManager = vdm[86]
    VDM_hasDatabaseManager.argtypes = [csharptypes.IntPtr]
    VDM_hasDatabaseManager.restype = ctypes.c_bool
    global VDM_DatabaseManager_destroy
    VDM_DatabaseManager_destroy = vdm[5]
    VDM_DatabaseManager_destroy.argtypes = [csharptypes.IntPtr]
    VDM_DatabaseManager_destroy.restype = None
    global VDM_DatabaseManager_appID
    VDM_DatabaseManager_appID = vdm[3]
    VDM_DatabaseManager_appID.argtypes = [csharptypes.IntPtr]
    VDM_DatabaseManager_appID.restype = csharptypes.IntPtr
    global VDM_DatabaseManager_numVoiceBanks
    VDM_DatabaseManager_numVoiceBanks = vdm[10]
    VDM_DatabaseManager_numVoiceBanks.argtypes = [csharptypes.IntPtr]
    VDM_DatabaseManager_numVoiceBanks.restype = csharptypes.UIntPtr
    global VDM_DatabaseManager_defaultVoiceBank
    VDM_DatabaseManager_defaultVoiceBank = vdm[4]
    VDM_DatabaseManager_defaultVoiceBank.argtypes = [csharptypes.IntPtr]
    VDM_DatabaseManager_defaultVoiceBank.restype = csharptypes.IntPtr
    global VDM_DatabaseManager_voiceBankByIndex
    VDM_DatabaseManager_voiceBankByIndex = vdm[15]
    VDM_DatabaseManager_voiceBankByIndex.argtypes = [csharptypes.IntPtr, csharptypes.UIntPtr]
    VDM_DatabaseManager_voiceBankByIndex.restype = csharptypes.IntPtr
    global VDM_DatabaseManager_voiceBankByCompID
    VDM_DatabaseManager_voiceBankByCompID = vdm[14]
    VDM_DatabaseManager_voiceBankByCompID.argtypes = [csharptypes.IntPtr, csharptypes.LPWStr]
    VDM_DatabaseManager_voiceBankByCompID.restype = csharptypes.IntPtr
    global VDM_DatabaseManager_voiceBankByBSPC
    VDM_DatabaseManager_voiceBankByBSPC = vdm[13]
    VDM_DatabaseManager_voiceBankByBSPC.argtypes = [csharptypes.IntPtr, ctypes.c_int, ctypes.c_int]
    VDM_DatabaseManager_voiceBankByBSPC.restype = csharptypes.IntPtr
    global VDM_DatabaseManager_numVibratoBanks
    VDM_DatabaseManager_numVibratoBanks = vdm[9]
    VDM_DatabaseManager_numVibratoBanks.argtypes = [csharptypes.IntPtr]
    VDM_DatabaseManager_numVibratoBanks.restype = csharptypes.UIntPtr
    global VDM_DatabaseManager_vibratoBank
    VDM_DatabaseManager_vibratoBank = vdm[12]
    VDM_DatabaseManager_vibratoBank.argtypes = [csharptypes.IntPtr, csharptypes.UIntPtr]
    VDM_DatabaseManager_vibratoBank.restype = csharptypes.IntPtr
    global VDM_DatabaseManager_numDvqmDBs
    VDM_DatabaseManager_numDvqmDBs = vdm[8]
    VDM_DatabaseManager_numDvqmDBs.argtypes = [csharptypes.IntPtr]
    VDM_DatabaseManager_numDvqmDBs.restype = csharptypes.UIntPtr
    global VDM_DatabaseManager_dvqmDBByIndex
    VDM_DatabaseManager_dvqmDBByIndex = vdm[7]
    VDM_DatabaseManager_dvqmDBByIndex.argtypes = [csharptypes.IntPtr, csharptypes.IntPtr]
    VDM_DatabaseManager_dvqmDBByIndex.restype = csharptypes.IntPtr
    global VDM_DatabaseManager_dvqmDBByID
    VDM_DatabaseManager_dvqmDBByID = vdm[6]
    VDM_DatabaseManager_dvqmDBByID.argtypes = [csharptypes.IntPtr, ctypes.c_int]
    VDM_DatabaseManager_dvqmDBByID.restype = csharptypes.IntPtr
    global VDM_DatabaseManager_numXSynthGroups
    VDM_DatabaseManager_numXSynthGroups = vdm[11]
    VDM_DatabaseManager_numXSynthGroups.argtypes = [csharptypes.IntPtr]
    VDM_DatabaseManager_numXSynthGroups.restype = csharptypes.UIntPtr
    global VDM_DatabaseManager_xsynthGroup
    VDM_DatabaseManager_xsynthGroup = vdm[16]
    VDM_DatabaseManager_xsynthGroup.argtypes = [csharptypes.IntPtr, csharptypes.UIntPtr]
    VDM_DatabaseManager_xsynthGroup.restype = csharptypes.IntPtr

def load_vdm_path():
    global vdm
    vdm = ctypes.cdll.LoadLibrary(path+"\\vdm.dll")
    load_vdm()

def load_vdm_dll(vdmdll):
    global vdm
    vdm = vdmdll
    load_vdm()

class DatabaseManager:
    
    _cppObjPtr = csharptypes.IntPtr.Zero
    
    def VDM_hasDatabaseManager(manager):
        global VDM_hasDatabaseManager
        return VDM_hasDatabaseManager(manager)
    
    def VDM_DatabaseManager_destroy(manager):
        global VDM_DatabaseManager_destroy
        return VDM_DatabaseManager_destroy(manager)
    
    def VDM_DatabaseManager_appID(manager):
        global VDM_DatabaseManager_appID
        return VDM_DatabaseManager_appID(manager)
    
    def VDM_DatabaseManager_numVoiceBanks(manager):
        global VDM_DatabaseManager_numVoiceBanks
        return VDM_DatabaseManager_numVoiceBanks(manager)
    
    def VDM_DatabaseManager_defaultVoiceBank(manager):
        global VDM_DatabaseManager_defaultVoiceBank
        return VDM_DatabaseManager_defaultVoiceBank(manager)
    
    def VDM_DatabaseManager_voiceBankByIndex(manager, index):
        global VDM_DatabaseManager_voiceBankByIndex
        return VDM_DatabaseManager_voiceBankByIndex(manager, index)
    
    def VDM_DatabaseManager_voiceBankByCompID(manager, compID):
        global VDM_DatabaseManager_voiceBankByCompID
        return VDM_DatabaseManager_voiceBankByCompID(manager, compID)
    
    def VDM_DatabaseManager_voiceBankByBSPC(manager, bs, pc):
        global VDM_DatabaseManager_voiceBankByBSPC
        return VDM_DatabaseManager_voiceBankByBSPC(manager, bs, pc)
    
    def VDM_DatabaseManager_numVibratoBanks(manager):
        global VDM_DatabaseManager_numVibratoBanks
        return VDM_DatabaseManager_numVibratoBanks(manager)
    
    def VDM_DatabaseManager_vibratoBank(manager, index):
        global VDM_DatabaseManager_vibratoBank
        return VDM_DatabaseManager_vibratoBank(manager, index)
    
    def VDM_DatabaseManager_voiceBankByIndex(manager, size_t_index):
        global VDM_DatabaseManager_voiceBankByIndex
        return VDM_DatabaseManager_voiceBankByIndex(manager, size_t_index)
    
    def VDM_DatabaseManager_numDvqmDBs(manager):
        global VDM_DatabaseManager_numDvqmDBs
        return VDM_DatabaseManager_numDvqmDBs(manager)
    
    def VDM_DatabaseManager_dvqmDBByIndex(manager, size_t_index):
        global VDM_DatabaseManager_dvqmDBByIndex
        return VDM_DatabaseManager_dvqmDBByIndex(manager, size_t_index)
    
    def VDM_DatabaseManager_dvqmDBByID(manager, ide):
        global VDM_DatabaseManager_dvqmDBByID
        return VDM_DatabaseManager_dvqmDBByID(manager, ide)
    
    def VDM_DatabaseManager_numXSynthGroups(manager):
        global VDM_DatabaseManager_numXSynthGroups
        return VDM_DatabaseManager_numXSynthGroups(manager)
    
    def VDM_DatabaseManager_xsynthGroup(manager, size_t_index):
        global VDM_DatabaseManager_xsynthGroup
        return VDM_DatabaseManager_xsynthGroup(manager, size_t_index)
    
    def IntPtr(self):
        return self._cppObjPtr
    
    def __init__(self, pDatabaseManager):
        if(pDatabaseManager == csharptypes.IntPtr.Zero):
            raise csharptypes.ArgumentException("アンマネージオブジェクトではない")
        self._cppObjPtr = pDatabaseManager
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        DatabaseManager.VDM_DatabaseManager_destroy(self._cppObjPtr)
        self._cppObjPtr = csharptypes.IntPtr.Zero
    
    def get_AppID(self):
        return DatabaseManager.VDM_DatabaseManager_appID(self._cppObjPtr)
    
    AppID = property(get_AppID)
    
    def get_NumVoiceBanks(self):
        num = DatabaseManager.VDM_DatabaseManager_numVoiceBanks(self._cppObjPtr)
        return num
    
    NumVoiceBanks = property(get_NumVoiceBanks)
    
    """
    public VoiceBank DefaultVoiceBank
    {
      get
      {
        IntPtr pVoiceBank = DatabaseManager.VDM_DatabaseManager_defaultVoiceBank(this._cppObjPtr);
        if (!(pVoiceBank == IntPtr.Zero))
          return new VoiceBank(pVoiceBank);
        return (VoiceBank) null;
      }
    }
    """
    
    def get_NumVibratoBanks(self):
        num = DatabaseManager.VDM_DatabaseManager_numVibratoBanks(self._cppObjPtr)
        return num
    
    NumVibratoBanks = property(get_NumVibratoBanks)
    
    def get_NumDvqmDBs(self):
        num = DatabaseManager.VDM_DatabaseManager_numDvqmDBs(self._cppObjPtr)
        return num
    
    NumDvqmDBs = property(get_NumDvqmDBs)
    
    def get_NumXSynthGroups(self):
        num = DatabaseManager.VDM_DatabaseManager_numXSynthGroups(self._cppObjPtr)
        return num
    
    NumXSynthGroups = property(get_NumXSynthGroups)
    
    def HasDatabaseManager(self, manager):
        if (manager == None):
            return false
        return DatabaseManager.VDM_hasDatabaseManager(manager._cppObjPtr)
    
    """
    public VoiceBank GetVoiceBankByIndex(ulong index)
    {
      IntPtr pVoiceBank = DatabaseManager.VDM_DatabaseManager_voiceBankByIndex(this._cppObjPtr, (UIntPtr) index);
      if (!(pVoiceBank == IntPtr.Zero))
        return new VoiceBank(pVoiceBank);
      return (VoiceBank) null;
    }
    """
    
    """
    public VoiceBank GetVoiceBankByCompID(string compID)
    {
      IntPtr pVoiceBank = DatabaseManager.VDM_DatabaseManager_voiceBankByCompID(this._cppObjPtr, compID);
      if (!(pVoiceBank == IntPtr.Zero))
        return new VoiceBank(pVoiceBank);
      return (VoiceBank) null;
    }
    """
    
    """
    public VoiceBank GetVoiceBankByBSPC(int bs, int pc)
    {
      IntPtr pVoiceBank = DatabaseManager.VDM_DatabaseManager_voiceBankByBSPC(this._cppObjPtr, bs, pc);
      if (!(pVoiceBank == IntPtr.Zero))
        return new VoiceBank(pVoiceBank);
      return (VoiceBank) null;
    }
    """
    
    """
    public VibratoBank GetVibratoBank(ulong index)
    {
      IntPtr pVibratoBank = DatabaseManager.VDM_DatabaseManager_vibratoBank(this._cppObjPtr, (UIntPtr) index);
      if (!(pVibratoBank == IntPtr.Zero))
        return new VibratoBank(pVibratoBank);
      return (VibratoBank) null;
    }
    """
    
    """
    public DvqmDB GetDvqmDBByIndex(ulong index)
    {
      IntPtr pDvqmDB = DatabaseManager.VDM_DatabaseManager_dvqmDBByIndex(this._cppObjPtr, (UIntPtr) index);
      if (!(pDvqmDB == IntPtr.Zero))
        return new DvqmDB(pDvqmDB);
      return (DvqmDB) null;
    }
    """
    
    """
    public DvqmDB GetDvqmDBByID(int id)
    {
      IntPtr pDvqmDB = DatabaseManager.VDM_DatabaseManager_dvqmDBByID(this._cppObjPtr, id);
      if (!(pDvqmDB == IntPtr.Zero))
        return new DvqmDB(pDvqmDB);
      return (DvqmDB) null;
    }
    """
    
    """
    public XSynthGroup GetXSynthGroup(ulong index)
    {
      IntPtr pXSynthGroup = DatabaseManager.VDM_DatabaseManager_xsynthGroup(this._cppObjPtr, (UIntPtr) index);
      if (!(pXSynthGroup == IntPtr.Zero))
        return new XSynthGroup(pXSynthGroup);
      return (XSynthGroup) null;
    }
    """
    
    def GetSingerName(self, compID):
        if(compID == None or compID == ""):
            return ""
        temp = self.GetVoiceBankByCompID(compID)
        if(temp == None):
            return ""
        elif(temp.name == None):
            return ""
        else:
            return temp.name
    
    """
    public List<DvqmDB> GetDvqmDBList(string vbCompID)
    {
      List<DvqmDB> dvqmDbList = new List<DvqmDB>();
      for (ulong index1 = 0; index1 < this.NumDvqmDBs; ++index1)
      {
        DvqmDB dvqmDbByIndex = this.GetDvqmDBByIndex(index1);
        if (dvqmDbByIndex != null)
        {
          ulong numVoiceBankIds = dvqmDbByIndex.NumVoiceBankIDs;
          if (numVoiceBankIds == 0UL)
          {
            dvqmDbList.Add(dvqmDbByIndex);
          }
          else
          {
            for (ulong index2 = 0; index2 < numVoiceBankIds; ++index2)
            {
              string voiceBankId = dvqmDbByIndex.GetVoiceBankID(index2);
              if (vbCompID.CompareTo(voiceBankId) == 0)
                dvqmDbList.Add(dvqmDbByIndex);
            }
          }
        }
      }
      return dvqmDbList;
    }
    """

    """
    def GetAvailableBSList(self):
        intList = list()
        for(index in range(0, self.NumVoiceBanks)):
            VoiceBank voiceBankByIndex = this.GetVoiceBankByIndex(index);
            if (voiceBankByIndex == null)
                return (List<int>) null;
            if (!intList.Contains(voiceBankByIndex.LangID))
                intList.Add(voiceBankByIndex.LangID);
        }
        return intList;
    }
    """

    def GetAvailableCompID(self, compID, bs):
        if(compID == None or compID == ""):
            return ""
        temp = self.GetAvailableVoiceBank(compID, bs)
        if(temp == None):
            return ""
        elif(temp.CompID == None):
            return ""
        else:
            return temp.CompID
    
    """
    public List<DvqmProperty> GetAvailableDvqmPropertyList(string compID, bool isAttack)
    {
      if (string.IsNullOrEmpty(compID))
        return (List<DvqmProperty>) null;
      List<DvqmProperty> dvqmPropertyList = new List<DvqmProperty>();
      for (ulong index1 = 0; index1 < this.NumDvqmDBs; ++index1)
      {
        DvqmDB dvqmDbByIndex = this.GetDvqmDBByIndex(index1);
        if (dvqmDbByIndex != null)
        {
          ulong numVoiceBankIds = dvqmDbByIndex.NumVoiceBankIDs;
          if (numVoiceBankIds == 0UL)
          {
            for (ulong index2 = 0; index2 < dvqmDbByIndex.NumDvqmProperties(isAttack); ++index2)
            {
              DvqmProperty dvqmPropertyByIndex = dvqmDbByIndex.GetDvqmPropertyByIndex(isAttack, index2);
              if (dvqmPropertyByIndex != null)
                dvqmPropertyList.Add(dvqmPropertyByIndex);
            }
          }
          else
          {
            for (ulong index2 = 0; index2 < numVoiceBankIds; ++index2)
            {
              string voiceBankId = dvqmDbByIndex.GetVoiceBankID(index2);
              if (compID.CompareTo(voiceBankId) == 0)
              {
                for (ulong index3 = 0; index3 < dvqmDbByIndex.NumDvqmProperties(isAttack); ++index3)
                {
                  DvqmProperty dvqmPropertyByIndex = dvqmDbByIndex.GetDvqmPropertyByIndex(isAttack, index3);
                  if (dvqmPropertyByIndex != null)
                    dvqmPropertyList.Add(dvqmPropertyByIndex);
                }
              }
            }
          }
        }
      }
      if (dvqmPropertyList.Count != 0)
        return dvqmPropertyList;
      return (List<DvqmProperty>) null;
    }
    """
    
    """
    public XSynthGroup GetAvailableXSynthGroup(VoiceBank voiceBank)
    {
      string compId = voiceBank?.CompID;
      if (string.IsNullOrEmpty(voiceBank.CompID))
        return (XSynthGroup) null;
      List<XSynthGroup> allXsynthGroupList = this.GetAllXSynthGroupList();
      if (allXsynthGroupList == null)
        return (XSynthGroup) null;
      foreach (XSynthGroup xsynthGroup in allXsynthGroupList)
      {
        if (xsynthGroup == null)
          return (XSynthGroup) null;
        if (xsynthGroup.HasCompID(compId))
          return xsynthGroup;
      }
      return (XSynthGroup) null;
    }
    """
    
    """
    private List<XSynthGroup> GetAllXSynthGroupList()
    {
      List<XSynthGroup> xsynthGroupList = new List<XSynthGroup>();
      for (ulong index = 0; index < this.NumXSynthGroups; ++index)
      {
        XSynthGroup xsynthGroup = this.GetXSynthGroup(index);
        if (xsynthGroup == null)
          return (List<XSynthGroup>) null;
        xsynthGroupList.Add(xsynthGroup);
      }
      return xsynthGroupList;
    }
    """
    
    """
    private VoiceBank GetAvailableVoiceBank(string compID, int bs)
    {
      if (string.IsNullOrEmpty(compID))
        return (VoiceBank) null;
      return this.GetVoiceBankByCompID(compID) ?? this.GetVoiceBankByBSPC(bs, 0) ?? this.DefaultVoiceBank ?? (VoiceBank) null;
    }
    """
    
if __name__ == '__main__':
    path = input(path)
    load_vdm_path()
