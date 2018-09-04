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
    private static extern VSMResult VIS_VSM_WIVSMSequence_lastError(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_isDirty(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_save(IntPtr cppobjptr, [MarshalAs(UnmanagedType.LPWStr), In] string path, [MarshalAs(UnmanagedType.U1)] bool prettify);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_close(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMSequence_title(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern void VIS_VSM_WIVSMSequence_setTitle(IntPtr cppobjptr, [MarshalAs(UnmanagedType.LPWStr), In] string title);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern int VIS_VSM_WIVSMSequence_tickFromBar(IntPtr cppobjptr, int bar);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern void VIS_VSM_WIVSMSequence_timeFromTick(IntPtr cppobjptr, int absPosition, out VSMSequenceTime seqTime);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern double VIS_VSM_WIVSMSequence_msecFromTick(IntPtr cppobjptr, int absPositionStart, int absPositionEnd);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern int VIS_VSM_WIVSMSequence_tickFromMsec(IntPtr cppobjptr, int absPositionStart, double msecEnd);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern long VIS_VSM_WIVSMSequence_numSampleInFrame(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern double VIS_VSM_WIVSMSequence_msecFromSample(IntPtr cppobjptr, long sample, VSMSamplingRate samplingRate);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern long VIS_VSM_WIVSMSequence_sampleFromMsec(IntPtr cppobjptr, double msec, VSMSamplingRate samplingRate);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern int VIS_VSM_WIVSMSequence_currentPosition(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern void VIS_VSM_WIVSMSequence_setCurrentPosition(IntPtr cppobjptr, int absPosition);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern void VIS_VSM_WIVSMSequence_loopRange(IntPtr cppobjptr, out VSMLoopRange pVSMLoopRangeData);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_setLoopRange(IntPtr cppobjptr, [In] ref VSMLoopRange pVSMLoopRangeData);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_isLoopOn(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern void VIS_VSM_WIVSMSequence_setLoopOn(IntPtr cppobjptr, [MarshalAs(UnmanagedType.U1)] bool loopOn);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern int VIS_VSM_WIVSMSequence_presendTime(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern VSMSamplingRate VIS_VSM_WIVSMSequence_samplingRate(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_setSamplingRate(IntPtr cppobjptr, VSMSamplingRate samplingRate);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern void VIS_VSM_WIVSMSequence_startAsyncRendering(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern void VIS_VSM_WIVSMSequence_stopAsyncRendering(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_canAsyncRendering(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern UIntPtr VIS_VSM_WIVSMSequence_rendererConcurrency(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern UIntPtr VIS_VSM_WIVSMSequence_defaultRendererConcurrency(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern UIntPtr VIS_VSM_WIVSMSequence_setRendererConcurrency(IntPtr cppobjptr, UIntPtr size_t_concurrency);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_addRendererObserver(IntPtr cppobjptr, IntPtr pIVSMRendererObserver);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_removeRendererObserver(IntPtr cppobjptr, IntPtr pIVSMRendererObserver);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_canInvokeRendererObservers(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern void VIS_VSM_WIVSMSequence_invokeRendererObservers(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_isFinishedRendering(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_renderMidiPart(IntPtr cppobjptr, IntPtr pIVSMMidiPart);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern UIntPtr VIS_VSM_WIVSMSequence_maxUndoCount(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern void VIS_VSM_WIVSMSequence_setMaxUndoCount(IntPtr cppobjptr, UIntPtr size_t_maxUndoCount);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_isStaged(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_commit(IntPtr cppobjptr, [MarshalAs(UnmanagedType.U1)] bool updateHistory);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_rollback(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_canUndo(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern void VIS_VSM_WIVSMSequence_undo(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_canRedo(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern void VIS_VSM_WIVSMSequence_redo(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern UIntPtr VIS_VSM_WIVSMSequence_numTempo(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMSequence_tempo(IntPtr cppobjptr, UIntPtr size_t_index);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_hasTempo(IntPtr cppobjptr, IntPtr pIVSMTempo);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern int VIS_VSM_WIVSMSequence_minTempoValue(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern int VIS_VSM_WIVSMSequence_maxTempoValue(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern int VIS_VSM_WIVSMSequence_defaultTempoValue(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMSequence_insertTempo(IntPtr cppobjptr, int relPosition, int value);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMSequence_duplicateTempo(IntPtr cppobjptr, int relPosition, IntPtr pIVSMTempo);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_removeTempo(IntPtr cppobjptr, IntPtr pIVSMTempo);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_moveTempo(IntPtr cppobjptr, int relPosition, IntPtr pIVSMTempo);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_isTempoTrackFolded(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern void VIS_VSM_WIVSMSequence_foldTempoTrack(IntPtr cppobjptr, [MarshalAs(UnmanagedType.U1)] bool isFolded);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern double VIS_VSM_WIVSMSequence_heightTempoTrack(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_setHeightTempoTrack(IntPtr cppobjptr, double height);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern UIntPtr VIS_VSM_WIVSMSequence_numTimeSig(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMSequence_timeSig(IntPtr cppobjptr, UIntPtr size_t_index);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_hasTimeSig(IntPtr cppobjptr, IntPtr timeSig);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern void VIS_VSM_WIVSMSequence_minTimeSigData(IntPtr cppobjptr, out VSMTimeSigEvent timeSig);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern void VIS_VSM_WIVSMSequence_maxTimeSigData(IntPtr cppobjptr, out VSMTimeSigEvent timeSig);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern void VIS_VSM_WIVSMSequence_defaultTimeSigData(IntPtr cppobjptr, out VSMTimeSigEvent timeSig);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMSequence_insertTimeSig(IntPtr cppobjptr, int bar, [In] ref VSMTimeSigEvent timeSig);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMSequence_dupulicateTimeSig(IntPtr cppobjptr, int bar, IntPtr pIVSMTimeSig);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_removeTimeSig(IntPtr cppobjptr, IntPtr pIVSMTimeSig);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_moveTimeSig(IntPtr cppobjptr, int bar, IntPtr pIVSMTimeSig);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_isTimeSigTrackFolded(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern void VIS_VSM_WIVSMSequence_foldTimeSigTrack(IntPtr cppobjptr, [MarshalAs(UnmanagedType.U1)] bool isFolded);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern UIntPtr VIS_VSM_WIVSMSequence_numMasterVolume(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMSequence_masterVolume(IntPtr cppobjptr, UIntPtr size_t_index);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_hasMasterVolume(IntPtr cppobjptr, IntPtr pIVSMMasterVolume);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern int VIS_VSM_WIVSMSequence_minVolumeValue(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern int VIS_VSM_WIVSMSequence_maxVolumeValue(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern int VIS_VSM_WIVSMSequence_defaultVolumeValue(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMSequence_insertMasterVolume(IntPtr cppobjptr, int relPosition, int value);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMSequence_duplicateMasterVolume(IntPtr cppobjptr, int relPosition, IntPtr pIVSMMasterVolume);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_removeMasterVolume(IntPtr cppobjptr, IntPtr pIVSMMasterVolume);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_moveMasterVolume(IntPtr cppobjptr, int relPosition, IntPtr pIVSMMasterVolume);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_isMasterVolumeTrackFolded(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern void VIS_VSM_WIVSMSequence_foldMasterVolumeTrack(IntPtr cppobjptr, [MarshalAs(UnmanagedType.U1)] bool isFolded);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern double VIS_VSM_WIVSMSequence_heightMasterVolumeTrack(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_setHeightMasterVolumeTrack(IntPtr cppobjptr, double height);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern UIntPtr VIS_VSM_WIVSMSequence_numTrack(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMSequence_track(IntPtr cppobjptr, UIntPtr size_t_index);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_hasTrack(IntPtr cppobjptr, IntPtr pIVSMTrack);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMSequence_insertAudioTrack(IntPtr cppobjptr, UIntPtr size_t_index, [MarshalAs(UnmanagedType.LPWStr), In] string name);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMSequence_insertMidiTrack(IntPtr cppobjptr, UIntPtr size_t_index, [MarshalAs(UnmanagedType.LPWStr), In] string name);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMSequence_duplicateTrack(IntPtr cppobjptr, UIntPtr size_t_index, IntPtr pIVSMTrack);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_removeTrack(IntPtr cppobjptr, IntPtr pIVSMTrack);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_moveTrack(IntPtr cppobjptr, UIntPtr size_t_fromIndex, UIntPtr size_t_toIndex);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern UIntPtr VIS_VSM_WIVSMSequence_maxNumTrack(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMSequence_effectManager(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern IntPtr VIS_VSM_WIVSMSequence_luaController(IntPtr cppobjptr);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern void VIS_VSM_WIVSMSequence_setLuaController(IntPtr cppobjptr, IntPtr pLuaController);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    [return: MarshalAs(UnmanagedType.U1)]
    private static extern bool VIS_VSM_WIVSMSequence_addUpdateObserver(IntPtr cppobjptr, IntPtr pIVSMUpdateObserver);

    [DllImport("vsm", CallingConvention = CallingConvention.Cdecl)]
    private static extern void VIS_VSM_WIVSMSequence_removeUpdateObserver(IntPtr cppobjptr, IntPtr pIVSMUpdateObserver);
    """
    pass
    
def load_vsm_path():
    global vsm
    os.chdir(path)
    vsm = ctypes.cdll.LoadLibrary("vsm.dll")
    load_vsm()
    GlobalTempo.load_vsm_dll(vsm)
 
def load_vsm_dll(vsmdll):
    global vsm
    vsm = vsmdll
    load_vsm()
    GlobalTempo.load_vsm_dll(vsm)
    
class WIVSMSequence:
    
    _cppObjPtr = csharptypes.IntPtr.Zero
    _globalTempo = None
    _isCreateUnmanagedObj = None
    """
    private const double _defaultHeightTempoTrack = 20.0;
    private const double _defaultHeightMasterVolumeTrack = 20.0;
    private const double _minHeightTempoTrack = 20.0;
    private const double _minHeightMasterVolumeTrack = 20.0;
    private const double _autoNormalizeMsec = 30.0;
    private const int _minLoopRange = 480;

    public static explicit operator IntPtr(WIVSMSequence obj)
    {
      return obj._cppObjPtr;
    }

    public override bool Equals(object obj)
    {
      if (obj == null)
        return false;
      WIVSMSequence wivsmSequence = obj as WIVSMSequence;
      if (wivsmSequence == null)
        return false;
      return this._cppObjPtr == wivsmSequence._cppObjPtr;
    }

    public override int GetHashCode()
    {
      return (int) this._cppObjPtr.ToInt64();
    }
    """

    def __init__(self, pSequence, isCreateUnmanagedObj = False):
        if (pSequence == csharptypes.IntPtr.Zero):
            raise csharptypes.ArgumentException("アンマネージオブジェクトではない")
        self._globalTempo = GlobalTempo.GlobalTempo(pSequence)
        self._isCreateUnmanagedObj = isCreateUnmanagedObj
        self._cppObjPtr = pSequence

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if (self._isCreateUnmanagedObj && self._cppObjPtr != csharptypes.IntPtr.Zero):
            raise csharptypes.ApplicationException("アンマネージオブジェクトが破棄されていない")
    """
    ~WIVSMSequence()
    {
      if (this._isCreateUnmanagedObj && this._cppObjPtr != IntPtr.Zero)
        throw new ApplicationException("アンマネージオブジェクトが破棄されていない");
    }

    public VSMResult LastError
    {
      get
      {
        return WIVSMSequence.VIS_VSM_WIVSMSequence_lastError(this._cppObjPtr);
      }
    }

    public bool IsOpen
    {
      get
      {
        return this._cppObjPtr != IntPtr.Zero;
      }
    }

    public bool IsDirty
    {
      get
      {
        return WIVSMSequence.VIS_VSM_WIVSMSequence_isDirty(this._cppObjPtr);
      }
    }

    public string Title
    {
      get
      {
        return Marshal.PtrToStringUni(WIVSMSequence.VIS_VSM_WIVSMSequence_title(this._cppObjPtr));
      }
      set
      {
        WIVSMSequence.VIS_VSM_WIVSMSequence_setTitle(this._cppObjPtr, value);
      }
    }

    public long NumSampleInFrame
    {
      get
      {
        return WIVSMSequence.VIS_VSM_WIVSMSequence_numSampleInFrame(this._cppObjPtr);
      }
    }

    public VSMAbsTick CurrentPosition
    {
      get
      {
        return new VSMAbsTick(WIVSMSequence.VIS_VSM_WIVSMSequence_currentPosition(this._cppObjPtr));
      }
      set
      {
        WIVSMSequence.VIS_VSM_WIVSMSequence_setCurrentPosition(this._cppObjPtr, value.Tick);
      }
    }

    public bool IsLoopOn
    {
      get
      {
        return WIVSMSequence.VIS_VSM_WIVSMSequence_isLoopOn(this._cppObjPtr);
      }
      set
      {
        WIVSMSequence.VIS_VSM_WIVSMSequence_setLoopOn(this._cppObjPtr, value);
      }
    }

    public VSMLoopRange LoopRange
    {
      get
      {
        VSMLoopRange pVSMLoopRangeData;
        WIVSMSequence.VIS_VSM_WIVSMSequence_loopRange(this._cppObjPtr, out pVSMLoopRangeData);
        return pVSMLoopRangeData;
      }
      set
      {
        if (!WIVSMSequence.VIS_VSM_WIVSMSequence_setLoopRange(this._cppObjPtr, ref value))
          throw new ApplicationException("ループ範囲設定に失敗した");
      }
    }

    public int PresendTime
    {
      get
      {
        return WIVSMSequence.VIS_VSM_WIVSMSequence_presendTime(this._cppObjPtr);
      }
    }

    public bool IsStaged
    {
      get
      {
        return WIVSMSequence.VIS_VSM_WIVSMSequence_isStaged(this._cppObjPtr);
      }
    }

    public bool CanInvokeRendererObservers
    {
      get
      {
        return WIVSMSequence.VIS_VSM_WIVSMSequence_canInvokeRendererObservers(this._cppObjPtr);
      }
    }

    public bool IsFinishedRendering
    {
      get
      {
        return WIVSMSequence.VIS_VSM_WIVSMSequence_isFinishedRendering(this._cppObjPtr);
      }
    }

    public GlobalTempo GlobalTempo
    {
      get
      {
        return this._globalTempo;
      }
    }

    public ulong NumTempos
    {
      get
      {
        UIntPtr num = WIVSMSequence.VIS_VSM_WIVSMSequence_numTempo(this._cppObjPtr);
        if (UIntPtr.Size != 4)
          return num.ToUInt64();
        return (ulong) num.ToUInt32();
      }
    }

    public bool IsTempoTrackFolded
    {
      get
      {
        return WIVSMSequence.VIS_VSM_WIVSMSequence_isTempoTrackFolded(this._cppObjPtr);
      }
      set
      {
        WIVSMSequence.VIS_VSM_WIVSMSequence_foldTempoTrack(this._cppObjPtr, value);
      }
    }

    public double HeightTempoTrack
    {
      get
      {
        double num = WIVSMSequence.VIS_VSM_WIVSMSequence_heightTempoTrack(this._cppObjPtr);
        if (num > 0.0)
          return num;
        return 20.0;
      }
      set
      {
        WIVSMSequence.VIS_VSM_WIVSMSequence_setHeightTempoTrack(this._cppObjPtr, value);
      }
    }

    public ulong NumTimeSigs
    {
      get
      {
        UIntPtr num = WIVSMSequence.VIS_VSM_WIVSMSequence_numTimeSig(this._cppObjPtr);
        if (UIntPtr.Size != 4)
          return num.ToUInt64();
        return (ulong) num.ToUInt32();
      }
    }

    public bool IsTimeSigTrackFolded
    {
      get
      {
        return WIVSMSequence.VIS_VSM_WIVSMSequence_isTimeSigTrackFolded(this._cppObjPtr);
      }
      set
      {
        WIVSMSequence.VIS_VSM_WIVSMSequence_foldTimeSigTrack(this._cppObjPtr, value);
      }
    }

    public VSMTimeSigEvent MinTimeSigValue
    {
      get
      {
        VSMTimeSigEvent timeSig;
        WIVSMSequence.VIS_VSM_WIVSMSequence_minTimeSigData(this._cppObjPtr, out timeSig);
        return timeSig;
      }
    }

    public VSMTimeSigEvent MaxTimeSigValue
    {
      get
      {
        VSMTimeSigEvent timeSig;
        WIVSMSequence.VIS_VSM_WIVSMSequence_maxTimeSigData(this._cppObjPtr, out timeSig);
        return timeSig;
      }
    }

    public VSMTimeSigEvent DefaultTimeSigValue
    {
      get
      {
        VSMTimeSigEvent timeSig;
        WIVSMSequence.VIS_VSM_WIVSMSequence_defaultTimeSigData(this._cppObjPtr, out timeSig);
        return timeSig;
      }
    }

    public ulong NumMasterVolumes
    {
      get
      {
        UIntPtr num = WIVSMSequence.VIS_VSM_WIVSMSequence_numMasterVolume(this._cppObjPtr);
        if (UIntPtr.Size != 4)
          return num.ToUInt64();
        return (ulong) num.ToUInt32();
      }
    }

    public bool IsMasterVolumeTrackFolded
    {
      get
      {
        return WIVSMSequence.VIS_VSM_WIVSMSequence_isMasterVolumeTrackFolded(this._cppObjPtr);
      }
      set
      {
        WIVSMSequence.VIS_VSM_WIVSMSequence_foldMasterVolumeTrack(this._cppObjPtr, value);
      }
    }

    public double HeightMasterVolumeTrack
    {
      get
      {
        double num = WIVSMSequence.VIS_VSM_WIVSMSequence_heightMasterVolumeTrack(this._cppObjPtr);
        if (num > 0.0)
          return num;
        return 20.0;
      }
      set
      {
        WIVSMSequence.VIS_VSM_WIVSMSequence_setHeightMasterVolumeTrack(this._cppObjPtr, value);
      }
    }

    public ulong NumTrack
    {
      get
      {
        UIntPtr num = WIVSMSequence.VIS_VSM_WIVSMSequence_numTrack(this._cppObjPtr);
        if (UIntPtr.Size != 4)
          return num.ToUInt64();
        return (ulong) num.ToUInt32();
      }
    }

    public ulong MaxNumTrack
    {
      get
      {
        UIntPtr num = WIVSMSequence.VIS_VSM_WIVSMSequence_maxNumTrack(this._cppObjPtr);
        if (UIntPtr.Size != 4)
          return num.ToUInt64();
        return (ulong) num.ToUInt32();
      }
    }

    public WIVSMEffectManager EffectManager
    {
      get
      {
        IntPtr pManager = WIVSMSequence.VIS_VSM_WIVSMSequence_effectManager(this._cppObjPtr);
        if (!(pManager == IntPtr.Zero))
          return new WIVSMEffectManager(pManager);
        return (WIVSMEffectManager) null;
      }
    }

    public bool Save(string filePath, bool prettify)
    {
      if (filePath == null)
        return false;
      return WIVSMSequence.VIS_VSM_WIVSMSequence_save(this._cppObjPtr, filePath, prettify);
    }

    public bool Close()
    {
      if (!this._isCreateUnmanagedObj)
        return true;
      int num = WIVSMSequence.VIS_VSM_WIVSMSequence_close(this._cppObjPtr) ? 1 : 0;
      if (num == 0)
        return num != 0;
      this._globalTempo = (GlobalTempo) null;
      this._cppObjPtr = IntPtr.Zero;
      this._isCreateUnmanagedObj = false;
      return num != 0;
    }

    public VSMAbsTick GetTickFromBar(int bar)
    {
      return new VSMAbsTick(WIVSMSequence.VIS_VSM_WIVSMSequence_tickFromBar(this._cppObjPtr, bar));
    }

    public VSMSequenceTime GetSequenceTimeFromTick(VSMAbsTick absPosition)
    {
      VSMSequenceTime seqTime;
      WIVSMSequence.VIS_VSM_WIVSMSequence_timeFromTick(this._cppObjPtr, absPosition.Tick, out seqTime);
      return seqTime;
    }

    public double GetMillisecFromTick(VSMAbsTick absPositionStart, VSMAbsTick absPositionEnd)
    {
      return WIVSMSequence.VIS_VSM_WIVSMSequence_msecFromTick(this._cppObjPtr, absPositionStart.Tick, absPositionEnd.Tick);
    }

    public int GetTickFromMillisec(VSMAbsTick absPositionStart, double msecEnd)
    {
      return WIVSMSequence.VIS_VSM_WIVSMSequence_tickFromMsec(this._cppObjPtr, absPositionStart.Tick, msecEnd);
    }

    public double GetMillisecFromSample(long sample, VSMSamplingRate samplingRate)
    {
      return WIVSMSequence.VIS_VSM_WIVSMSequence_msecFromSample(this._cppObjPtr, sample, samplingRate);
    }

    public long GetSampleFromMillisec(double msec, VSMSamplingRate samplingRate)
    {
      return WIVSMSequence.VIS_VSM_WIVSMSequence_sampleFromMsec(this._cppObjPtr, msec, samplingRate);
    }

    public bool SetLoopRange(VSMLoopRange loopRange)
    {
      return WIVSMSequence.VIS_VSM_WIVSMSequence_setLoopRange(this._cppObjPtr, ref loopRange);
    }

    public VSMSamplingRate GetSamplingRate()
    {
      return WIVSMSequence.VIS_VSM_WIVSMSequence_samplingRate(this._cppObjPtr);
    }

    public bool SetSamplingRate(VSMSamplingRate samplingRate)
    {
      return WIVSMSequence.VIS_VSM_WIVSMSequence_setSamplingRate(this._cppObjPtr, samplingRate);
    }

    public void StartAsyncRendering()
    {
      WIVSMSequence.VIS_VSM_WIVSMSequence_startAsyncRendering(this._cppObjPtr);
    }

    public void StopAsyncRendering()
    {
      WIVSMSequence.VIS_VSM_WIVSMSequence_stopAsyncRendering(this._cppObjPtr);
    }

    public bool CanAsyncRendering()
    {
      return WIVSMSequence.VIS_VSM_WIVSMSequence_canAsyncRendering(this._cppObjPtr);
    }

    public ulong GetRendererConcurrency()
    {
      UIntPtr num = WIVSMSequence.VIS_VSM_WIVSMSequence_rendererConcurrency(this._cppObjPtr);
      if (UIntPtr.Size != 4)
        return num.ToUInt64();
      return (ulong) num.ToUInt32();
    }

    public ulong SetRendererConcurrency(ulong concurrency)
    {
      UIntPtr num = WIVSMSequence.VIS_VSM_WIVSMSequence_setRendererConcurrency(this._cppObjPtr, (UIntPtr) concurrency);
      if (UIntPtr.Size != 4)
        return num.ToUInt64();
      return (ulong) num.ToUInt32();
    }

    public ulong GetDefaultRendererConcurrency()
    {
      UIntPtr num = WIVSMSequence.VIS_VSM_WIVSMSequence_defaultRendererConcurrency(this._cppObjPtr);
      if (UIntPtr.Size != 4)
        return num.ToUInt64();
      return (ulong) num.ToUInt32();
    }

    public bool AddRendererObserver(WIVSMRendererObserver rendereObserver)
    {
      return WIVSMSequence.VIS_VSM_WIVSMSequence_addRendererObserver(this._cppObjPtr, (IntPtr) rendereObserver);
    }

    public bool RemoveRendererObserver(WIVSMRendererObserver rendereObserver)
    {
      return WIVSMSequence.VIS_VSM_WIVSMSequence_removeRendererObserver(this._cppObjPtr, (IntPtr) rendereObserver);
    }

    public void InvokeRendererObserver()
    {
      WIVSMSequence.VIS_VSM_WIVSMSequence_invokeRendererObservers(this._cppObjPtr);
    }

    [Obsolete("Use Async Rendering.", true)]
    public bool RenderMidiPart(WIVSMMidiPart midiPart)
    {
      if (midiPart == null)
        return false;
      return WIVSMSequence.VIS_VSM_WIVSMSequence_renderMidiPart(this._cppObjPtr, (IntPtr) midiPart);
    }

    public ulong GetMaxUndoCount()
    {
      UIntPtr num = WIVSMSequence.VIS_VSM_WIVSMSequence_maxUndoCount(this._cppObjPtr);
      if (UIntPtr.Size != 4)
        return num.ToUInt64();
      return (ulong) num.ToUInt32();
    }

    public void SetMaxUndoCount(ulong maxUndoCount)
    {
      WIVSMSequence.VIS_VSM_WIVSMSequence_setMaxUndoCount(this._cppObjPtr, (UIntPtr) maxUndoCount);
    }

    public bool Commit(bool updateHistory = true)
    {
      return WIVSMSequence.VIS_VSM_WIVSMSequence_commit(this._cppObjPtr, updateHistory);
    }

    public bool Rollback()
    {
      return WIVSMSequence.VIS_VSM_WIVSMSequence_rollback(this._cppObjPtr);
    }

    public bool CanUndo()
    {
      return WIVSMSequence.VIS_VSM_WIVSMSequence_canUndo(this._cppObjPtr);
    }

    public void Undo()
    {
      WIVSMSequence.VIS_VSM_WIVSMSequence_undo(this._cppObjPtr);
    }

    public bool CanRedo()
    {
      return WIVSMSequence.VIS_VSM_WIVSMSequence_canRedo(this._cppObjPtr);
    }

    public void Redo()
    {
      WIVSMSequence.VIS_VSM_WIVSMSequence_redo(this._cppObjPtr);
    }

    public WIVSMTempo GetTempo(ulong index)
    {
      IntPtr pTempo = WIVSMSequence.VIS_VSM_WIVSMSequence_tempo(this._cppObjPtr, (UIntPtr) index);
      if (!(pTempo == IntPtr.Zero))
        return new WIVSMTempo(pTempo);
      return (WIVSMTempo) null;
    }

    public bool HasTempo(WIVSMTempo tempo)
    {
      if (tempo == null)
        return false;
      return WIVSMSequence.VIS_VSM_WIVSMSequence_hasTempo(this._cppObjPtr, (IntPtr) tempo);
    }

    public int GetMinTempoValue()
    {
      return WIVSMSequence.VIS_VSM_WIVSMSequence_minTempoValue(this._cppObjPtr);
    }

    public int GetMaxTempoValue()
    {
      return WIVSMSequence.VIS_VSM_WIVSMSequence_maxTempoValue(this._cppObjPtr);
    }

    public int GetDefaultTempoValue()
    {
      return WIVSMSequence.VIS_VSM_WIVSMSequence_defaultTempoValue(this._cppObjPtr);
    }

    public WIVSMTempo InsertTempo(VSMRelTick relPosition, int value)
    {
      IntPtr pTempo = WIVSMSequence.VIS_VSM_WIVSMSequence_insertTempo(this._cppObjPtr, relPosition.Tick, value);
      if (!(pTempo == IntPtr.Zero))
        return new WIVSMTempo(pTempo);
      return (WIVSMTempo) null;
    }

    public WIVSMTempo DuplicateTempo(VSMRelTick relPosition, WIVSMTempo tempo)
    {
      if (tempo == null)
        return (WIVSMTempo) null;
      IntPtr pTempo = WIVSMSequence.VIS_VSM_WIVSMSequence_duplicateTempo(this._cppObjPtr, relPosition.Tick, (IntPtr) tempo);
      if (!(pTempo == IntPtr.Zero))
        return new WIVSMTempo(pTempo);
      return (WIVSMTempo) null;
    }

    public bool RemoveTempo(WIVSMTempo tempo)
    {
      if (tempo == null)
        return false;
      return WIVSMSequence.VIS_VSM_WIVSMSequence_removeTempo(this._cppObjPtr, (IntPtr) tempo);
    }

    public bool MoveTempo(VSMRelTick relPosition, WIVSMTempo tempo)
    {
      if (tempo == null)
        return false;
      return WIVSMSequence.VIS_VSM_WIVSMSequence_moveTempo(this._cppObjPtr, relPosition.Tick, (IntPtr) tempo);
    }

    public WIVSMTimeSig GetTimeSig(ulong index)
    {
      IntPtr pIVSMTimeSig = WIVSMSequence.VIS_VSM_WIVSMSequence_timeSig(this._cppObjPtr, (UIntPtr) index);
      if (!(pIVSMTimeSig == IntPtr.Zero))
        return new WIVSMTimeSig(pIVSMTimeSig);
      return (WIVSMTimeSig) null;
    }

    public bool HasTimeSig(WIVSMTimeSig timeSig)
    {
      if (timeSig == null)
        return false;
      return WIVSMSequence.VIS_VSM_WIVSMSequence_hasTimeSig(this._cppObjPtr, (IntPtr) timeSig);
    }

    public WIVSMTimeSig InsertTimeSig(int bar, VSMTimeSigEvent timeSigEvent)
    {
      IntPtr pIVSMTimeSig = WIVSMSequence.VIS_VSM_WIVSMSequence_insertTimeSig(this._cppObjPtr, bar, ref timeSigEvent);
      if (!(pIVSMTimeSig == IntPtr.Zero))
        return new WIVSMTimeSig(pIVSMTimeSig);
      return (WIVSMTimeSig) null;
    }

    public WIVSMTimeSig DuplicateTimeSig(int bar, WIVSMTimeSig timeSig)
    {
      if (timeSig == null)
        return (WIVSMTimeSig) null;
      IntPtr pIVSMTimeSig = WIVSMSequence.VIS_VSM_WIVSMSequence_dupulicateTimeSig(this._cppObjPtr, bar, (IntPtr) timeSig);
      if (!(pIVSMTimeSig == IntPtr.Zero))
        return new WIVSMTimeSig(pIVSMTimeSig);
      return (WIVSMTimeSig) null;
    }

    public bool RemoveTimeSig(WIVSMTimeSig timeSig)
    {
      if (timeSig == null)
        return false;
      return WIVSMSequence.VIS_VSM_WIVSMSequence_removeTimeSig(this._cppObjPtr, (IntPtr) timeSig);
    }

    public bool MoveTimeSig(int bar, WIVSMTimeSig timeSig)
    {
      if (timeSig == null)
        return false;
      return WIVSMSequence.VIS_VSM_WIVSMSequence_moveTimeSig(this._cppObjPtr, bar, (IntPtr) timeSig);
    }

    public WIVSMMasterVolume GetMasterVolume(ulong index)
    {
      IntPtr pMasterVolume = WIVSMSequence.VIS_VSM_WIVSMSequence_masterVolume(this._cppObjPtr, (UIntPtr) index);
      if (!(pMasterVolume == IntPtr.Zero))
        return new WIVSMMasterVolume(pMasterVolume);
      return (WIVSMMasterVolume) null;
    }

    public bool HasMasterVolume(WIVSMMasterVolume masterVolume)
    {
      if (masterVolume == null)
        return false;
      return WIVSMSequence.VIS_VSM_WIVSMSequence_hasMasterVolume(this._cppObjPtr, (IntPtr) masterVolume);
    }

    public int GetMinVolumeValue()
    {
      return WIVSMSequence.VIS_VSM_WIVSMSequence_minVolumeValue(this._cppObjPtr);
    }

    public int GetMaxVolumeValue()
    {
      return WIVSMSequence.VIS_VSM_WIVSMSequence_maxVolumeValue(this._cppObjPtr);
    }

    public int GetDefaultVolumeValue()
    {
      return WIVSMSequence.VIS_VSM_WIVSMSequence_defaultVolumeValue(this._cppObjPtr);
    }

    public WIVSMMasterVolume InsertMasterVolume(VSMRelTick relPosition, int value)
    {
      IntPtr pMasterVolume = WIVSMSequence.VIS_VSM_WIVSMSequence_insertMasterVolume(this._cppObjPtr, relPosition.Tick, value);
      if (!(pMasterVolume == IntPtr.Zero))
        return new WIVSMMasterVolume(pMasterVolume);
      return (WIVSMMasterVolume) null;
    }

    public WIVSMMasterVolume DuplicateMasterVolume(VSMRelTick relPosition, WIVSMMasterVolume masterVolume)
    {
      if (masterVolume == null)
        return (WIVSMMasterVolume) null;
      IntPtr pMasterVolume = WIVSMSequence.VIS_VSM_WIVSMSequence_duplicateMasterVolume(this._cppObjPtr, relPosition.Tick, (IntPtr) masterVolume);
      if (!(pMasterVolume == IntPtr.Zero))
        return new WIVSMMasterVolume(pMasterVolume);
      return (WIVSMMasterVolume) null;
    }

    public bool RemoveMasterVolume(WIVSMMasterVolume masterVolume)
    {
      if (masterVolume == null)
        return false;
      return WIVSMSequence.VIS_VSM_WIVSMSequence_removeMasterVolume(this._cppObjPtr, (IntPtr) masterVolume);
    }

    public bool MoveMasterVolume(VSMRelTick relPosition, WIVSMMasterVolume masterVolume)
    {
      if (masterVolume == null)
        return false;
      return WIVSMSequence.VIS_VSM_WIVSMSequence_moveMasterVolume(this._cppObjPtr, relPosition.Tick, (IntPtr) masterVolume);
    }

    public WIVSMTrack GetTrack(ulong index)
    {
      IntPtr pTrack = WIVSMSequence.VIS_VSM_WIVSMSequence_track(this._cppObjPtr, (UIntPtr) index);
      if (!(pTrack == IntPtr.Zero))
        return new WIVSMTrack(pTrack);
      return (WIVSMTrack) null;
    }

    public bool HasTrack(WIVSMTrack track)
    {
      if (track == null)
        return false;
      return WIVSMSequence.VIS_VSM_WIVSMSequence_hasTrack(this._cppObjPtr, (IntPtr) track);
    }

    private WIVSMMidiTrack InsertMidiTrack(ulong index, string name)
    {
      if (name == null)
        return (WIVSMMidiTrack) null;
      IntPtr pTrack = WIVSMSequence.VIS_VSM_WIVSMSequence_insertMidiTrack(this._cppObjPtr, (UIntPtr) index, name);
      if (!(pTrack == IntPtr.Zero))
        return new WIVSMMidiTrack(pTrack);
      return (WIVSMMidiTrack) null;
    }

    private WIVSMAudioTrack InsertAudioTrack(ulong index, string name)
    {
      if (name == null)
        return (WIVSMAudioTrack) null;
      IntPtr pTrack = WIVSMSequence.VIS_VSM_WIVSMSequence_insertAudioTrack(this._cppObjPtr, (UIntPtr) index, name);
      if (!(pTrack == IntPtr.Zero))
        return new WIVSMAudioTrack(pTrack);
      return (WIVSMAudioTrack) null;
    }

    public WIVSMTrack DuplicateTrack(ulong index, WIVSMTrack track)
    {
      if (track == null)
        return (WIVSMTrack) null;
      IntPtr pTrack = WIVSMSequence.VIS_VSM_WIVSMSequence_duplicateTrack(this._cppObjPtr, (UIntPtr) index, (IntPtr) track);
      if (!(pTrack == IntPtr.Zero))
        return new WIVSMTrack(pTrack);
      return (WIVSMTrack) null;
    }

    public bool RemoveTrack(WIVSMTrack track)
    {
      if (track == null)
        return false;
      return WIVSMSequence.VIS_VSM_WIVSMSequence_removeTrack(this._cppObjPtr, (IntPtr) track);
    }

    public bool MoveTrack(ulong fromIndex, ulong toIndex)
    {
      return WIVSMSequence.VIS_VSM_WIVSMSequence_moveTrack(this._cppObjPtr, (UIntPtr) fromIndex, (UIntPtr) toIndex);
    }

    public IntPtr GetLuaController()
    {
      return WIVSMSequence.VIS_VSM_WIVSMSequence_luaController(this._cppObjPtr);
    }

    public void SetLuaController(IntPtr pLuaController)
    {
      WIVSMSequence.VIS_VSM_WIVSMSequence_setLuaController(this._cppObjPtr, pLuaController);
    }

    public bool AddUpdateObserver(WIVSMUpdateObserver observer)
    {
      return WIVSMSequence.VIS_VSM_WIVSMSequence_addUpdateObserver(this._cppObjPtr, (IntPtr) observer);
    }

    public void RemoveUpdateObserver(WIVSMUpdateObserver observer)
    {
      WIVSMSequence.VIS_VSM_WIVSMSequence_removeUpdateObserver(this._cppObjPtr, (IntPtr) observer);
    }

    public static double MinHeightTempoTrack
    {
      get
      {
        return 20.0;
      }
    }

    public static double MinHeightMasterVolumeTrack
    {
      get
      {
        return 20.0;
      }
    }

    public static double AutoNormalizeMsec
    {
      get
      {
        return 30.0;
      }
    }

    public static int MinLoopRange
    {
      get
      {
        return 480;
      }
    }

    public List<WIVSMTempo> Tempos
    {
      get
      {
        List<WIVSMTempo> wivsmTempoList = new List<WIVSMTempo>();
        for (ulong index = 0; index < this.NumTempos; ++index)
          wivsmTempoList.Add(this.GetTempo(index));
        return wivsmTempoList;
      }
    }

    public bool HasSelectedTempo
    {
      get
      {
        foreach (WIVSMTempo tempo in this.Tempos)
        {
          if (tempo.IsSelected)
            return true;
        }
        return false;
      }
    }

    public List<WIVSMTempo> SelectedTempos
    {
      get
      {
        List<WIVSMTempo> wivsmTempoList = new List<WIVSMTempo>();
        foreach (WIVSMTempo tempo in this.Tempos)
        {
          if (tempo.IsSelected)
            wivsmTempoList.Add(tempo);
        }
        return wivsmTempoList;
      }
    }

    public List<WIVSMTimeSig> TimeSigs
    {
      get
      {
        List<WIVSMTimeSig> wivsmTimeSigList = new List<WIVSMTimeSig>();
        for (ulong index = 0; index < this.NumTimeSigs; ++index)
          wivsmTimeSigList.Add(this.GetTimeSig(index));
        return wivsmTimeSigList;
      }
    }

    public bool HasSelectedTimeSig
    {
      get
      {
        foreach (WIVSMTimeSig timeSig in this.TimeSigs)
        {
          if (timeSig.IsSelected)
            return true;
        }
        return false;
      }
    }

    public List<WIVSMTimeSig> SelectedTimeSigs
    {
      get
      {
        List<WIVSMTimeSig> wivsmTimeSigList = new List<WIVSMTimeSig>();
        foreach (WIVSMTimeSig timeSig in this.TimeSigs)
        {
          if (timeSig.IsSelected)
            wivsmTimeSigList.Add(timeSig);
        }
        return wivsmTimeSigList;
      }
    }

    public List<WIVSMMasterVolume> MasterVolumes
    {
      get
      {
        List<WIVSMMasterVolume> wivsmMasterVolumeList = new List<WIVSMMasterVolume>();
        for (ulong index = 0; index < this.NumMasterVolumes; ++index)
          wivsmMasterVolumeList.Add(this.GetMasterVolume(index));
        return wivsmMasterVolumeList;
      }
    }

    public bool HasSelectedMasterVolume
    {
      get
      {
        foreach (WIVSMBreakPoint masterVolume in this.MasterVolumes)
        {
          if (masterVolume.IsSelected)
            return true;
        }
        return false;
      }
    }

    public List<WIVSMMasterVolume> SelectedMasterVolumes
    {
      get
      {
        List<WIVSMMasterVolume> wivsmMasterVolumeList = new List<WIVSMMasterVolume>();
        foreach (WIVSMMasterVolume masterVolume in this.MasterVolumes)
        {
          if (masterVolume.IsSelected)
            wivsmMasterVolumeList.Add(masterVolume);
        }
        return wivsmMasterVolumeList;
      }
    }

    public bool IsEditableMasterVolume
    {
      get
      {
        if (this.NumMasterVolumes == 0UL)
          return true;
        if (this.NumMasterVolumes == 1UL)
          return this.GetMasterVolume(0UL).RelPosition.Tick == 0;
        return false;
      }
    }

    public List<WIVSMTrack> Tracks
    {
      get
      {
        List<WIVSMTrack> wivsmTrackList = new List<WIVSMTrack>();
        for (ulong index = 0; index < this.NumTrack; ++index)
          wivsmTrackList.Add(this.GetTrack(index));
        return wivsmTrackList;
      }
    }

    public bool HasSelectedTrack
    {
      get
      {
        foreach (WIVSMTrack track in this.Tracks)
        {
          if (track.IsSelected)
            return true;
        }
        return false;
      }
    }

    public List<WIVSMTrack> SelectedTracks
    {
      get
      {
        List<WIVSMTrack> wivsmTrackList = new List<WIVSMTrack>();
        foreach (WIVSMTrack track in this.Tracks)
        {
          if (track.IsSelected)
            wivsmTrackList.Add(track);
        }
        return wivsmTrackList;
      }
    }

    public WIVSMTrack InsertTrackEx(ulong index, VSMTrackType type, string name)
    {
      WIVSMTrack wivsmTrack = (WIVSMTrack) null;
      switch (type)
      {
        case VSMTrackType.Midi:
          wivsmTrack = (WIVSMTrack) this.InsertMidiTrack(index, name);
          break;
        case VSMTrackType.Audio:
          wivsmTrack = (WIVSMTrack) this.InsertAudioTrack(index, name);
          break;
      }
      if (wivsmTrack == null)
        return (WIVSMTrack) null;
      if (wivsmTrack.InsertVolume(new VSMRelTick(0), WIVSMVolume.DefaultValue) == null)
        return (WIVSMTrack) null;
      if (wivsmTrack.InsertPanpot(new VSMRelTick(0), WIVSMVolume.DefaultValue) == null)
        return (WIVSMTrack) null;
      wivsmTrack.HeightVolumeLane = WIVSMTrack.DefaultHeightVolumeLane;
      wivsmTrack.HeightPanpotLane = WIVSMTrack.DefaultHeightPanpotLane;
      return wivsmTrack;
    }

    public List<WIVSMMidiTrack> MidiTracks
    {
      get
      {
        List<WIVSMMidiTrack> wivsmMidiTrackList = new List<WIVSMMidiTrack>();
        for (ulong index = 0; index < this.NumTrack; ++index)
        {
          WIVSMTrack track = this.GetTrack(index);
          if (track.Type == VSMTrackType.Midi)
            wivsmMidiTrackList.Add(new WIVSMMidiTrack(track));
        }
        return wivsmMidiTrackList;
      }
    }

    public bool HasSelectedMidiTrack
    {
      get
      {
        foreach (WIVSMTrack midiTrack in this.MidiTracks)
        {
          if (midiTrack.IsSelected)
            return true;
        }
        return false;
      }
    }

    public List<WIVSMMidiTrack> SelectedMidiTracks
    {
      get
      {
        List<WIVSMMidiTrack> wivsmMidiTrackList = new List<WIVSMMidiTrack>();
        foreach (WIVSMMidiTrack midiTrack in this.MidiTracks)
        {
          if (midiTrack.IsSelected)
            wivsmMidiTrackList.Add(midiTrack);
        }
        return wivsmMidiTrackList;
      }
    }

    public List<WIVSMAudioTrack> AudioTracks
    {
      get
      {
        List<WIVSMAudioTrack> wivsmAudioTrackList = new List<WIVSMAudioTrack>();
        for (ulong index = 0; index < this.NumTrack; ++index)
        {
          WIVSMTrack track = this.GetTrack(index);
          if (track.Type == VSMTrackType.Audio)
            wivsmAudioTrackList.Add(new WIVSMAudioTrack(track));
        }
        return wivsmAudioTrackList;
      }
    }

    public bool HasSelectedPart
    {
      get
      {
        foreach (WIVSMTrack track in this.Tracks)
        {
          if (track.HasSelectedPart)
            return true;
        }
        return false;
      }
    }

    public List<WIVSMPart> SelectedParts
    {
      get
      {
        List<WIVSMPart> wivsmPartList = new List<WIVSMPart>();
        foreach (WIVSMTrack track in this.Tracks)
        {
          foreach (WIVSMPart selectedPart in track.SelectedParts)
            wivsmPartList.Add(selectedPart);
        }
        return wivsmPartList;
      }
    }

    public List<WIVSMMidiPart> MidiParts
    {
      get
      {
        List<WIVSMMidiPart> wivsmMidiPartList = new List<WIVSMMidiPart>();
        foreach (WIVSMMidiTrack midiTrack in this.MidiTracks)
        {
          for (ulong index = 0; index < midiTrack.NumParts; ++index)
            wivsmMidiPartList.Add(midiTrack.GetPart(index));
        }
        return wivsmMidiPartList;
      }
    }

    public List<WIVSMMidiPart> SelectedMidiParts
    {
      get
      {
        List<WIVSMMidiPart> wivsmMidiPartList = new List<WIVSMMidiPart>();
        foreach (WIVSMPart selectedPart in this.SelectedParts)
        {
          if (selectedPart.Type == VSMPartType.Midi)
            wivsmMidiPartList.Add(new WIVSMMidiPart(selectedPart));
        }
        return wivsmMidiPartList;
      }
    }

    public List<WIVSMAudioPart> AudioParts
    {
      get
      {
        List<WIVSMAudioPart> wivsmAudioPartList = new List<WIVSMAudioPart>();
        foreach (WIVSMAudioTrack audioTrack in this.AudioTracks)
        {
          for (ulong index = 0; index < audioTrack.NumParts; ++index)
            wivsmAudioPartList.Add(audioTrack.GetPart(index));
        }
        return wivsmAudioPartList;
      }
    }

    public List<WIVSMAudioPart> SelectedAudioParts
    {
      get
      {
        List<WIVSMAudioPart> wivsmAudioPartList = new List<WIVSMAudioPart>();
        foreach (WIVSMPart selectedPart in this.SelectedParts)
        {
          if (selectedPart.Type == VSMPartType.Audio)
            wivsmAudioPartList.Add(new WIVSMAudioPart(selectedPart));
        }
        return wivsmAudioPartList;
      }
    }

    public bool HasSelectedTrackVolume
    {
      get
      {
        foreach (WIVSMTrack track in this.Tracks)
        {
          if (track.HasSelectedVolume)
            return true;
        }
        return false;
      }
    }

    public List<WIVSMTrackVolume> SelectedTrackVolumes
    {
      get
      {
        List<WIVSMTrackVolume> wivsmTrackVolumeList = new List<WIVSMTrackVolume>();
        foreach (WIVSMTrack track in this.Tracks)
        {
          foreach (WIVSMTrackVolume selectedVolume in track.SelectedVolumes)
            wivsmTrackVolumeList.Add(selectedVolume);
        }
        return wivsmTrackVolumeList;
      }
    }

    public bool HasSelectedPanpot
    {
      get
      {
        foreach (WIVSMTrack track in this.Tracks)
        {
          if (track.HasSelectedPanpot)
            return true;
        }
        return false;
      }
    }

    public List<WIVSMPanpot> SelectedPanpots
    {
      get
      {
        List<WIVSMPanpot> wivsmPanpotList = new List<WIVSMPanpot>();
        foreach (WIVSMTrack track in this.Tracks)
        {
          foreach (WIVSMPanpot selectedPanpot in track.SelectedPanpots)
            wivsmPanpotList.Add(selectedPanpot);
        }
        return wivsmPanpotList;
      }
    }

    public int GetMostRecentBarFromTick(VSMAbsTick absPosition)
    {
      return this.GetSequenceTimeFromTick(absPosition).Bar;
    }

    public bool RemoveTempos(List<WIVSMTempo> tempos)
    {
      bool flag = true;
      foreach (WIVSMTempo tempo in tempos)
      {
        if (tempo.AbsPosition.Tick == 0)
        {
          tempo.Value = WIVSMTempo.DefaultValue;
        }
        else
        {
          flag = this.RemoveTempo(tempo);
          if (!flag)
            break;
        }
      }
      return flag;
    }

    public bool RemoveMasterVolumes(List<WIVSMMasterVolume> volumes)
    {
      bool flag = true;
      foreach (WIVSMMasterVolume volume in volumes)
      {
        if (volume.AbsPosition.Tick == 0)
        {
          volume.Value = WIVSMVolume.DefaultValue;
        }
        else
        {
          flag = this.RemoveMasterVolume(volume);
          if (!flag)
            break;
        }
      }
      return flag;
    }

    public bool InterpolatedMasterVolume()
    {
      bool flag = false;
      if (0UL < this.NumMasterVolumes)
      {
        int tick1 = this.GetMasterVolume(0UL).RelPosition.Tick;
        if (0 < tick1)
          flag = true;
        else if (tick1 < 0)
        {
          int num1 = tick1;
          int num2 = num1;
          for (ulong index = 1; index < this.NumMasterVolumes; ++index)
          {
            int tick2 = this.GetMasterVolume(index).RelPosition.Tick;
            if (tick2 < 0)
              num2 = tick2;
            else
              break;
          }
          for (ulong numMasterVolumes = this.NumMasterVolumes; 0UL < numMasterVolumes; --numMasterVolumes)
          {
            WIVSMMasterVolume masterVolume = this.GetMasterVolume(numMasterVolumes - 1UL);
            if (masterVolume != null && num1 <= masterVolume.AbsPosition.Tick && (masterVolume.AbsPosition.Tick <= num2 && !this.RemoveMasterVolume(masterVolume)))
              return false;
          }
          if (this.NumMasterVolumes == 0UL || this.GetMasterVolume(0UL).RelPosition.Tick != 0)
            flag = true;
        }
      }
      else
        flag = true;
      return !flag || this.InsertMasterVolume(VSMRelTick.Zero, this.GetDefaultVolumeValue()) != null;
    }

    public bool Contains(WIVSMTrack targetTrack)
    {
      if (targetTrack == null)
        return false;
      foreach (WIVSMTrack track in this.Tracks)
      {
        if (targetTrack.Equals((object) track))
          return true;
      }
      return false;
    }

    public ulong IndexOf(WIVSMTrack track)
    {
      if (track == null)
        throw new ArgumentNullException("トラックオブジェクト引数がnull");
      for (ulong index = 0; index < this.NumTrack; ++index)
      {
        if (track.Equals((object) this.GetTrack(index)))
          return index;
      }
      throw new ApplicationException("シーケンスに指定トラックオブジェクトが存在しない");
    }

    public void SetAllMidiTrackRecording(bool isEnabled)
    {
      foreach (WIVSMMidiTrack midiTrack in this.MidiTracks)
        midiTrack.IsEnabledMidiRecording = isEnabled;
    }

    public void MatchMidiRecordingEnabledWithSelectedAllMidiTracks()
    {
      foreach (WIVSMMidiTrack midiTrack in this.MidiTracks)
      {
        if (midiTrack.IsEnabledMidiRecording != midiTrack.IsSelected)
          midiTrack.IsEnabledMidiRecording = midiTrack.IsSelected;
      }
    }

    public bool RemoveParts(List<WIVSMPart> parts)
    {
      bool flag = true;
      foreach (WIVSMPart part in parts)
      {
        flag = part.Parent.RemovePart(part);
        if (!flag)
          break;
      }
      return flag;
    }

    public bool RemoveTrackVolumes(List<WIVSMTrackVolume> volumes)
    {
      bool flag = true;
      foreach (WIVSMTrackVolume volume in volumes)
      {
        if (volume.AbsPosition.Tick == 0)
        {
          volume.Value = WIVSMVolume.DefaultValue;
        }
        else
        {
          flag = volume.Parent.RemoveVolume(volume);
          if (!flag)
            break;
        }
      }
      return flag;
    }

    public bool RemovePanpots(List<WIVSMPanpot> panpots)
    {
      bool flag = true;
      foreach (WIVSMPanpot panpot in panpots)
      {
        if (panpot.AbsPosition.Tick == 0)
        {
          panpot.Value = WIVSMPanpot.DefaultValue;
        }
        else
        {
          flag = panpot.Parent.RemovePanpot(panpot);
          if (!flag)
            break;
        }
      }
      return flag;
    }

    public VSMLoopRange CalcLoopRange(bool isStartMarker, int posTick)
    {
      int num1 = this.LoopRange.TickBegin;
      int num2 = this.LoopRange.TickEnd;
      if (isStartMarker)
        num1 = num2 - WIVSMSequence.MinLoopRange / 2 > posTick || posTick >= num2 + WIVSMSequence.MinLoopRange / 2 ? (posTick >= num2 ? Math.Max(posTick, num2 + WIVSMSequence.MinLoopRange) : Math.Min(posTick, num2 - WIVSMSequence.MinLoopRange)) : num2;
      else
        num2 = num1 - WIVSMSequence.MinLoopRange / 2 > posTick || posTick >= num1 + WIVSMSequence.MinLoopRange / 2 ? (posTick >= num1 ? Math.Max(posTick, num1 + WIVSMSequence.MinLoopRange) : Math.Min(posTick, num1 - WIVSMSequence.MinLoopRange)) : num1;
      if (num1 < 0)
        num1 = 0;
      if (num2 < 0)
        num2 = 0;
      return num1 >= num2 ? new VSMLoopRange(num2, num1) : new VSMLoopRange(num1, num2);
    }
    """
