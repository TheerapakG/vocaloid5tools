# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type


using System;
using System.Collections.Generic;
using System.Runtime.InteropServices;

namespace Yamaha.VOCALOID.VSM
{
  public class WIVSMClipboard
  {
    protected IntPtr _cppObjPtr = IntPtr.Zero;

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMClipboard_destroy(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern VSMResult VIS_VSM_WIVSMClipboard_lastError(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern UIntPtr VIS_VSM_WIVSMClipboard_numTimeSig(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMClipboard_timeSig(IntPtr cppobjptr, UIntPtr size_t_index);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMClipboard_pushTimeSig(IntPtr cppobjptr, IntPtr timeSig);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern void VIS_VSM_WIVSMClipboard_clearTimeSig(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern UIntPtr VIS_VSM_WIVSMClipboard_numTempo(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMClipboard_tempo(IntPtr cppobjptr, UIntPtr size_t_index);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMClipboard_pushTempo(IntPtr cppobjptr, IntPtr tempo);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern void VIS_VSM_WIVSMClipboard_clearTempo(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern UIntPtr VIS_VSM_WIVSMClipboard_numMasterVolume(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMClipboard_masterVolume(IntPtr cppobjptr, UIntPtr size_t_index);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMClipboard_pushMasterVolume(IntPtr cppobjptr, IntPtr mastrervolume);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern void VIS_VSM_WIVSMClipboard_clearMasterVolume(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern UIntPtr VIS_VSM_WIVSMClipboard_numTrack(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMClipboard_track(IntPtr cppobjptr, UIntPtr size_t_index);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMClipboard_pushTrack(IntPtr cppobjptr, IntPtr track);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern void VIS_VSM_WIVSMClipboard_clearTrack(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern UIntPtr VIS_VSM_WIVSMClipboard_numTrackVolume(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMClipboard_trackVolume(IntPtr cppobjptr, UIntPtr size_t_index);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMClipboard_pushTrackVolume(IntPtr cppobjptr, IntPtr trackVolume);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern void VIS_VSM_WIVSMClipboard_clearTrackVolume(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern UIntPtr VIS_VSM_WIVSMClipboard_numPanpot(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMClipboard_panpot(IntPtr cppobjptr, UIntPtr size_t_index);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMClipboard_pushPanpot(IntPtr cppobjptr, IntPtr panpot);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern void VIS_VSM_WIVSMClipboard_clearPanpot(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern UIntPtr VIS_VSM_WIVSMClipboard_numMidiPart(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMClipboard_midiPart(IntPtr cppobjptr, UIntPtr size_t_index);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMClipboard_pushMidiPart(IntPtr cppobjptr, IntPtr midiPart);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern void VIS_VSM_WIVSMClipboard_clearMidiPart(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern UIntPtr VIS_VSM_WIVSMClipboard_numAudioPart(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMClipboard_audioPart(IntPtr cppobjptr, UIntPtr size_t_index);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMClipboard_pushAudioPart(IntPtr cppobjptr, IntPtr audioPart);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern void VIS_VSM_WIVSMClipboard_clearAudioPart(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern UIntPtr VIS_VSM_WIVSMClipboard_numMidiPartController(IntPtr cppobjptr, VSMControllerType type);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMClipboard_midiPartController(IntPtr cppobjptr, VSMControllerType type, UIntPtr size_t_index);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMClipboard_pushMidiPartController(IntPtr cppobjptr, VSMControllerType type, IntPtr midiController);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern void VIS_VSM_WIVSMClipboard_clearMidiPartController(IntPtr cppobjptr, VSMControllerType type);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern UIntPtr VIS_VSM_WIVSMClipboard_numNote(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMClipboard_note(IntPtr cppobjptr, UIntPtr size_t_index);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMClipboard_pushNote(IntPtr cppobjptr, IntPtr note);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern void VIS_VSM_WIVSMClipboard_clearNote(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern UIntPtr VIS_VSM_WIVSMClipboard_numVibratoEvents(IntPtr cppobjptr, VSMVibratoEventType type);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMClipboard_vibratoEvent(IntPtr cppobjptr, VSMVibratoEventType type, UIntPtr size_t_index);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMClipboard_pushVibratoEvent(IntPtr cppobjptr, VSMVibratoEventType type, IntPtr vibratoEvent);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern void VIS_VSM_WIVSMClipboard_clearVibratoEvent(IntPtr cppobjptr, VSMVibratoEventType type);

    public override bool Equals(object obj)
    {
      if (obj == null)
        return false;
      WIVSMClipboard wivsmClipboard = obj as WIVSMClipboard;
      if (wivsmClipboard == null)
        return false;
      return this._cppObjPtr == wivsmClipboard._cppObjPtr;
    }

    public override int GetHashCode()
    {
      return (int) this._cppObjPtr.ToInt64();
    }

    internal WIVSMClipboard(IntPtr pClipboard)
    {
      if (pClipboard == IntPtr.Zero)
        throw new ArgumentException("アンマネージオブジェクトではない");
      this._cppObjPtr = pClipboard;
    }

    public VSMResult LastError
    {
      get
      {
        return WIVSMClipboard.VIS_VSM_WIVSMClipboard_lastError(this._cppObjPtr);
      }
    }

    public ulong NumTimeSig
    {
      get
      {
        UIntPtr num = WIVSMClipboard.VIS_VSM_WIVSMClipboard_numTimeSig(this._cppObjPtr);
        if (UIntPtr.Size != 4)
          return num.ToUInt64();
        return (ulong) num.ToUInt32();
      }
    }

    public ulong NumTempo
    {
      get
      {
        UIntPtr num = WIVSMClipboard.VIS_VSM_WIVSMClipboard_numTempo(this._cppObjPtr);
        if (UIntPtr.Size != 4)
          return num.ToUInt64();
        return (ulong) num.ToUInt32();
      }
    }

    public ulong NumMasterVolume
    {
      get
      {
        UIntPtr num = WIVSMClipboard.VIS_VSM_WIVSMClipboard_numMasterVolume(this._cppObjPtr);
        if (UIntPtr.Size != 4)
          return num.ToUInt64();
        return (ulong) num.ToUInt32();
      }
    }

    public ulong NumTrack
    {
      get
      {
        UIntPtr num = WIVSMClipboard.VIS_VSM_WIVSMClipboard_numTrack(this._cppObjPtr);
        if (UIntPtr.Size != 4)
          return num.ToUInt64();
        return (ulong) num.ToUInt32();
      }
    }

    public ulong NumTrackVolume
    {
      get
      {
        UIntPtr num = WIVSMClipboard.VIS_VSM_WIVSMClipboard_numTrackVolume(this._cppObjPtr);
        if (UIntPtr.Size != 4)
          return num.ToUInt64();
        return (ulong) num.ToUInt32();
      }
    }

    public ulong NumPanpot
    {
      get
      {
        UIntPtr num = WIVSMClipboard.VIS_VSM_WIVSMClipboard_numPanpot(this._cppObjPtr);
        if (UIntPtr.Size != 4)
          return num.ToUInt64();
        return (ulong) num.ToUInt32();
      }
    }

    public ulong NumMidiPart
    {
      get
      {
        UIntPtr num = WIVSMClipboard.VIS_VSM_WIVSMClipboard_numMidiPart(this._cppObjPtr);
        if (UIntPtr.Size != 4)
          return num.ToUInt64();
        return (ulong) num.ToUInt32();
      }
    }

    public ulong NumAudioPart
    {
      get
      {
        UIntPtr num = WIVSMClipboard.VIS_VSM_WIVSMClipboard_numAudioPart(this._cppObjPtr);
        if (UIntPtr.Size != 4)
          return num.ToUInt64();
        return (ulong) num.ToUInt32();
      }
    }

    public ulong NumNote
    {
      get
      {
        UIntPtr num = WIVSMClipboard.VIS_VSM_WIVSMClipboard_numNote(this._cppObjPtr);
        if (UIntPtr.Size != 4)
          return num.ToUInt64();
        return (ulong) num.ToUInt32();
      }
    }

    public bool Destroy()
    {
      int num = WIVSMClipboard.VIS_VSM_WIVSMClipboard_destroy(this._cppObjPtr) ? 1 : 0;
      if (num == 0)
        return num != 0;
      this._cppObjPtr = IntPtr.Zero;
      return num != 0;
    }

    public WIVSMTimeSig GetTimeSig(ulong index)
    {
      IntPtr pIVSMTimeSig = WIVSMClipboard.VIS_VSM_WIVSMClipboard_timeSig(this._cppObjPtr, (UIntPtr) index);
      if (!(pIVSMTimeSig == IntPtr.Zero))
        return new WIVSMTimeSig(pIVSMTimeSig);
      return (WIVSMTimeSig) null;
    }

    public WIVSMTimeSig PushTimeSig(WIVSMTimeSig timeSig)
    {
      if (timeSig == null)
        return (WIVSMTimeSig) null;
      IntPtr pIVSMTimeSig = WIVSMClipboard.VIS_VSM_WIVSMClipboard_pushTimeSig(this._cppObjPtr, (IntPtr) timeSig);
      if (!(pIVSMTimeSig == IntPtr.Zero))
        return new WIVSMTimeSig(pIVSMTimeSig);
      return (WIVSMTimeSig) null;
    }

    public void ClearTimeSig()
    {
      WIVSMClipboard.VIS_VSM_WIVSMClipboard_clearTimeSig(this._cppObjPtr);
    }

    public WIVSMTempo GetTempo(ulong index)
    {
      IntPtr pTempo = WIVSMClipboard.VIS_VSM_WIVSMClipboard_tempo(this._cppObjPtr, (UIntPtr) index);
      if (!(pTempo == IntPtr.Zero))
        return new WIVSMTempo(pTempo);
      return (WIVSMTempo) null;
    }

    public WIVSMTempo PushTempo(WIVSMTempo tempo)
    {
      if (tempo == null)
        return (WIVSMTempo) null;
      IntPtr pTempo = WIVSMClipboard.VIS_VSM_WIVSMClipboard_pushTempo(this._cppObjPtr, (IntPtr) tempo);
      if (!(pTempo == IntPtr.Zero))
        return new WIVSMTempo(pTempo);
      return (WIVSMTempo) null;
    }

    public void ClearTempo()
    {
      WIVSMClipboard.VIS_VSM_WIVSMClipboard_clearTempo(this._cppObjPtr);
    }

    public WIVSMMasterVolume GetMasterVolume(ulong index)
    {
      IntPtr pMasterVolume = WIVSMClipboard.VIS_VSM_WIVSMClipboard_masterVolume(this._cppObjPtr, (UIntPtr) index);
      if (!(pMasterVolume == IntPtr.Zero))
        return new WIVSMMasterVolume(pMasterVolume);
      return (WIVSMMasterVolume) null;
    }

    public WIVSMMasterVolume PushMasterVolume(WIVSMMasterVolume masterVolume)
    {
      if (masterVolume == null)
        return (WIVSMMasterVolume) null;
      IntPtr pMasterVolume = WIVSMClipboard.VIS_VSM_WIVSMClipboard_pushMasterVolume(this._cppObjPtr, (IntPtr) masterVolume);
      if (!(pMasterVolume == IntPtr.Zero))
        return new WIVSMMasterVolume(pMasterVolume);
      return (WIVSMMasterVolume) null;
    }

    public void ClearMasterVolume()
    {
      WIVSMClipboard.VIS_VSM_WIVSMClipboard_clearMasterVolume(this._cppObjPtr);
    }

    public WIVSMTrack GetTrack(ulong index)
    {
      IntPtr pTrack = WIVSMClipboard.VIS_VSM_WIVSMClipboard_track(this._cppObjPtr, (UIntPtr) index);
      if (!(pTrack == IntPtr.Zero))
        return new WIVSMTrack(pTrack);
      return (WIVSMTrack) null;
    }

    public WIVSMTrack PushTrack(WIVSMTrack track)
    {
      if (track == null)
        return (WIVSMTrack) null;
      IntPtr pTrack = WIVSMClipboard.VIS_VSM_WIVSMClipboard_pushTrack(this._cppObjPtr, (IntPtr) track);
      if (!(pTrack == IntPtr.Zero))
        return new WIVSMTrack(pTrack);
      return (WIVSMTrack) null;
    }

    public void ClearTrack()
    {
      WIVSMClipboard.VIS_VSM_WIVSMClipboard_clearTrack(this._cppObjPtr);
    }

    public WIVSMTrackVolume GetTrackVolume(ulong index)
    {
      IntPtr pTrackVolume = WIVSMClipboard.VIS_VSM_WIVSMClipboard_trackVolume(this._cppObjPtr, (UIntPtr) index);
      if (!(pTrackVolume == IntPtr.Zero))
        return new WIVSMTrackVolume(pTrackVolume);
      return (WIVSMTrackVolume) null;
    }

    public WIVSMTrackVolume PushTrackVolume(WIVSMTrackVolume trackVolume)
    {
      if (trackVolume == null)
        return (WIVSMTrackVolume) null;
      IntPtr pTrackVolume = WIVSMClipboard.VIS_VSM_WIVSMClipboard_pushTrackVolume(this._cppObjPtr, (IntPtr) trackVolume);
      if (!(pTrackVolume == IntPtr.Zero))
        return new WIVSMTrackVolume(pTrackVolume);
      return (WIVSMTrackVolume) null;
    }

    public void ClearTrackVolume()
    {
      WIVSMClipboard.VIS_VSM_WIVSMClipboard_clearTrackVolume(this._cppObjPtr);
    }

    public WIVSMPanpot GetPanpot(ulong index)
    {
      IntPtr pPanpot = WIVSMClipboard.VIS_VSM_WIVSMClipboard_panpot(this._cppObjPtr, (UIntPtr) index);
      if (!(pPanpot == IntPtr.Zero))
        return new WIVSMPanpot(pPanpot);
      return (WIVSMPanpot) null;
    }

    public WIVSMPanpot PushPanpot(WIVSMPanpot panpot)
    {
      if (panpot == null)
        return (WIVSMPanpot) null;
      IntPtr pPanpot = WIVSMClipboard.VIS_VSM_WIVSMClipboard_pushPanpot(this._cppObjPtr, (IntPtr) panpot);
      if (!(pPanpot == IntPtr.Zero))
        return new WIVSMPanpot(pPanpot);
      return (WIVSMPanpot) null;
    }

    public void ClearPanpot()
    {
      WIVSMClipboard.VIS_VSM_WIVSMClipboard_clearPanpot(this._cppObjPtr);
    }

    public WIVSMMidiPart GetMidiPart(ulong index)
    {
      IntPtr pPart = WIVSMClipboard.VIS_VSM_WIVSMClipboard_midiPart(this._cppObjPtr, (UIntPtr) index);
      if (!(pPart == IntPtr.Zero))
        return new WIVSMMidiPart(pPart);
      return (WIVSMMidiPart) null;
    }

    public WIVSMMidiPart PushMidiPart(WIVSMMidiPart midiPart)
    {
      if (midiPart == null)
        return (WIVSMMidiPart) null;
      IntPtr pPart = WIVSMClipboard.VIS_VSM_WIVSMClipboard_pushMidiPart(this._cppObjPtr, (IntPtr) midiPart);
      if (!(pPart == IntPtr.Zero))
        return new WIVSMMidiPart(pPart);
      return (WIVSMMidiPart) null;
    }

    public void ClearMidiPart()
    {
      WIVSMClipboard.VIS_VSM_WIVSMClipboard_clearMidiPart(this._cppObjPtr);
    }

    public WIVSMAudioPart GetAudioPart(ulong index)
    {
      IntPtr pPart = WIVSMClipboard.VIS_VSM_WIVSMClipboard_audioPart(this._cppObjPtr, (UIntPtr) index);
      if (!(pPart == IntPtr.Zero))
        return new WIVSMAudioPart(pPart);
      return (WIVSMAudioPart) null;
    }

    public WIVSMAudioPart PushAudioPart(WIVSMAudioPart audioPart)
    {
      if (audioPart == null)
        return (WIVSMAudioPart) null;
      IntPtr pPart = WIVSMClipboard.VIS_VSM_WIVSMClipboard_pushAudioPart(this._cppObjPtr, (IntPtr) audioPart);
      if (!(pPart == IntPtr.Zero))
        return new WIVSMAudioPart(pPart);
      return (WIVSMAudioPart) null;
    }

    public void ClearAudioPart()
    {
      WIVSMClipboard.VIS_VSM_WIVSMClipboard_clearAudioPart(this._cppObjPtr);
    }

    public ulong GetNumMidiPartController(VSMControllerType type)
    {
      UIntPtr num = WIVSMClipboard.VIS_VSM_WIVSMClipboard_numMidiPartController(this._cppObjPtr, type);
      if (UIntPtr.Size != 4)
        return num.ToUInt64();
      return (ulong) num.ToUInt32();
    }

    public WIVSMMidiController GetMidiPartController(VSMControllerType type, ulong index)
    {
      IntPtr pMidiController = WIVSMClipboard.VIS_VSM_WIVSMClipboard_midiPartController(this._cppObjPtr, type, (UIntPtr) index);
      if (!(pMidiController == IntPtr.Zero))
        return new WIVSMMidiController(pMidiController);
      return (WIVSMMidiController) null;
    }

    public WIVSMMidiController PushMidiPartController(VSMControllerType type, WIVSMMidiController midiController)
    {
      if (midiController == null)
        return (WIVSMMidiController) null;
      IntPtr pMidiController = WIVSMClipboard.VIS_VSM_WIVSMClipboard_pushMidiPartController(this._cppObjPtr, type, (IntPtr) midiController);
      if (!(pMidiController == IntPtr.Zero))
        return new WIVSMMidiController(pMidiController);
      return (WIVSMMidiController) null;
    }

    public void ClearMidiPartController(VSMControllerType type)
    {
      WIVSMClipboard.VIS_VSM_WIVSMClipboard_clearMidiPartController(this._cppObjPtr, type);
    }

    public WIVSMNote GetNote(ulong index)
    {
      IntPtr pNote = WIVSMClipboard.VIS_VSM_WIVSMClipboard_note(this._cppObjPtr, (UIntPtr) index);
      if (!(pNote == IntPtr.Zero))
        return new WIVSMNote(pNote);
      return (WIVSMNote) null;
    }

    public WIVSMNote PushNote(WIVSMNote note)
    {
      if (note == null)
        return (WIVSMNote) null;
      IntPtr pNote = WIVSMClipboard.VIS_VSM_WIVSMClipboard_pushNote(this._cppObjPtr, (IntPtr) note);
      if (!(pNote == IntPtr.Zero))
        return new WIVSMNote(pNote);
      return (WIVSMNote) null;
    }

    public void ClearNote()
    {
      WIVSMClipboard.VIS_VSM_WIVSMClipboard_clearNote(this._cppObjPtr);
    }

    public ulong GetNumVibratoEvents(VSMVibratoEventType type)
    {
      UIntPtr num = WIVSMClipboard.VIS_VSM_WIVSMClipboard_numVibratoEvents(this._cppObjPtr, type);
      if (UIntPtr.Size != 4)
        return num.ToUInt64();
      return (ulong) num.ToUInt32();
    }

    public WIVSMVibratoEvent GetVibratoEvent(VSMVibratoEventType type, ulong index)
    {
      IntPtr pVibratoEvent = WIVSMClipboard.VIS_VSM_WIVSMClipboard_vibratoEvent(this._cppObjPtr, type, (UIntPtr) index);
      if (!(pVibratoEvent == IntPtr.Zero))
        return new WIVSMVibratoEvent(pVibratoEvent);
      return (WIVSMVibratoEvent) null;
    }

    public WIVSMVibratoEvent PushVibratoEvent(VSMVibratoEventType type, WIVSMVibratoEvent vibratoEvent)
    {
      if (vibratoEvent == null)
        return (WIVSMVibratoEvent) null;
      IntPtr pVibratoEvent = WIVSMClipboard.VIS_VSM_WIVSMClipboard_pushVibratoEvent(this._cppObjPtr, type, (IntPtr) vibratoEvent);
      if (!(pVibratoEvent == IntPtr.Zero))
        return new WIVSMVibratoEvent(pVibratoEvent);
      return (WIVSMVibratoEvent) null;
    }

    public void ClearVibratoEvent(VSMVibratoEventType type)
    {
      WIVSMClipboard.VIS_VSM_WIVSMClipboard_clearVibratoEvent(this._cppObjPtr, type);
    }

    public void ClearAll()
    {
      this.ClearMasterVolume();
      this.ClearMidiPart();
      foreach (VSMControllerType type in Enum.GetValues(typeof (VSMControllerType)))
        this.ClearMidiPartController(type);
      this.ClearNote();
      this.ClearPanpot();
      this.ClearTempo();
      this.ClearTimeSig();
      this.ClearTrack();
      this.ClearTrackVolume();
      foreach (VSMVibratoEventType type in Enum.GetValues(typeof (VSMVibratoEventType)))
        this.ClearVibratoEvent(type);
      this.ClearAudioPart();
    }

    public bool PushTimeSigs(IEnumerable<WIVSMTimeSig> timesigs)
    {
      foreach (WIVSMTimeSig timesig in timesigs)
      {
        if (this.PushTimeSig(timesig) == null)
          return false;
      }
      return true;
    }

    public int GetFirstPositionPushedTimeSigs(WIVSMSequence seq)
    {
      int val1 = int.MaxValue;
      for (ulong index = 0; index < this.NumTimeSig; ++index)
        val1 = Math.Min(val1, seq.GetTickFromBar(this.GetTimeSig(index).PosBar).Tick);
      return val1;
    }

    public bool PushTempos(IEnumerable<WIVSMTempo> tempos)
    {
      foreach (WIVSMTempo tempo in tempos)
      {
        if (this.PushTempo(tempo) == null)
          return false;
      }
      return true;
    }

    public int GetFirstPositionPushedTempos()
    {
      int val1 = int.MaxValue;
      for (ulong index = 0; index < this.NumTempo; ++index)
        val1 = Math.Min(val1, this.GetTempo(index).AbsPosition.Tick);
      return val1;
    }

    public bool PushMasterVolumes(IEnumerable<WIVSMMasterVolume> volumes)
    {
      foreach (WIVSMMasterVolume volume in volumes)
      {
        if (this.PushMasterVolume(volume) == null)
          return false;
      }
      return true;
    }

    public int GetFirstPositionPushedMasterVolumes()
    {
      int val1 = int.MaxValue;
      for (ulong index = 0; index < this.NumMasterVolume; ++index)
        val1 = Math.Min(val1, this.GetMasterVolume(index).AbsPosition.Tick);
      return val1;
    }

    public bool PushTracks(IEnumerable<WIVSMTrack> tracks)
    {
      foreach (WIVSMTrack track in tracks)
      {
        if (this.PushTrack(track) == null)
          return false;
      }
      return true;
    }

    public bool PushParts(IEnumerable<WIVSMPart> parts)
    {
      foreach (WIVSMPart part in parts)
      {
        if (part == null)
          return false;
        if (part.Type == VSMPartType.Midi)
        {
          if (this.PushMidiPart(new WIVSMMidiPart(part)) == null)
            return false;
        }
        else if (part.Type == VSMPartType.Audio && this.PushAudioPart(new WIVSMAudioPart(part)) == null)
          return false;
      }
      return true;
    }

    public int GetFirstPositionPushedParts()
    {
      int val1 = int.MaxValue;
      for (ulong index = 0; index < this.NumMidiPart; ++index)
        val1 = Math.Min(val1, this.GetMidiPart(index).AbsPosition.Tick);
      for (ulong index = 0; index < this.NumAudioPart; ++index)
        val1 = Math.Min(val1, this.GetAudioPart(index).AbsPosition.Tick);
      return val1;
    }

    public bool PushTrackVolumes(IEnumerable<WIVSMTrackVolume> volumes)
    {
      foreach (WIVSMTrackVolume volume in volumes)
      {
        if (this.PushTrackVolume(volume) == null)
          return false;
      }
      return true;
    }

    public int GetFirstPositionPushedTrackVolumes()
    {
      int val1 = int.MaxValue;
      for (ulong index = 0; index < this.NumTrackVolume; ++index)
        val1 = Math.Min(val1, this.GetTrackVolume(index).AbsPosition.Tick);
      return val1;
    }

    public bool PushPanpots(IEnumerable<WIVSMPanpot> panpots)
    {
      foreach (WIVSMPanpot panpot in panpots)
      {
        if (this.PushPanpot(panpot) == null)
          return false;
      }
      return true;
    }

    public int GetFirstPositionPushedPanpots()
    {
      int val1 = int.MaxValue;
      for (ulong index = 0; index < this.NumPanpot; ++index)
        val1 = Math.Min(val1, this.GetPanpot(index).AbsPosition.Tick);
      return val1;
    }

    public bool HasCopyMidiController()
    {
      foreach (VSMControllerType type in Enum.GetValues(typeof (VSMControllerType)))
      {
        switch (type)
        {
          case VSMControllerType.DynamicsHmm:
          case VSMControllerType.PitchBendHmm:
          case VSMControllerType.WeightHmm:
            continue;
          default:
            if (0UL < this.GetNumMidiPartController(type))
              return true;
            continue;
        }
      }
      return false;
    }

    public bool HasCopiedOneTrackObjects()
    {
      WIVSMTrack wivsmTrack = (WIVSMTrack) null;
      for (ulong index = 0; index < this.NumMidiPart; ++index)
      {
        WIVSMMidiPart midiPart = this.GetMidiPart(index);
        if (wivsmTrack == null)
          wivsmTrack = (WIVSMTrack) midiPart.Parent;
        else if (!wivsmTrack.Equals((object) midiPart.Parent))
          return false;
      }
      for (ulong index = 0; index < this.NumAudioPart; ++index)
      {
        WIVSMAudioPart audioPart = this.GetAudioPart(index);
        if (wivsmTrack == null)
          wivsmTrack = (WIVSMTrack) audioPart.Parent;
        else if (!wivsmTrack.Equals((object) audioPart.Parent))
          return false;
      }
      for (ulong index = 0; index < this.NumTrackVolume; ++index)
      {
        WIVSMTrackVolume trackVolume = this.GetTrackVolume(index);
        if (wivsmTrack == null)
          wivsmTrack = trackVolume.Parent;
        else if (!wivsmTrack.Equals((object) trackVolume.Parent))
          return false;
      }
      for (ulong index = 0; index < this.NumPanpot; ++index)
      {
        WIVSMPanpot panpot = this.GetPanpot(index);
        if (wivsmTrack == null)
          wivsmTrack = panpot.Parent;
        else if (!wivsmTrack.Equals((object) panpot.Parent))
          return false;
      }
      return wivsmTrack != null;
    }
  }
}
