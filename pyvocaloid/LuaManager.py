# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type

import ctypes
import csharptypes

class LuaManager:
"""
    private static readonly List<string> _robotVoiceGuid = new List<string>()
    {
      "ROBOTHAD-D8E4-44b8-939B-41CD101E08FD",
      "ROBOTNML-D8E4-44b8-939B-41CD101E08FD",
      "ROBOTSFT-D8E4-44b8-939B-41CD101E08FD"
    };
"""
    _singingSkillList = list()
"""
    private List<string> _robotVoiceLuaPathList = new List<string>();
    private const string _jsonStr = ".json";
    private const string _luaStr = ".lua";
    private const string _defaultSingingSkillGuid = "75F04D2B-D8E4-44b8-939B-41CD101E08FD";

    public string DefaultSingingSkillGuid
    {
      get
      {
        return "75F04D2B-D8E4-44b8-939B-41CD101E08FD";
      }
    }
"""
    def __init__(self):
        if (!self.readSingingSkillFiles()):
            raise csharptypes.ApplicationException("failed to read singing skill files")
        if (!self.InitializeForRobotVoice()):
            raise csharptypes.ApplicationException("ロボットボイスのための初期化に失敗した")
    }
"""
    public bool HasDefaultSingingSkillFiles()
    {
      try
      {
        return File.Exists(Path.Combine(FolderLocation.PathSystemMESingingSkill, "75F04D2B-D8E4-44b8-939B-41CD101E08FD.lua")) && File.Exists(Path.Combine(FolderLocation.PathSystemMESingingSkill, "75F04D2B-D8E4-44b8-939B-41CD101E08FD.json"));
      }
      catch
      {
        return false;
      }
    }

    public List<string> GetGenreTags()
    {
      List<string> stringList = new List<string>();
      if (this._singingSkillList == null)
        return (List<string>) null;
      for (int index1 = 0; index1 < this._singingSkillList.Count; ++index1)
      {
        List<string> genreTags = this._singingSkillList[index1].GenreTags;
        if (genreTags == null)
          return (List<string>) null;
        for (int index2 = 0; index2 < genreTags.Count; ++index2)
        {
          string str1 = genreTags[index2];
          if (string.IsNullOrEmpty(str1))
            return (List<string>) null;
          bool flag = false;
          foreach (string str2 in stringList)
          {
            if (string.IsNullOrEmpty(str2))
              return (List<string>) null;
            if (str1 == str2)
            {
              flag = true;
              break;
            }
          }
          if (!flag)
            stringList.Add(str1);
        }
      }
      return stringList;
    }

    public List<string> GetSingingSkillNames()
    {
      List<string> stringList = new List<string>();
      if (this._singingSkillList == null)
        return (List<string>) null;
      for (int index = 0; index < this._singingSkillList.Count; ++index)
      {
        string name = this._singingSkillList[index].Name;
        if (string.IsNullOrEmpty(name))
          return (List<string>) null;
        bool flag = false;
        foreach (string str in stringList)
        {
          if (string.IsNullOrEmpty(str))
            return (List<string>) null;
          if (name == str)
          {
            flag = true;
            break;
          }
        }
        if (!flag)
          stringList.Add(name);
      }
      return stringList;
    }

    public bool HasSelectedGanreTag(string singingSkillName, string selectedGenreTag, out bool hasSelectedGenreTag)
    {
      hasSelectedGenreTag = false;
      if (string.IsNullOrEmpty(singingSkillName) || string.IsNullOrEmpty(selectedGenreTag))
        return false;
      foreach (SingingSkill singingSkill in this._singingSkillList)
      {
        if (singingSkill == null || string.IsNullOrEmpty(singingSkill.Name))
          return false;
        if (singingSkillName == singingSkill.Name)
        {
          if (singingSkill.GenreTags == null)
            return false;
          foreach (string genreTag in singingSkill.GenreTags)
          {
            if (string.IsNullOrEmpty(genreTag))
              return false;
            if (selectedGenreTag == genreTag)
            {
              hasSelectedGenreTag = true;
              return true;
            }
          }
        }
      }
      return true;
    }

    public string GetSingingSkillNameByGuid(string guid)
    {
      if (string.IsNullOrEmpty(guid))
        return (string) null;
      foreach (SingingSkill singingSkill in this._singingSkillList)
      {
        if (singingSkill == null || string.IsNullOrEmpty(singingSkill.ID))
          return (string) null;
        if (guid == singingSkill.ID)
        {
          if (string.IsNullOrEmpty(singingSkill.Name))
            return (string) null;
          return singingSkill.Name;
        }
      }
      return (string) null;
    }

    public string GetGuidBySingingSkillName(string name)
    {
      if (string.IsNullOrEmpty(name))
        return (string) null;
      foreach (SingingSkill singingSkill in this._singingSkillList)
      {
        if (singingSkill == null || string.IsNullOrEmpty(singingSkill.Name))
          return (string) null;
        if (name == singingSkill.Name)
        {
          if (string.IsNullOrEmpty(singingSkill.ID))
            return (string) null;
          return singingSkill.ID;
        }
      }
      return (string) null;
    }

    public bool SetScriptFilePathToMidiEffectSingingSkill(WIVSMMidiEffect midiEffect)
    {
      string singingSkillGuid = this.GetSingingSkillGuid(midiEffect);
      if (string.IsNullOrEmpty(singingSkillGuid))
        return false;
      string path = (string) null;
      foreach (SingingSkill singingSkill in this._singingSkillList)
      {
        if (singingSkillGuid == singingSkill.ID)
        {
          path = singingSkill.LuaFilePath;
          break;
        }
      }
      if (!string.IsNullOrEmpty(path) && !File.Exists(path))
        return false;
      midiEffect.ScriptFilePath = path;
      return true;
    }

    public bool SetTimingToMidiEffectSingingSkill(WIVSMMidiEffect midiEffect)
    {
      string singingSkillGuid = this.GetSingingSkillGuid(midiEffect);
      if (string.IsNullOrEmpty(singingSkillGuid))
        return false;
      foreach (SingingSkill singingSkill in this._singingSkillList)
      {
        if (singingSkillGuid == singingSkill.ID)
        {
          switch (singingSkill.Timing)
          {
            case TimingType.Commit:
              midiEffect.Timing = VSMMidiEffectTiming.BeforeCommitting;
              return true;
            case TimingType.Rendering:
              midiEffect.Timing = VSMMidiEffectTiming.BeforeRendering;
              return true;
            default:
              return false;
          }
        }
      }
      midiEffect.Timing = VSMMidiEffectTiming.Undefined;
      return true;
    }
"""
    def readSingingSkillFiles(self):
        self._singingSkillList.clear()
        jsonFilePaths = self.GetJsonFilePaths()
        if jsonFilePaths == None:
            return false
        for jsonFilePath in jsonFilePaths
            if jsonFilePath != None and jsonFilePath != "":
                singingSkill = self.GetSingingSkill(jsonFilePath)
                if (singingSkill != None)
                    self._singingSkillList.append(singingSkill)
        return true
"""
    public bool HasRobotVoiceLuaFiles()
    {
      if (this._robotVoiceLuaPathList == null)
        return false;
      foreach (string robotVoiceLuaPath in this._robotVoiceLuaPathList)
      {
        if (string.IsNullOrEmpty(robotVoiceLuaPath) || !File.Exists(robotVoiceLuaPath))
          return false;
      }
      return true;
    }

    public string GetRobotVoiceScriptPath(VSMRobotVoiceModeType mode)
    {
      return this._robotVoiceLuaPathList[(int) mode];
    }
"""
    private List<string> GetJsonFilePaths()
    {
      List<string> stringList = new List<string>();
      if (!Directory.Exists(FolderLocation.PathSystemMESingingSkill))
        return (List<string>) null;
      foreach (string file in Directory.GetFiles(FolderLocation.PathSystemMESingingSkill, "*.json", SearchOption.TopDirectoryOnly))
      {
        if (string.IsNullOrEmpty(file))
          return (List<string>) null;
        stringList.Add(file);
      }
      if (Directory.Exists(FolderLocation.PathUserMESingingSkill))
      {
        foreach (string file in Directory.GetFiles(FolderLocation.PathUserMESingingSkill, "*.json", SearchOption.TopDirectoryOnly))
        {
          if (string.IsNullOrEmpty(file))
            return (List<string>) null;
          stringList.Add(file);
        }
      }
      return stringList;
    }

    private SingingSkill GetSingingSkill(string jsonFilePath)
    {
      if (string.IsNullOrEmpty(jsonFilePath))
        return (SingingSkill) null;
      if (!File.Exists(jsonFilePath))
        return (SingingSkill) null;
      string str = File.ReadAllText(jsonFilePath);
      if (string.IsNullOrEmpty(str))
        return (SingingSkill) null;
      JsonParseSingingSkill parseSingingSkill = JsonConvert.DeserializeObject<JsonParseSingingSkill>(str);
      if (parseSingingSkill == null)
        return (SingingSkill) null;
      SingingSkill singingSkill = new SingingSkill();
      if (string.IsNullOrEmpty(parseSingingSkill.Name))
        return (SingingSkill) null;
      singingSkill.Name = parseSingingSkill.Name;
      if (string.IsNullOrEmpty(parseSingingSkill.PluginID))
        return (SingingSkill) null;
      singingSkill.ID = parseSingingSkill.PluginID;
      if (parseSingingSkill.GenreTags == null)
        return (SingingSkill) null;
      singingSkill.GenreTags.AddRange((IEnumerable<string>) parseSingingSkill.GenreTags);
      singingSkill.Timing = parseSingingSkill.Timing != 1 ? TimingType.Rendering : TimingType.Commit;
      singingSkill.LuaFilePath = jsonFilePath.Replace(".json", ".lua");
      return singingSkill;
    }
"""
    private string GetSingingSkillGuid(WIVSMMidiEffect midiEffect)
    {
      if (string.IsNullOrEmpty(midiEffect?.Id))
        return (string) null;
      WIVSMEffectManager parent = midiEffect.Parent;
      if (midiEffect.Id != parent?.GetMidiEffectID(VSMMidiEffectType.SingingSkill))
        return (string) null;
      string nameSingingSkill = midiEffect.GetParameterNameSingingSkill(VSMSingingSkillParameterType.Name);
      if (string.IsNullOrEmpty(nameSingingSkill))
        return (string) null;
      WIVSMEffectValue valueByName = midiEffect.GetValueByName(nameSingingSkill);
      if (valueByName == null)
        return (string) null;
      if (valueByName.Type != VSMEffectValueType.String)
        return (string) null;
      string rawString = valueByName.RawString;
      if (string.IsNullOrEmpty(rawString))
        return (string) null;
      return rawString;
    }
"""
    private bool InitializeForRobotVoice()
    {
      string systemMeRobotVoice = FolderLocation.PathSystemMERobotVoice;
      if (!Directory.Exists(systemMeRobotVoice))
        return false;
      this._robotVoiceLuaPathList.Clear();
      foreach (string path2 in LuaManager._robotVoiceGuid)
      {
        string path = Path.Combine(systemMeRobotVoice, path2) + ".lua";
        if (string.IsNullOrEmpty(path) || !File.Exists(path))
          return false;
        this._robotVoiceLuaPathList.Add(path);
      }
      return true;
    }
  }
